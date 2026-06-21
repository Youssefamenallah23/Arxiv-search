from __future__ import annotations

from unittest import TestCase
from unittest.mock import patch

from arxiv_rag.serving import RAGPipeline, _extract_citations


class ExtractCitationsTest(TestCase):
    def test_single_citation(self) -> None:
        self.assertEqual(_extract_citations("See [2606.12345v1]"), ["2606.12345v1"])

    def test_multiple_citations(self) -> None:
        self.assertEqual(
            _extract_citations("See [2606.12345v1] and [2606.67890v2]"),
            ["2606.12345v1", "2606.67890v2"],
        )

    def test_comma_separated(self) -> None:
        self.assertEqual(
            _extract_citations("See [2606.12345v1, 2606.67890v2]"),
            ["2606.12345v1", "2606.67890v2"],
        )

    def test_no_citations(self) -> None:
        self.assertEqual(_extract_citations("No citations here"), [])

    def test_arxiv_id_in_text_not_bracket(self) -> None:
        self.assertEqual(_extract_citations("Paper 2606.12345v1 is good"), [])

    def test_deduplicates(self) -> None:
        self.assertEqual(
            _extract_citations("[2606.12345v1] and [2606.12345v1] again"),
            ["2606.12345v1"],
        )

    def test_empty_string(self) -> None:
        self.assertEqual(_extract_citations(""), [])


class PipelineQueryShapeTest(TestCase):
    def test_query_return_keys(self) -> None:
        with (
            patch("arxiv_rag.serving.load_papers", return_value=[]),
            patch("arxiv_rag.serving.chunk_papers", return_value=[]),
            patch("arxiv_rag.serving.SentenceTransformerEncoder"),
            patch("arxiv_rag.serving.CrossEncoderReranker"),
            patch("arxiv_rag.serving.QdrantSearcher"),
        ):
            pipeline = RAGPipeline(
                corpus_path="data/raw/arxiv_corpus_2026-06-19.jsonl",
                use_qdrant=True,
            )

            pipeline.chunk_by_id = {}
            pipeline.qdrant_searcher.search.return_value = []
            pipeline.query = lambda **kw: {
                "answer": "test",
                "citations": [],
                "evidence": [],
                "latency": {"retrieval": 0.0, "rerank": 0.0, "generation": 0.0, "total": 0.0},
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
            }

            result = pipeline.query(query="test", top_k=10, context_budget=3)
            self.assertIn("answer", result)
            self.assertIn("citations", result)
            self.assertIn("evidence", result)
            self.assertIn("latency", result)
            self.assertIn("usage", result)
            self.assertIn("retrieval", result["latency"])
            self.assertIn("rerank", result["latency"])
            self.assertIn("generation", result["latency"])
            self.assertIn("total", result["latency"])
