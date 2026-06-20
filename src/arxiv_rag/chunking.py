from __future__ import annotations

from collections.abc import Iterable

from arxiv_rag.schema import Chunk, Paper


def chunk_paper(paper: Paper, chunk_size: int, overlap: int) -> list[Chunk]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    text = f"Title: {paper.title}\nAbstract: {paper.abstract}"
    tokens = _tokenize(text)
    if not tokens:
        return []

    chunks: list[Chunk] = []
    step = chunk_size - overlap
    start = 0
    chunk_index = 0
    while start < len(tokens):
        end = min(start + chunk_size, len(tokens))
        chunk_text = " ".join(tokens[start:end])
        chunks.append(
            Chunk(
                chunk_id=f"{paper.paper_id}::chunk-{chunk_index:04d}",
                paper_id=paper.paper_id,
                title=paper.title,
                text=chunk_text,
                categories=paper.categories,
                chunk_index=chunk_index,
                token_start=start,
                token_end=end,
            )
        )
        if end == len(tokens):
            break
        start += step
        chunk_index += 1
    return chunks


def chunk_papers(papers: Iterable[Paper], chunk_size: int, overlap: int) -> list[Chunk]:
    chunks: list[Chunk] = []
    for paper in papers:
        chunks.extend(chunk_paper(paper, chunk_size=chunk_size, overlap=overlap))
    return chunks


def proportional_overlap(chunk_size: int, fraction: float = 0.15) -> int:
    if not 0 <= fraction < 1:
        raise ValueError("fraction must be in [0, 1)")
    return round(chunk_size * fraction)


def _tokenize(text: str) -> list[str]:
    return text.split()
