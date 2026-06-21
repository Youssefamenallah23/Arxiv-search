from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tqdm import tqdm

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.arxiv_api import iter_arxiv_papers
from arxiv_rag.io import write_jsonl


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect a frozen arXiv title/abstract snapshot.")
    parser.add_argument("--query", required=True, help="arXiv API search_query string.")
    parser.add_argument("--max-results", type=int, required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--sleep-seconds", type=float, default=3.0)
    args = parser.parse_args()

    output = Path(args.output)
    if output.exists():
        raise SystemExit(
            f"{output} already exists. Refusing to overwrite an immutable corpus snapshot."
        )

    papers = tqdm(
        iter_arxiv_papers(
            query=args.query,
            max_results=args.max_results,
            page_size=args.page_size,
            sleep_seconds=args.sleep_seconds,
        ),
        total=args.max_results,
        unit="paper",
    )
    write_jsonl(output, papers)
    print(f"Wrote frozen snapshot to {output}")


if __name__ == "__main__":
    main()
