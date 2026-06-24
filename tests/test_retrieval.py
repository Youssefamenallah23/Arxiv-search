from __future__ import annotations

import numpy as np
import pytest

from arxiv_rag.embeddings import SentenceTransformerEncoder
from arxiv_rag.retrieval import (
    BM25Retriever,
    HybridRetriever,
    hybrid_fusion,
)
from arxiv_rag.schema import Chunk


def _chunk(text: str, paper_id: str = "9999.00001v1") -> Chunk:
    return Chunk(
        chunk_id=f"{paper_id}::chunk-0000",
        paper_id=paper_id,
        title="Test Title",
        text=text,
        categories=["cs.AI"],
        chunk_index=0,
        token_start=0,
        token_end=len(text.split()),
    )


TEXTS = [
    "machine learning transformers for natural language processing",
    "reinforcement learning for robot control and manipulation",
    "diffusion models for image generation and computer vision",
    "graph neural networks for molecular property prediction",
    "attention mechanisms in large language models",
]


@pytest.fixture
def chunks() -> list[Chunk]:
    return [_chunk(t, f"9999.{i + 1:05d}v1") for i, t in enumerate(TEXTS)]


class TestBM25Retriever:
    def test_exact_match_top_result(self, chunks: list[Chunk]):
        retriever = BM25Retriever(chunks)
        results = retriever.retrieve("machine learning transformers", 3)
        assert len(results) == 3
        assert results[0].text == TEXTS[0]

    def test_relevant_chunk_in_results(self, chunks: list[Chunk]):
        retriever = BM25Retriever(chunks)
        results = retriever.retrieve("molecular property prediction", 3)
        ids = [c.text for c in results]
        assert TEXTS[3] in ids

    def test_empty_query_returns_some_results(self, chunks: list[Chunk]):
        retriever = BM25Retriever(chunks)
        results = retriever.retrieve("", 3)
        assert len(results) == 3


class TestHybridFusion:
    def test_fusion_interleaves_results(self, chunks: list[Chunk]):
        dense = list(reversed(chunks))
        bm25 = chunks
        merged = hybrid_fusion(dense, bm25, 5)
        dense_ids = {c.chunk_id for c in dense}
        bm25_ids = {c.chunk_id for c in bm25}
        assert any(c.chunk_id in dense_ids for c in merged)
        assert any(c.chunk_id in bm25_ids for c in merged)
        assert len(merged) == 5

    def test_fusion_respects_top_k(self, chunks: list[Chunk]):
        merged = hybrid_fusion(chunks[:3], chunks[3:], 2)
        assert len(merged) == 2

    def test_fusion_deduplicates(self, chunks: list[Chunk]):
        merged = hybrid_fusion(chunks[:3], chunks[:3], 5)
        assert len(merged) == 3


class TestHybridRetriever:
    @pytest.fixture
    def retriever(self, chunks: list[Chunk]):
        encoder = SentenceTransformerEncoder("BAAI/bge-small-en-v1.5")
        chunk_vectors, _ = encoder.encode_documents([c.text for c in chunks])
        return HybridRetriever(chunks, encoder, chunk_vectors)

    def test_returns_correct_number(self, retriever: HybridRetriever):
        results = retriever.retrieve("machine learning", 3)
        assert len(results) == 3

    def test_contains_dense_and_bm25(self, retriever: HybridRetriever):
        results = retriever.retrieve("reinforcement learning robot", 5)
        assert len(results) == 5
        texts = [c.text for c in results]
        assert any("reinforcement" in t for t in texts)

    def test_works_with_short_query(self, retriever: HybridRetriever):
        results = retriever.retrieve("graph", 2)
        assert len(results) == 2
