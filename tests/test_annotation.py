from __future__ import annotations

import unittest

from arxiv_rag.annotation import next_query_id
from arxiv_rag.schema import QueryLabel


class AnnotationTest(unittest.TestCase):
    def test_next_query_id(self) -> None:
        labels = [
            QueryLabel(
                query_id="train-001",
                split="train",
                query="question",
                relevant_paper_ids=["p1"],
            ),
            QueryLabel(
                query_id="validation-007",
                split="validation",
                query="question",
                relevant_paper_ids=["p2"],
            ),
        ]

        self.assertEqual(next_query_id(labels, "train"), "train-002")
        self.assertEqual(next_query_id(labels, "validation"), "validation-008")
        self.assertEqual(next_query_id(labels, "test"), "test-001")


if __name__ == "__main__":
    unittest.main()
