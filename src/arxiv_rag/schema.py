from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class Paper(BaseModel):
    paper_id: str
    arxiv_url: str
    title: str
    abstract: str
    categories: list[str]
    authors: list[str]
    published: str
    updated: str | None = None


class QueryLabel(BaseModel):
    query_id: str
    split: Literal["train", "validation", "test"]
    query: str
    relevant_paper_ids: list[str] = Field(min_length=1)
    notes: str = ""


class Chunk(BaseModel):
    chunk_id: str
    paper_id: str
    title: str
    text: str
    categories: list[str]
    chunk_index: int
    token_start: int
    token_end: int
