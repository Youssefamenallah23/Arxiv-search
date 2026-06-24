from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.config import Settings


def main() -> None:
    settings = Settings()
    eval_path = Path("data/results/eval_test_generation.jsonl")
    if not eval_path.exists():
        print(f"Eval data not found: {eval_path}")
        sys.exit(1)

    rows = [json.loads(line) for line in eval_path.open()]

    retrieval_metrics = {
        "recall@5": sum(r["retrieval"]["recall@5"] for r in rows) / len(rows),
        "recall@10": sum(r["retrieval"]["recall@10"] for r in rows) / len(rows),
        "mrr": sum(r["retrieval"]["mrr"] for r in rows) / len(rows),
        "ndcg@10": sum(r["retrieval"]["ndcg@10"] for r in rows) / len(rows),
    }

    gen_metrics = {
        "faithfulness": sum(r["generation"]["faithfulness"] for r in rows) / len(rows),
        "citation_accuracy": sum(r["generation"]["citation_accuracy"] for r in rows) / len(rows),
        "completeness": sum(r["generation"]["completeness"] for r in rows) / len(rows),
        "avg_latency_seconds": sum(r["generation"]["latency_seconds"] for r in rows) / len(rows),
        "total_tokens": sum(r["generation"]["llm_usage"]["total_tokens"] for r in rows),
    }

    import wandb

    run = wandb.init(
        project=settings.wandb_project,
        name="final-eval-test-set",
        config={
            "stage": "final_evaluation",
            "dataset_snapshot": "arxiv_corpus_2026-06-19",
            "labels": "query_labels_2026-06-19",
            "split": "test",
            "embedding_model": "BAAI/bge-small-en-v1.5",
            "reranker_model": "BAAI/bge-reranker-base",
            "llm_model": "gemini-3.1-flash-lite",
            "chunk_size": 512,
        },
    )

    run.log({"retrieval": retrieval_metrics})
    run.log({"generation": gen_metrics})

    for _i, r in enumerate(rows):
        run.log(
            {
                f"query/{r['query_id']}/recall@5": r["retrieval"]["recall@5"],
                f"query/{r['query_id']}/recall@10": r["retrieval"]["recall@10"],
                f"query/{r['query_id']}/mrr": r["retrieval"]["mrr"],
                f"query/{r['query_id']}/ndcg@10": r["retrieval"]["ndcg@10"],
                f"query/{r['query_id']}/faithfulness": r["generation"]["faithfulness"],
                f"query/{r['query_id']}/citation_accuracy": r["generation"]["citation_accuracy"],
                f"query/{r['query_id']}/completeness": r["generation"]["completeness"],
                f"query/{r['query_id']}/latency": r["generation"]["latency_seconds"],
                f"query/{r['query_id']}/tokens": r["generation"]["llm_usage"]["total_tokens"],
            }
        )

    run.finish()

    print(f"Logged {len(rows)} queries to W&B project '{settings.wandb_project}'")
    print(f"Retrieval: {retrieval_metrics}")
    print(f"Generation: {gen_metrics}")
    print(f"View at: https://wandb.ai/{run.entity}/{settings.wandb_project}")


if __name__ == "__main__":
    main()
