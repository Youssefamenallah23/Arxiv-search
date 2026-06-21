from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.chunking import chunk_papers, proportional_overlap
from arxiv_rag.config import DEFAULT_EMBEDDING_MODELS, DEFAULT_RERANKER_MODEL
from arxiv_rag.embeddings import CrossEncoderReranker, SentenceTransformerEncoder
from arxiv_rag.labels import load_labels, load_papers, qrels_for_split
from arxiv_rag.metrics import evaluate_retrieval
from arxiv_rag.retrieval import (
    build_runs,
    collapse_reranked_chunk_ids,
    rank_chunks,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare vector search vs vector + reranker.")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--labels", required=True)
    parser.add_argument("--split", choices=["train", "validation"], default="validation")
    parser.add_argument("--model", default="bge-small")
    parser.add_argument("--reranker", default=DEFAULT_RERANKER_MODEL)
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--top-k-chunks", type=int, default=50)
    parser.add_argument("--top-k-papers", type=int, default=10)
    parser.add_argument("--wandb", action="store_true")
    args = parser.parse_args()

    papers = load_papers(args.corpus)
    labels = [label for label in load_labels(args.labels) if label.split == args.split]
    qrels = qrels_for_split(labels, args.split)
    chunks = chunk_papers(
        papers,
        chunk_size=args.chunk_size,
        overlap=proportional_overlap(args.chunk_size),
    )
    chunk_by_id = {chunk.chunk_id: chunk for chunk in chunks}

    encoder = SentenceTransformerEncoder(DEFAULT_EMBEDDING_MODELS.get(args.model, args.model))
    chunk_vectors, embed_seconds = encoder.encode_documents([chunk.text for chunk in chunks])
    query_vectors, query_seconds = encoder.encode_queries([label.query for label in labels])
    ranked_chunks = rank_chunks(
        query_vectors=query_vectors,
        chunk_vectors=chunk_vectors,
        chunks=chunks,
        top_k_chunks=args.top_k_chunks,
    )
    baseline_runs = build_runs(labels, ranked_chunks, top_k_papers=args.top_k_papers)
    baseline_metrics = evaluate_retrieval(qrels, baseline_runs)
    print("baseline", baseline_metrics)

    reranker = CrossEncoderReranker(args.reranker)
    reranked_runs: dict[str, list[str]] = {}
    rerank_seconds_total = 0.0
    for query_index, label in enumerate(labels):
        candidates = [(chunk.chunk_id, chunk.text) for chunk in ranked_chunks[query_index]]
        ranked_chunk_ids, rerank_seconds = reranker.rerank(label.query, candidates)
        rerank_seconds_total += rerank_seconds
        reranked_runs[label.query_id] = collapse_reranked_chunk_ids(
            ranked_chunk_ids,
            chunk_by_id=chunk_by_id,
            top_k_papers=args.top_k_papers,
        )

    reranked_metrics = evaluate_retrieval(qrels, reranked_runs)
    reranked_metrics.update(
        {
            "embedding_seconds_total": embed_seconds,
            "query_embedding_seconds_total": query_seconds,
            "rerank_seconds_total": rerank_seconds_total,
            "rerank_seconds_per_query": rerank_seconds_total / max(len(labels), 1),
        }
    )
    print("reranked", reranked_metrics)

    if args.wandb:
        _log_wandb(
            run_name=f"reranking-{args.split}",
            config={
                "stage": "reranking_experiment",
                "dataset_snapshot": args.corpus,
                "labels": args.labels,
                "split": args.split,
                "embedding_model": args.model,
                "chunk_size": args.chunk_size,
                "overlap": proportional_overlap(args.chunk_size),
                "reranker": args.reranker,
            },
            baseline_metrics={f"baseline_{key}": value for key, value in baseline_metrics.items()},
            reranked_metrics={f"reranked_{key}": value for key, value in reranked_metrics.items()},
        )


def _log_wandb(
    run_name: str,
    config: dict[str, object],
    baseline_metrics: dict[str, float],
    reranked_metrics: dict[str, float],
) -> None:
    import wandb

    run = wandb.init(project="arxiv-rag", name=run_name, config=config)
    run.log({**baseline_metrics, **reranked_metrics})
    run.finish()


if __name__ == "__main__":
    main()
