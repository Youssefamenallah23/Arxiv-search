from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.labels import EXPECTED_SPLITS, load_labels, load_papers, validate_labels


PLACEHOLDERS = {"REPLACE_WITH_CORPUS_ID", "1706.03762"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Show labeling progress and validation errors.")
    parser.add_argument("--labels", required=True)
    parser.add_argument("--corpus", required=True)
    args = parser.parse_args()

    labels = load_labels(args.labels)
    papers = load_papers(args.corpus)
    split_counts = Counter(label.split for label in labels)
    placeholder_rows = [
        label.query_id
        for label in labels
        if any(paper_id in PLACEHOLDERS for paper_id in label.relevant_paper_ids)
    ]

    print("Label progress")
    for split, expected in EXPECTED_SPLITS.items():
        actual = split_counts.get(split, 0)
        remaining = max(expected - actual, 0)
        print(f"- {split}: {actual}/{expected} complete, {remaining} remaining")

    if placeholder_rows:
        print()
        print("Placeholder rows still need replacement:")
        for query_id in placeholder_rows:
            print(f"- {query_id}")

    errors = validate_labels(labels, papers)
    if errors:
        print()
        print("Validation errors:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print()
    print("Label file is valid.")


if __name__ == "__main__":
    main()
