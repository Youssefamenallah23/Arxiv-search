from __future__ import annotations

import argparse
from pathlib import Path
import sys
import time

from tqdm import tqdm

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.chunking import chunk_papers, proportional_overlap
from arxiv_rag.config import DEFAULT_EMBEDDING_MODELS
from arxiv_rag.embeddings import SentenceTransformerEncoder, CrossEncoderReranker
from arxiv_rag.generation import generate_answer
from arxiv_rag.generation_eval import (
    score_faithfulness,
    score_citation_accuracy,
    score_completeness,
)
from arxiv_rag.labels import load_labels, load_papers, qrels_for_split
from arxiv_rag.metrics import (
    evaluate_retrieval,
    recall_at_k,
    reciprocal_rank,
    ndcg_at_k,
    bootstrap_interval,
)
from arxiv_rag.retrieval import build_runs, collapse_reranked_chunk_ids, rank_chunks
from arxiv_rag.io import write_jsonl


def main() -> None:
    parser = argparse.ArgumentParser(
        description="End-to-end generation evaluation on the test split."
    )
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--labels", required=True)
    parser.add_argument("--model", default="bge-small")
    parser.add_argument("--reranker", default="BAAI/bge-reranker-base")
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--top-k-chunks", type=int, default=50)
    parser.add_argument("--top-k-papers", type=int, default=10)
    parser.add_argument(
        "--context-budget", type=int, default=5, help="Number of reranked chunks to pass to Gemini"
    )
    parser.add_argument("--llm-model", default="gemini-3.1-flash-lite")
    parser.add_argument("--output", default="reports/generation_eval_results.jsonl")
    parser.add_argument(
        "--skip-generation",
        action="store_true",
        help="Skip LLM calls, compute retrieval metrics only",
    )
    args = parser.parse_args()

    papers = load_papers(args.corpus)
    labels = [label for label in load_labels(args.labels) if label.split == "test"]
    qrels = qrels_for_split(labels, "test")

    if not labels:
        print("No test labels found.")
        return

    print(f"Loaded {len(labels)} test queries, {len(papers)} papers")

    # Chunk and embed
    overlap = proportional_overlap(args.chunk_size)
    chunks = chunk_papers(papers, chunk_size=args.chunk_size, overlap=overlap)
    chunk_by_id = {chunk.chunk_id: chunk for chunk in chunks}
    print(f"Built {len(chunks)} chunks")

    encoder = SentenceTransformerEncoder(DEFAULT_EMBEDDING_MODELS.get(args.model, args.model))
    chunk_vectors, embed_seconds = encoder.encode_documents([chunk.text for chunk in chunks])
    query_vectors, _ = encoder.encode_queries([label.query for label in labels])

    ranked_chunks = rank_chunks(
        query_vectors=query_vectors,
        chunk_vectors=chunk_vectors,
        chunks=chunks,
        top_k_chunks=args.top_k_chunks,
    )

    # Rerank
    print("Reranking...")
    reranker = CrossEncoderReranker(args.reranker)
    reranked_chunks_by_query: dict[str, list[dict]] = {}
    runs: dict[str, list[str]] = {}

    for query_index, label in enumerate(tqdm(labels, desc="reranking", unit="query")):
        candidates = [(chunk.chunk_id, chunk.text) for chunk in ranked_chunks[query_index]]
        ranked_chunk_ids, _ = reranker.rerank(label.query, candidates)
        runs[label.query_id] = collapse_reranked_chunk_ids(
            ranked_chunk_ids,
            chunk_by_id=chunk_by_id,
            top_k_papers=args.top_k_papers,
        )
        budget_ids = ranked_chunk_ids[: args.context_budget]
        reranked_chunks_by_query[label.query_id] = [
            {
                "chunk_id": cid,
                "paper_id": chunk_by_id[cid].paper_id,
                "title": chunk_by_id[cid].title,
                "text": chunk_by_id[cid].text,
            }
            for cid in budget_ids
        ]

    # Retrieval metrics
    retrieval_metrics = evaluate_retrieval(qrels, runs)
    print(f"Retrieval metrics: {retrieval_metrics}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for label in labels:
        chunk_dicts = reranked_chunks_by_query[label.query_id]
        relevant = qrels.get(label.query_id, set())
        retrieved = runs.get(label.query_id, [])

        row = {
            "query_id": label.query_id,
            "query": label.query,
            "retrieval": {
                "recall@5": recall_at_k(relevant, retrieved, 5),
                "recall@10": recall_at_k(relevant, retrieved, 10),
                "mrr": reciprocal_rank(relevant, retrieved),
                "ndcg@10": ndcg_at_k(relevant, retrieved, 10),
            },
        }

        if not args.skip_generation:
            print(f"Generating answer for {label.query_id}...", end=" ", flush=True)
            t0 = time.perf_counter()
            try:
                answer, gen_seconds, usage = generate_answer(
                    query=label.query,
                    chunks=chunk_dicts,
                    model_name=args.llm_model,
                )
                gen_latency = time.perf_counter() - t0
                print(f"{gen_latency:.1f}s")

                faithfulness_score, faith_results = score_faithfulness(answer, chunk_dicts)
                citation_score, cite_results = score_citation_accuracy(answer, chunk_dicts)

                expected_points = [label.query]
                completeness_score, compl_results = score_completeness(
                    label.query, answer, expected_points
                )

                row["generation"] = {
                    "answer": answer,
                    "faithfulness": faithfulness_score,
                    "citation_accuracy": citation_score,
                    "completeness": completeness_score,
                    "latency_seconds": gen_latency,
                    "llm_usage": usage,
                    "faithfulness_claims": faith_results,
                    "citation_results": cite_results,
                    "completeness_results": compl_results,
                }
            except Exception as exc:
                print(f"FAILED: {exc}")
                row["generation"] = {"error": str(exc)}

        rows.append(row)
        write_jsonl(output_path, rows)
        print(f"  saved ({len(rows)}/{len(labels)})")

    # Summary
    if not args.skip_generation:
        faith_scores = [r["generation"]["faithfulness"] for r in rows if "generation" in r]
        cite_scores = [r["generation"]["citation_accuracy"] for r in rows if "generation" in r]
        compl_scores = [r["generation"]["completeness"] for r in rows if "generation" in r]
        total_latency = sum(r["generation"]["latency_seconds"] for r in rows if "generation" in r)

        print("\n=== SUMMARY ===")
        print(f"Test queries: {len(rows)}")
        print(
            f"Retrieval: Recall@10={retrieval_metrics['recall@10']:.3f}, MRR={retrieval_metrics['mrr']:.3f}, NDCG@10={retrieval_metrics['ndcg@10']:.3f}"
        )
        if faith_scores:
            print(f"Faithfulness: {sum(faith_scores) / len(faith_scores):.3f}")
            print(f"Citation Accuracy: {sum(cite_scores) / len(cite_scores):.3f}")
            print(f"Completeness: {sum(compl_scores) / len(compl_scores):.3f}")
            print(f"Total LLM generation time: {total_latency:.1f}s")


if __name__ == "__main__":
    main()
