from __future__ import annotations

from collections import Counter
from pathlib import Path

from arxiv_rag.io import read_jsonl
from arxiv_rag.schema import Paper, QueryLabel


EXPECTED_SPLITS = {"train": 100, "validation": 25, "test": 25}


def load_labels(path: str | Path) -> list[QueryLabel]:
    return [QueryLabel.model_validate(row) for row in read_jsonl(path)]


def load_papers(path: str | Path) -> list[Paper]:
    return [Paper.model_validate(row) for row in read_jsonl(path)]


def validate_labels(labels: list[QueryLabel], papers: list[Paper]) -> list[str]:
    errors: list[str] = []
    paper_ids = {paper.paper_id for paper in papers}

    query_ids = [label.query_id for label in labels]
    duplicate_query_ids = [item for item, count in Counter(query_ids).items() if count > 1]
    if duplicate_query_ids:
        errors.append(f"Duplicate query_id values: {', '.join(sorted(duplicate_query_ids))}")

    split_counts = Counter(label.split for label in labels)
    for split, expected_count in EXPECTED_SPLITS.items():
        actual = split_counts.get(split, 0)
        if actual != expected_count:
            errors.append(f"Split '{split}' has {actual} queries, expected {expected_count}")

    for label in labels:
        missing_ids = sorted(set(label.relevant_paper_ids) - paper_ids)
        if missing_ids:
            errors.append(
                f"{label.query_id} references paper IDs not present in corpus: "
                + ", ".join(missing_ids[:10])
            )
    return errors


def qrels_for_split(labels: list[QueryLabel], split: str) -> dict[str, set[str]]:
    return {
        label.query_id: set(label.relevant_paper_ids)
        for label in labels
        if label.split == split
    }
