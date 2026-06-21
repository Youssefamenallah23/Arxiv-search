from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.chunking import chunk_papers, proportional_overlap
from arxiv_rag.config import DEFAULT_EMBEDDING_MODELS
from arxiv_rag.embeddings import CrossEncoderReranker, SentenceTransformerEncoder
from arxiv_rag.generation import generate_answer
from arxiv_rag.labels import load_papers


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask a question about arXiv AI/ML papers.")
    parser.add_argument("query", nargs="+", help="Your research question")
    parser.add_argument("--corpus", default="data/raw/arxiv_corpus_2026-06-19.jsonl")
    parser.add_argument("--model", default="bge-small")
    parser.add_argument("--reranker", default="BAAI/bge-reranker-base")
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--top-k-chunks", type=int, default=50)
    parser.add_argument("--top-k-papers", type=int, default=10)
    parser.add_argument("--context-budget", type=int, default=5)
    parser.add_argument("--llm-model", default="gemini-3.1-flash-lite")
    parser.add_argument("--no-rerank", action="store_true", help="Skip reranking step")
    parser.add_argument("--show-evidence", action="store_true", help="Show retrieved abstracts")
    args = parser.parse_args()

    query = " ".join(args.query)
    corpus_path = Path(args.corpus)
    if not corpus_path.exists():
        print(f"Corpus not found: {corpus_path}")
        sys.exit(1)

    print(f"Loading corpus ({corpus_path})...", end=" ", flush=True)
    papers = load_papers(str(corpus_path))
    print(f"{len(papers)} papers")

    print("Chunking...", end=" ", flush=True)
    overlap = proportional_overlap(args.chunk_size)
    chunks = chunk_papers(papers, chunk_size=args.chunk_size, overlap=overlap)
    chunk_by_id = {chunk.chunk_id: chunk for chunk in chunks}
    print(f"{len(chunks)} chunks")

    print("Encoding with embeddings...", end=" ", flush=True)
    encoder = SentenceTransformerEncoder(DEFAULT_EMBEDDING_MODELS.get(args.model, args.model))
    chunk_vectors, embed_seconds = encoder.encode_documents([chunk.text for chunk in chunks])
    query_vector, _ = encoder.encode_queries([query])
    print(f"done ({embed_seconds:.1f}s)")

    scores = query_vector @ chunk_vectors.T
    top_indices = scores[0].argsort()[::-1][: args.top_k_chunks]
    ranked_chunks = [chunks[i] for i in top_indices]

    if not args.no_rerank:
        print("Reranking...", end=" ", flush=True)
        reranker = CrossEncoderReranker(args.reranker)
        candidates = [(chunk.chunk_id, chunk.text) for chunk in ranked_chunks]
        ranked_chunk_ids, rerank_seconds = reranker.rerank(query, candidates)
        ranked_chunks = [chunk_by_id[cid] for cid in ranked_chunk_ids]
        print(f"done ({rerank_seconds:.1f}s)")

    budget_chunks = ranked_chunks[: args.context_budget]
    chunk_dicts = [
        {
            "chunk_id": c.chunk_id,
            "paper_id": c.paper_id,
            "title": c.title,
            "text": c.text,
        }
        for c in budget_chunks
    ]

    if args.show_evidence:
        print(f"\n--- Evidence (top {args.context_budget} chunks) ---")
        for c in chunk_dicts:
            print(f"\n[{c['paper_id']}] {c['title']}")
            print(f"  {c['text'][:300]}...")

    print("\nGenerating answer...", end=" ", flush=True)
    t0 = time.perf_counter()
    answer, gen_seconds, usage = generate_answer(
        query=query, chunks=chunk_dicts, model_name=args.llm_model
    )
    elapsed = time.perf_counter() - t0
    print(f"{elapsed:.1f}s")

    print(f"\n{'=' * 60}")
    print(f"Q: {query}")
    print(f"{'=' * 60}")
    print(answer)
    print(f"{'=' * 60}")
    if usage:
        tokens = usage.get("total_tokens", 0)
        print(f"Tokens: {tokens} | Generation: {gen_seconds:.1f}s | Total: {elapsed:.1f}s")
    else:
        print(f"Generation: {gen_seconds:.1f}s | Total: {elapsed:.1f}s")

    print(f"\nCited papers: {len([c for c in budget_chunks if c['paper_id'] in answer])}")
    shown = set()
    for c in budget_chunks:
        pid = c["paper_id"]
        if pid in answer and pid not in shown:
            print(f"  [{pid}] {c['title']}")
            shown.add(pid)


if __name__ == "__main__":
    main()
