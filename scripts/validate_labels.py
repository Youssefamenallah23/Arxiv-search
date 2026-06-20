from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.labels import load_labels, load_papers, validate_labels


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate query labels against the frozen corpus.")
    parser.add_argument("--labels", required=True)
    parser.add_argument("--corpus", required=True)
    args = parser.parse_args()

    labels = load_labels(args.labels)
    papers = load_papers(args.corpus)
    errors = validate_labels(labels, papers)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"Labels valid: {len(labels)} queries against {len(papers)} papers.")


if __name__ == "__main__":
    main()
