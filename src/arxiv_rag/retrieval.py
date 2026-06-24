from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from rank_bm25 import BM25Okapi

from arxiv_rag.config import Settings
from arxiv_rag.embeddings import SentenceTransformerEncoder
from arxiv_rag.schema import Chunk, QueryLabel


def rank_chunks(
    query_vectors: np.ndarray,
    chunk_vectors: np.ndarray,
    chunks: Sequence[Chunk],
    top_k_chunks: int,
) -> dict[int, list[Chunk]]:
    scores = query_vectors @ chunk_vectors.T
    rankings: dict[int, list[Chunk]] = {}
    for query_index in range(scores.shape[0]):
        candidate_indices = np.argsort(-scores[query_index])[:top_k_chunks]
        rankings[query_index] = [chunks[index] for index in candidate_indices]
    return rankings


def paper_run_from_chunks(chunks: Sequence[Chunk], top_k_papers: int) -> list[str]:
    seen: set[str] = set()
    papers: list[str] = []
    for chunk in chunks:
        if chunk.paper_id in seen:
            continue
        seen.add(chunk.paper_id)
        papers.append(chunk.paper_id)
        if len(papers) == top_k_papers:
            break
    return papers


def build_runs(
    labels: Sequence[QueryLabel],
    ranked_chunks: dict[int, list[Chunk]],
    top_k_papers: int,
) -> dict[str, list[str]]:
    runs: dict[str, list[str]] = {}
    for query_index, label in enumerate(labels):
        runs[label.query_id] = paper_run_from_chunks(
            ranked_chunks[query_index],
            top_k_papers=top_k_papers,
        )
    return runs


def collapse_reranked_chunk_ids(
    ranked_chunk_ids: Sequence[str],
    chunk_by_id: dict[str, Chunk],
    top_k_papers: int,
) -> list[str]:
    seen: set[str] = set()
    papers: list[str] = []
    for chunk_id in ranked_chunk_ids:
        paper_id = chunk_by_id[chunk_id].paper_id
        if paper_id in seen:
            continue
        seen.add(paper_id)
        papers.append(paper_id)
        if len(papers) == top_k_papers:
            break
    return papers


def hybrid_fusion(
    dense_chunks: list[Chunk],
    bm25_chunks: list[Chunk],
    top_k: int,
    rrf_k: int = 60,
) -> list[Chunk]:
    dense_rank = {c.chunk_id: i for i, c in enumerate(dense_chunks)}
    bm25_rank = {c.chunk_id: i for i, c in enumerate(bm25_chunks)}
    all_ids = set(dense_rank) | set(bm25_rank)
    scored = []
    for cid in all_ids:
        dr = dense_rank.get(cid, len(dense_chunks))
        br = bm25_rank.get(cid, len(bm25_chunks))
        score = 1.0 / (rrf_k + dr) + 1.0 / (rrf_k + br)
        scored.append((cid, score))
    scored.sort(key=lambda x: x[1], reverse=True)
    lookup = {c.chunk_id: c for c in dense_chunks}
    lookup.update({c.chunk_id: c for c in bm25_chunks})
    return [lookup[cid] for cid, _ in scored[:top_k]]


class BM25Retriever:
    def __init__(self, chunks: Sequence[Chunk]):
        self.chunks = list(chunks)
        self.tokenized = [self._tokenize(c.text) for c in chunks]
        self.index = BM25Okapi(self.tokenized)

    def retrieve(self, query: str, top_k: int) -> list[Chunk]:
        tokenized_query = self._tokenize(query)
        scores = self.index.get_scores(tokenized_query)
        top_indices = np.argsort(scores)[::-1][:top_k]
        return [self.chunks[i] for i in top_indices]

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        return text.lower().split()


class HybridRetriever:
    def __init__(
        self,
        chunks: Sequence[Chunk],
        encoder: SentenceTransformerEncoder,
        chunk_vectors: np.ndarray,
        rrf_k: int = 60,
    ):
        self.chunks = list(chunks)
        self.chunk_by_id = {c.chunk_id: c for c in chunks}
        self.encoder = encoder
        self.chunk_vectors = chunk_vectors
        self.bm25 = BM25Retriever(chunks)
        self.rrf_k = rrf_k

    def retrieve(self, query: str, top_k: int) -> list[Chunk]:
        query_vector, _ = self.encoder.encode_queries([query])
        dense_scores = query_vector @ self.chunk_vectors.T
        dense_indices = dense_scores[0].argsort()[::-1][:top_k]
        dense_chunks = [self.chunks[i] for i in dense_indices]

        bm25_chunks = self.bm25.retrieve(query, top_k)

        return hybrid_fusion(dense_chunks, bm25_chunks, top_k, self.rrf_k)
