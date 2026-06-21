from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.labels import load_papers
from arxiv_rag.lexical import rank_papers_tfidf


def main() -> None:
    parser = argparse.ArgumentParser(description="Lexically search the frozen corpus for labeling.")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    papers = load_papers(args.corpus)
    ranked_papers = rank_papers_tfidf(papers, args.query, limit=args.limit)

    for rank, (paper, score) in enumerate(ranked_papers, start=1):
        print(f"{rank}. {paper.paper_id} score={score:.4f}")
        print(f"   {paper.title}")
        print(f"   Categories: {', '.join(paper.categories)}")
        print(f"   Abstract: {paper.abstract[:500]}{'...' if len(paper.abstract) > 500 else ''}")
        print()


if __name__ == "__main__":
    main()
