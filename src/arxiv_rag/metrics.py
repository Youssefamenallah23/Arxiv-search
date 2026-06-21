from __future__ import annotations

import math
import random
from collections.abc import Callable, Sequence

Run = Sequence[str]


def recall_at_k(relevant: set[str], retrieved: Run, k: int) -> float:
    if not relevant:
        return 0.0
    return len(relevant.intersection(retrieved[:k])) / len(relevant)


def reciprocal_rank(relevant: set[str], retrieved: Run) -> float:
    for index, paper_id in enumerate(retrieved, start=1):
        if paper_id in relevant:
            return 1.0 / index
    return 0.0


def ndcg_at_k(relevant: set[str], retrieved: Run, k: int) -> float:
    dcg = 0.0
    for index, paper_id in enumerate(retrieved[:k], start=1):
        if paper_id in relevant:
            dcg += 1.0 / math.log2(index + 1)

    ideal_hits = min(len(relevant), k)
    if ideal_hits == 0:
        return 0.0
    idcg = sum(1.0 / math.log2(index + 1) for index in range(1, ideal_hits + 1))
    return dcg / idcg


def evaluate_retrieval(
    qrels: dict[str, set[str]],
    runs: dict[str, Run],
    k_values: Sequence[int] = (5, 10),
) -> dict[str, float]:
    if not qrels:
        raise ValueError("qrels cannot be empty")

    metrics: dict[str, list[float]] = {f"recall@{k}": [] for k in k_values}
    metrics["mrr"] = []
    metrics["ndcg@10"] = []

    for query_id, relevant in qrels.items():
        retrieved = runs.get(query_id, [])
        for k in k_values:
            metrics[f"recall@{k}"].append(recall_at_k(relevant, retrieved, k))
        metrics["mrr"].append(reciprocal_rank(relevant, retrieved))
        metrics["ndcg@10"].append(ndcg_at_k(relevant, retrieved, 10))

    return {name: _mean(values) for name, values in metrics.items()}


def bootstrap_interval(
    rows: Sequence[object],
    scorer: Callable[[Sequence[object]], float],
    iterations: int = 1000,
    confidence: float = 0.90,
    seed: int = 13,
) -> tuple[float, float]:
    if not rows:
        raise ValueError("rows cannot be empty")
    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1")

    rng = random.Random(seed)
    scores: list[float] = []
    for _ in range(iterations):
        sample = [rows[rng.randrange(len(rows))] for _ in range(len(rows))]
        scores.append(scorer(sample))
    scores.sort()

    alpha = 1 - confidence
    lower_index = int((alpha / 2) * len(scores))
    upper_index = min(len(scores) - 1, int((1 - alpha / 2) * len(scores)))
    return scores[lower_index], scores[upper_index]


def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0
