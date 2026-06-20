from __future__ import annotations

from collections import Counter
from pathlib import Path

from pydantic import BaseModel, Field

from arxiv_rag.io import write_jsonl
from arxiv_rag.labels import EXPECTED_SPLITS, load_labels, load_papers, validate_labels
from arxiv_rag.lexical import TfidfPaperRanker
from arxiv_rag.schema import Paper, QueryLabel


PLACEHOLDER_IDS = {"REPLACE_WITH_CORPUS_ID", "1706.03762"}


class LabelPayload(BaseModel):
    split: str
    query: str = Field(min_length=3)
    relevant_paper_ids: list[str] = Field(min_length=1)
    notes: str = ""


class LabelStore:
    def __init__(self, corpus_path: str | Path, labels_path: str | Path):
        self.corpus_path = Path(corpus_path)
        self.labels_path = Path(labels_path)
        self.papers = load_papers(self.corpus_path)
        self.paper_ids = {paper.paper_id for paper in self.papers}
        self.ranker = TfidfPaperRanker(self.papers)

    def search(self, query: str, limit: int = 10) -> list[dict[str, object]]:
        results = []
        for paper, score in self.ranker.rank(query, limit=limit):
            results.append(
                {
                    "paper_id": paper.paper_id,
                    "title": paper.title,
                    "abstract": paper.abstract,
                    "categories": paper.categories,
                    "authors": paper.authors,
                    "published": paper.published,
                    "score": score,
                }
            )
        return results

    def list_labels(self) -> list[QueryLabel]:
        if not self.labels_path.exists():
            return []
        return load_labels(self.labels_path)

    def status(self) -> dict[str, object]:
        labels = self.list_labels()
        split_counts = Counter(label.split for label in labels)
        placeholders = [
            label.query_id
            for label in labels
            if any(paper_id in PLACEHOLDER_IDS for paper_id in label.relevant_paper_ids)
        ]
        errors = validate_labels(labels, self.papers)
        progress = {
            split: {
                "actual": split_counts.get(split, 0),
                "expected": expected,
                "remaining": max(expected - split_counts.get(split, 0), 0),
            }
            for split, expected in EXPECTED_SPLITS.items()
        }
        return {
            "valid": not errors,
            "progress": progress,
            "placeholder_query_ids": placeholders,
            "errors": errors,
            "total_labels": len(labels),
        }

    def add_label(self, payload: LabelPayload) -> QueryLabel:
        if payload.split not in EXPECTED_SPLITS:
            raise ValueError(f"split must be one of {', '.join(EXPECTED_SPLITS)}")
        missing_ids = sorted(set(payload.relevant_paper_ids) - self.paper_ids)
        if missing_ids:
            raise ValueError("paper IDs not present in corpus: " + ", ".join(missing_ids))

        labels = [
            label
            for label in self.list_labels()
            if not any(paper_id in PLACEHOLDER_IDS for paper_id in label.relevant_paper_ids)
        ]
        label = QueryLabel(
            query_id=next_query_id(labels, payload.split),
            split=payload.split,
            query=payload.query,
            relevant_paper_ids=payload.relevant_paper_ids,
            notes=payload.notes,
        )
        labels.append(label)
        labels.sort(key=lambda item: (split_sort_key(item.split), item.query_id))
        write_jsonl(self.labels_path, [item.model_dump() for item in labels])
        return label

    def delete_label(self, query_id: str) -> bool:
        labels = self.list_labels()
        kept = [label for label in labels if label.query_id != query_id]
        if len(kept) == len(labels):
            return False
        write_jsonl(self.labels_path, [item.model_dump() for item in kept])
        return True


def next_query_id(labels: list[QueryLabel], split: str) -> str:
    prefix = f"{split}-"
    max_index = 0
    for label in labels:
        if not label.query_id.startswith(prefix):
            continue
        suffix = label.query_id.removeprefix(prefix)
        if suffix.isdigit():
            max_index = max(max_index, int(suffix))
    return f"{prefix}{max_index + 1:03d}"


def split_sort_key(split: str) -> int:
    return {"train": 0, "validation": 1, "test": 2}.get(split, 99)


def paper_preview(paper: Paper) -> dict[str, object]:
    return {
        "paper_id": paper.paper_id,
        "title": paper.title,
        "abstract": paper.abstract,
        "categories": paper.categories,
    }
