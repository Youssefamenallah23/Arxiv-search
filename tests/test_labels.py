from __future__ import annotations

import unittest

from arxiv_rag.labels import validate_labels
from arxiv_rag.schema import Paper, QueryLabel


class LabelsTest(unittest.TestCase):
    def test_validate_missing_relevant_id(self) -> None:
        papers = [
            Paper(
                paper_id="p1",
                arxiv_url="https://arxiv.org/abs/p1",
                title="Paper",
                abstract="Abstract",
                categories=["cs.AI"],
                authors=["A"],
                published="2026-01-01T00:00:00Z",
            )
        ]
        labels = [
            QueryLabel(
                query_id="q1",
                split="train",
                query="question",
                relevant_paper_ids=["missing"],
            )
        ]
        errors = validate_labels(labels, papers)
        self.assertTrue(any("missing" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
