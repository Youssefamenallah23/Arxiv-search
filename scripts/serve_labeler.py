from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import uvicorn

from arxiv_rag.annotation_app import create_app


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve the local query relevance labeler.")
    parser.add_argument("--corpus", default="data/raw/arxiv_corpus_2026-06-19.jsonl")
    parser.add_argument("--labels", default="eval/query_labels_2026-06-19.jsonl")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8010)
    args = parser.parse_args()

    app = create_app(corpus_path=args.corpus, labels_path=args.labels)
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
