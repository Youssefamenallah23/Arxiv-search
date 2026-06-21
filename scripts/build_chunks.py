from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.chunking import chunk_papers, proportional_overlap
from arxiv_rag.io import write_jsonl
from arxiv_rag.labels import load_papers


def main() -> None:
    parser = argparse.ArgumentParser(description="Build chunk JSONL from a frozen corpus.")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--chunk-size", type=int, required=True)
    parser.add_argument("--overlap", type=int, default=None)
    args = parser.parse_args()

    overlap = args.overlap
    if overlap is None:
        overlap = proportional_overlap(args.chunk_size)

    papers = load_papers(args.corpus)
    chunks = chunk_papers(papers, chunk_size=args.chunk_size, overlap=overlap)
    write_jsonl(args.output, [chunk.model_dump() for chunk in chunks])
    print(f"Wrote {len(chunks)} chunks to {args.output}")


if __name__ == "__main__":
    main()
