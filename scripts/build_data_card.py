from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.labels import load_papers


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a short data card for a corpus snapshot.")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    papers = load_papers(args.corpus)
    categories = Counter(category for paper in papers for category in paper.categories)
    years = Counter(_year(paper.published) for paper in papers)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "\n".join(
            [
                "# ArXiv Corpus Data Card",
                "",
                f"- Corpus file: `{args.corpus}`",
                f"- Generated at: `{datetime.now().isoformat(timespec='seconds')}`",
                f"- Paper count: {len(papers)}",
                "- Fields: title, abstract, categories, authors, published, updated",
                "- Known limitation: title/abstract only, no full text.",
                "",
                "## Top Categories",
                "",
                *_format_counter(categories, limit=20),
                "",
                "## Papers By Year",
                "",
                *_format_counter(Counter(dict(sorted(years.items()))), limit=None),
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Wrote data card to {output}")


def _year(timestamp: str) -> str:
    return timestamp[:4] if timestamp else "unknown"


def _format_counter(counter: Counter[str], limit: int | None) -> list[str]:
    items = counter.most_common(limit) if limit is not None else counter.items()
    return [f"- {key}: {value}" for key, value in items]


if __name__ == "__main__":
    main()
