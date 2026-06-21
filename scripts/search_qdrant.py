from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.config import DEFAULT_EMBEDDING_MODELS, Settings
from arxiv_rag.embeddings import SentenceTransformerEncoder


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a manual Qdrant search sanity check.")
    parser.add_argument("--query", required=True)
    parser.add_argument("--model", default="bge-small")
    parser.add_argument("--url", default=None)
    parser.add_argument("--collection", default=None)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    from qdrant_client import QdrantClient

    settings = Settings()
    url = args.url or settings.qdrant_url
    collection = args.collection or settings.qdrant_collection

    encoder = SentenceTransformerEncoder(DEFAULT_EMBEDDING_MODELS.get(args.model, args.model))
    query_vector, _ = encoder.encode_queries([args.query])
    client = QdrantClient(url=url)
    results = client.search(
        collection_name=collection,
        query_vector=query_vector[0].tolist(),
        limit=args.limit,
    )

    for index, result in enumerate(results, start=1):
        payload = result.payload or {}
        print(f"{index}. {payload.get('paper_id')} score={result.score:.4f}")
        print(f"   {payload.get('title')}")


if __name__ == "__main__":
    main()
