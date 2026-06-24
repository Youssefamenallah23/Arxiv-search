from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.adaptive import AdaptiveRetriever
from arxiv_rag.chunking import chunk_papers, proportional_overlap
from arxiv_rag.embeddings import SentenceTransformerEncoder
from arxiv_rag.labels import load_labels, load_papers, qrels_for_split
from arxiv_rag.metrics import evaluate_retrieval
from arxiv_rag.retrieval import (
    HybridRetriever,
    build_runs,
    paper_run_from_chunks,
)
from arxiv_rag.schema import Chunk

ALL_MODES = ["dense", "hybrid", "adaptive_dense", "adaptive_hybrid"]


def _dense_retrieve(
    query: str,
    encoder: SentenceTransformerEncoder,
    chunk_vectors: np.ndarray,
    chunks: list[Chunk],
    top_k: int,
) -> list[Chunk]:
    qv, _ = encoder.encode_queries([query])
    scores = qv @ chunk_vectors.T
    idx = scores[0].argsort()[::-1][:top_k]
    return [chunks[i] for i in idx]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare dense vs hybrid vs adaptive retrieval modes."
    )
    parser.add_argument("--corpus", default="data/raw/arxiv_corpus_2026-06-19.jsonl")
    parser.add_argument("--labels", default="docs/eval/query_labels_2026-06-19.jsonl")
    parser.add_argument("--split", choices=["train", "validation"], default="validation")
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--top-k-chunks", type=int, default=50)
    parser.add_argument("--top-k-papers", type=int, default=10)
    parser.add_argument("--wandb", action="store_true")
    parser.add_argument(
        "--mode",
        choices=ALL_MODES,
        action="append",
        help="Mode(s) to run (can be repeated, default: all)",
    )
    parser.add_argument("--delay", type=float, default=0, help="Seconds to sleep between queries")
    args = parser.parse_args()

    modes = args.mode or ALL_MODES

    papers = load_papers(args.corpus)
    labels = [label for label in load_labels(args.labels) if label.split == args.split]
    qrels = qrels_for_split(labels, args.split)
    chunks = chunk_papers(
        papers, chunk_size=args.chunk_size, overlap=proportional_overlap(args.chunk_size)
    )
    chunk_by_id = {c.chunk_id: c for c in chunks}
    query_texts = [label.query for label in labels]
    n_queries = len(query_texts)
    print(f"Running {len(modes)} mode(s) on {n_queries} queries ({args.split} split)")

    encoder = SentenceTransformerEncoder("BAAI/bge-small-en-v1.5")
    chunk_vectors, embed_sec = encoder.encode_documents([c.text for c in chunks])
    print(f"Encoded {len(chunks)} chunks in {embed_sec:.1f}s\n")

    hybrid_retriever = HybridRetriever(chunks, encoder, chunk_vectors)

    results_by_mode: dict[str, dict] = {}

    for mode in modes:
        print(f"=== Mode: {mode} ===")
        all_runs: dict[str, list[str]] = {}
        latencies: list[float] = []
        adaptive_stats = {"n_reformulated": 0, "reformulations": []}

        for label in labels:
            t0 = time.perf_counter()

            if mode == "dense":
                ranked = _dense_retrieve(
                    label.query, encoder, chunk_vectors, chunks, args.top_k_chunks
                )

            elif mode == "hybrid":
                ranked = hybrid_retriever.retrieve(label.query, args.top_k_chunks)

            elif mode == "adaptive_dense":
                base = object()
                attr_retriever = AdaptiveRetriever(base, chunks)
                attr_retriever._retrieve_core = lambda q, k: _dense_retrieve(  # type: ignore[method-assign]
                    q, encoder, chunk_vectors, chunks, k
                )
                ranked, meta = attr_retriever.retrieve(label.query, args.top_k_chunks)
                if meta["reformulated"]:
                    adaptive_stats["n_reformulated"] += 1
                    adaptive_stats["reformulations"].append(
                        {
                            "query_id": label.query_id,
                            "original": meta["original_query"],
                            "reformulated": meta["reformulated_query"],
                        }
                    )

            elif mode == "adaptive_hybrid":
                attr_retriever = AdaptiveRetriever(hybrid_retriever, chunks)
                ranked, meta = attr_retriever.retrieve(label.query, args.top_k_chunks)
                if meta["reformulated"]:
                    adaptive_stats["n_reformulated"] += 1
                    adaptive_stats["reformulations"].append(
                        {
                            "query_id": label.query_id,
                            "original": meta["original_query"],
                            "reformulated": meta["reformulated_query"],
                        }
                    )

            latency = time.perf_counter() - t0
            latencies.append(latency)

            all_runs[label.query_id] = paper_run_from_chunks(ranked, args.top_k_papers)

            if args.delay:
                time.sleep(args.delay)

        metrics = evaluate_retrieval(qrels, all_runs, k_values=(1, 5, 10))
        metrics["latency_mean"] = sum(latencies) / len(latencies)
        metrics["latency_median"] = sorted(latencies)[len(latencies) // 2]
        if adaptive_stats["n_reformulated"] > 0:
            reformulated = adaptive_stats["reformulations"]
            metrics["n_reformulated"] = adaptive_stats["n_reformulated"]
            metrics["pct_reformulated"] = adaptive_stats["n_reformulated"] / n_queries

        results_by_mode[mode] = {"metrics": metrics, "latencies": latencies}
        if mode.startswith("adaptive"):
            results_by_mode[mode]["adaptive_stats"] = adaptive_stats

        print(
            f"  recall@1={metrics['recall@1']:.3f} recall@5={metrics['recall@5']:.3f} recall@10={metrics['recall@10']:.3f}"
        )
        print(f"  MRR={metrics['mrr']:.3f} NDCG@10={metrics['ndcg@10']:.3f}")
        print(
            f"  latency: mean={metrics['latency_mean']:.3f}s median={metrics['latency_median']:.3f}s"
        )
        if metrics.get("n_reformulated"):
            print(
                f"  reformulated: {metrics['n_reformulated']}/{n_queries} ({metrics['pct_reformulated'] * 100:.0f}%)"
            )
            for r in adaptive_stats["reformulations"]:
                print(f"    {r['query_id']}: '{r['original']}' -> '{r['reformulated']}'")
        print()

    # Summary table
    header = f"{'Mode':<20} | {'R@1':>5} | {'R@5':>5} | {'R@10':>5} | {'MRR':>5} | {'NDCG@10':>7} | {'Lat(mean)':>9} | {'Reform%':>7}"
    sep = "-" * len(header)
    print("=" * len(header))
    print("RETRIEVAL COMPARISON SUMMARY")
    print("=" * len(header))
    print(header)
    print(sep)
    for mode in modes:
        m = results_by_mode[mode]["metrics"]
        reform_pct = f"{m.get('pct_reformulated', 0) * 100:.0f}%"
        print(
            f"{mode:<20} | {m['recall@1']:>5.3f} | {m['recall@5']:>5.3f} | {m['recall@10']:>5.3f} | "
            f"{m['mrr']:>5.3f} | {m['ndcg@10']:>7.4f} | {m['latency_mean']:>9.3f}s | {reform_pct:>7}"
        )
    print(sep)
    print()

    # Best mode
    best = max(modes, key=lambda m: results_by_mode[m]["metrics"]["mrr"])
    print(f"Best mode by MRR: {best}")
    if "dense" in results_by_mode:
        print(
            f"MRR improvement over dense: {results_by_mode[best]['metrics']['mrr'] - results_by_mode['dense']['metrics']['mrr']:.4f}"
        )

    if args.wandb:
        import wandb

        run = wandb.init(project="arxiv-rag", name=f"retrieval-comparison-{args.split}")
        for mode in modes:
            run.log({f"{mode}/{k}": v for k, v in results_by_mode[mode]["metrics"].items()})
        run.finish()
        print(f"W&B: https://wandb.ai/ahmedmohmohsen8881-momo/arxiv-rag")


if __name__ == "__main__":
    main()
