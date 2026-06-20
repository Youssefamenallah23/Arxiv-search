from __future__ import annotations

from unittest import TestCase
from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient


def _make_mock_pipeline() -> MagicMock:
    p = MagicMock()
    p.papers = [MagicMock() for _ in range(5000)]
    p.chunk_vectors = None
    p.use_qdrant = True
    p.query.return_value = {
        "answer": "Based on the provided abstracts, attention mechanisms in transformers enable models to dynamically weigh the importance of different parts of the input sequence.",
        "citations": ["2606.09951v1", "2606.17830v1"],
        "evidence": [
            {"paper_id": "2606.09951v1", "title": "Hasse Diagrams for Attention", "text": "..."},
            {
                "paper_id": "2606.17830v1",
                "title": "Functional Equivalence in Attention",
                "text": "...",
            },
        ],
        "latency": {"retrieval": 0.025, "rerank": 10.367, "generation": 3.135, "total": 13.527},
        "usage": {"prompt_tokens": 899, "completion_tokens": 215, "total_tokens": 1114},
    }
    return p


class ApiHealthTest(TestCase):
    def test_health_returns_ok(self) -> None:
        with patch("arxiv_rag.api.RAGPipeline") as mock_cls:
            mock_cls.return_value = _make_mock_pipeline()
            from arxiv_rag.api import app

            with TestClient(app) as client:
                resp = client.get("/health")
                self.assertEqual(resp.status_code, 200)
                body = resp.json()
                self.assertEqual(body["status"], "ok")
                self.assertIn("corpus_size", body)
                self.assertIn("index_loaded", body)
                self.assertIn("mode", body)

    def test_health_reports_correct_mode(self) -> None:
        with patch("arxiv_rag.api.RAGPipeline") as mock_cls:
            mock_cls.return_value = _make_mock_pipeline()
            from arxiv_rag.api import app

            with TestClient(app) as client:
                body = client.get("/health").json()
                self.assertEqual(body["mode"], "qdrant")


class ApiQueryValidationTest(TestCase):
    def setUp(self) -> None:
        patcher = patch("arxiv_rag.api.RAGPipeline")
        self.mock_cls = patcher.start()
        self.mock_cls.return_value = _make_mock_pipeline()
        from arxiv_rag.api import app

        self.client = TestClient(app)
        self.addCleanup(patcher.stop)

    def test_query_empty_body_returns_422(self) -> None:
        resp = self.client.post("/query", json={})
        self.assertEqual(resp.status_code, 422)

    def test_query_missing_query_returns_422(self) -> None:
        resp = self.client.post("/query", json={"top_k": 10})
        self.assertEqual(resp.status_code, 422)

    def test_query_empty_string_returns_422(self) -> None:
        resp = self.client.post("/query", json={"query": ""})
        self.assertEqual(resp.status_code, 422)

    def test_query_negative_top_k_returns_422(self) -> None:
        resp = self.client.post("/query", json={"query": "test", "top_k": -1})
        self.assertEqual(resp.status_code, 422)

    def test_query_too_large_context_budget_returns_422(self) -> None:
        resp = self.client.post("/query", json={"query": "test", "context_budget": 100})
        self.assertEqual(resp.status_code, 422)

    def test_valid_query_returns_200(self) -> None:
        resp = self.client.post("/query", json={"query": "attention mechanisms"})
        self.assertEqual(resp.status_code, 200)

    def test_valid_query_with_all_params(self) -> None:
        resp = self.client.post(
            "/query",
            json={
                "query": "attention mechanisms in transformers",
                "top_k": 30,
                "context_budget": 3,
            },
        )
        self.assertEqual(resp.status_code, 200)


class ApiQueryResponseShapeTest(TestCase):
    def setUp(self) -> None:
        patcher = patch("arxiv_rag.api.RAGPipeline")
        self.mock_cls = patcher.start()
        self.mock_cls.return_value = _make_mock_pipeline()
        from arxiv_rag.api import app

        self.client = TestClient(app)
        self.addCleanup(patcher.stop)

    def test_response_has_all_fields(self) -> None:
        resp = self.client.post("/query", json={"query": "attention mechanisms"})
        body = resp.json()
        self.assertIn("query", body)
        self.assertIn("answer", body)
        self.assertIn("citations", body)
        self.assertIn("evidence", body)
        self.assertIn("latency", body)
        self.assertIn("usage", body)

    def test_response_latency_has_all_stages(self) -> None:
        resp = self.client.post("/query", json={"query": "attention mechanisms"})
        lat = resp.json()["latency"]
        self.assertIn("retrieval", lat)
        self.assertIn("rerank", lat)
        self.assertIn("generation", lat)
        self.assertIn("total", lat)

    def test_response_usage_has_token_counts(self) -> None:
        resp = self.client.post("/query", json={"query": "attention mechanisms"})
        usage = resp.json()["usage"]
        self.assertIn("prompt_tokens", usage)
        self.assertIn("completion_tokens", usage)
        self.assertIn("total_tokens", usage)

    def test_citations_is_list_of_strings(self) -> None:
        resp = self.client.post("/query", json={"query": "attention mechanisms"})
        citations = resp.json()["citations"]
        self.assertIsInstance(citations, list)
        if citations:
            self.assertIsInstance(citations[0], str)

    def test_evidence_items_have_required_fields(self) -> None:
        resp = self.client.post("/query", json={"query": "attention mechanisms"})
        evidence = resp.json()["evidence"]
        self.assertIsInstance(evidence, list)
        for item in evidence:
            self.assertIn("paper_id", item)
            self.assertIn("title", item)
            self.assertIn("text", item)
