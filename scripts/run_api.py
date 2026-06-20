from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import uvicorn


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve the ArXiv RAG API.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument(
        "--use-qdrant",
        action="store_true",
        help="Use Qdrant vector search (auto-detected by default)",
    )
    parser.add_argument(
        "--force-in-memory", action="store_true", help="Skip Qdrant, use in-memory numpy search"
    )
    parser.add_argument(
        "--qdrant-path",
        default=None,
        help="Local Qdrant storage path (persistent, no server needed)",
    )
    args = parser.parse_args()

    if args.use_qdrant:
        os.environ["RAG_USE_QDRANT"] = "1"
    elif args.force_in_memory:
        os.environ["RAG_USE_QDRANT"] = "0"
    if args.qdrant_path:
        os.environ["RAG_QDRANT_PATH"] = args.qdrant_path

    uvicorn.run(
        "arxiv_rag.api:app",
        host=args.host,
        port=args.port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
