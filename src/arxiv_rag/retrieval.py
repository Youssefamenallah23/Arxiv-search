from __future__ import annotations

from collections.abc import Sequence

import numpy as np

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
