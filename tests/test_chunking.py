from __future__ import annotations

import unittest

from arxiv_rag.chunking import chunk_paper, proportional_overlap
from arxiv_rag.schema import Paper


class ChunkingTest(unittest.TestCase):
    def test_chunk_paper_with_overlap(self) -> None:
        paper = Paper(
            paper_id="1234.5678",
            arxiv_url="https://arxiv.org/abs/1234.5678",
            title="Test",
            abstract="one two three four five six seven eight",
            categories=["cs.AI"],
            authors=["A"],
            published="2026-01-01T00:00:00Z",
        )
        chunks = chunk_paper(paper, chunk_size=5, overlap=2)
        self.assertEqual(len(chunks), 3)
        self.assertEqual(chunks[0].token_start, 0)
        self.assertEqual(chunks[1].token_start, 3)
        self.assertEqual(chunks[-1].paper_id, "1234.5678")

    def test_proportional_overlap(self) -> None:
        self.assertEqual(proportional_overlap(512), 77)


if __name__ == "__main__":
    unittest.main()
