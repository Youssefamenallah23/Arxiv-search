from __future__ import annotations

import unittest

from arxiv_rag.metrics import (
    bootstrap_interval,
    evaluate_retrieval,
    ndcg_at_k,
    recall_at_k,
    reciprocal_rank,
)


class MetricsTest(unittest.TestCase):
    def test_recall_at_k(self) -> None:
        self.assertEqual(recall_at_k({"a", "b"}, ["a", "x", "b"], 1), 0.5)
        self.assertEqual(recall_at_k({"a", "b"}, ["a", "x", "b"], 3), 1.0)

    def test_reciprocal_rank(self) -> None:
        self.assertEqual(reciprocal_rank({"a"}, ["x", "a"]), 0.5)
        self.assertEqual(reciprocal_rank({"a"}, ["x", "y"]), 0.0)

    def test_ndcg_at_k(self) -> None:
        self.assertAlmostEqual(ndcg_at_k({"a"}, ["a"], 10), 1.0)
        self.assertLess(ndcg_at_k({"a"}, ["x", "a"], 10), 1.0)

    def test_evaluate_retrieval(self) -> None:
        metrics = evaluate_retrieval(
            qrels={"q1": {"a"}, "q2": {"b"}},
            runs={"q1": ["a"], "q2": ["x", "b"]},
        )
        self.assertEqual(metrics["recall@5"], 1.0)
        self.assertEqual(metrics["recall@10"], 1.0)
        self.assertEqual(metrics["mrr"], 0.75)

    def test_bootstrap_interval(self) -> None:
        lower, upper = bootstrap_interval([1, 2, 3], lambda rows: sum(rows) / len(rows), 50)
        self.assertLessEqual(lower, upper)


if __name__ == "__main__":
    unittest.main()
