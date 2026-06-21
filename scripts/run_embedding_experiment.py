from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.chunking import chunk_papers, proportional_overlap
from arxiv_rag.config import DEFAULT_EMBEDDING_MODELS
from arxiv_rag.embeddings import SentenceTransformerEncoder
from arxiv_rag.labels import load_labels, load_papers, qrels_for_split
from arxiv_rag.metrics import evaluate_retrieval
from arxiv_rag.retrieval import build_runs, rank_chunks


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare embedding models at fixed chunk size.")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--labels", required=True)
    parser.add_argument("--split", choices=["train", "validation"], default="validation")
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--top-k-chunks", type=int, default=50)
    parser.add_argument("--top-k-papers", type=int, default=10)
    parser.add_argument("--models", nargs="+", default=list(DEFAULT_EMBEDDING_MODELS.keys()))
    parser.add_argument("--wandb", action="store_true")
    args = parser.parse_args()

    papers = load_papers(args.corpus)
    labels = [label for label in load_labels(args.labels) if label.split == args.split]
    qrels = qrels_for_split(labels, args.split)
    chunks = chunk_papers(
        papers,
        chunk_size=args.chunk_size,
        overlap=proportional_overlap(args.chunk_size, 0.0),
    )
    chunk_texts = [chunk.text for chunk in chunks]
    query_texts = [label.query for label in labels]

    for model_key in args.models:
        model_name = DEFAULT_EMBEDDING_MODELS.get(model_key, model_key)
        encoder = SentenceTransformerEncoder(model_name)
        chunk_vectors, embed_seconds = encoder.encode_documents(chunk_texts)
        query_vectors, query_seconds = encoder.encode_queries(query_texts)
        ranked_chunks = rank_chunks(
            query_vectors=query_vectors,
            chunk_vectors=chunk_vectors,
            chunks=chunks,
            top_k_chunks=args.top_k_chunks,
        )
        runs = build_runs(labels, ranked_chunks, top_k_papers=args.top_k_papers)
        metrics = evaluate_retrieval(qrels, runs)
        metrics.update(
            {
                "embedding_seconds_total": embed_seconds,
                "query_embedding_seconds_total": query_seconds,
                "embedding_seconds_per_chunk": embed_seconds / max(len(chunks), 1),
                "index_storage_mb_estimate": chunk_vectors.nbytes / (1024 * 1024),
            }
        )
        print(model_key, metrics)
        if args.wandb:
            _log_wandb(
                run_name=f"embedding-{model_key}-{args.split}",
                config={
                    "stage": "embedding_experiment",
                    "dataset_snapshot": args.corpus,
                    "labels": args.labels,
                    "split": args.split,
                    "embedding_model": model_name,
                    "chunk_size": args.chunk_size,
                    "overlap": 0,
                    "reranker": False,
                },
                metrics=metrics,
            )


def _log_wandb(run_name: str, config: dict[str, object], metrics: dict[str, float]) -> None:
    import wandb

    run = wandb.init(project="arxiv-rag", name=run_name, config=config)
    run.log(metrics)
    run.finish()


if __name__ == "__main__":
    main()
