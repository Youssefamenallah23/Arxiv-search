from __future__ import annotations

import argparse
import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.config import DEFAULT_EMBEDDING_MODELS, Settings
from arxiv_rag.embeddings import SentenceTransformerEncoder
from arxiv_rag.io import read_jsonl
from arxiv_rag.schema import Chunk


def main() -> None:
    parser = argparse.ArgumentParser(description="Index chunk JSONL into Qdrant.")
    parser.add_argument("--chunks", required=True)
    parser.add_argument("--model", default="bge-small")
    parser.add_argument("--url", default=None)
    parser.add_argument("--collection", default=None)
    parser.add_argument("--batch-size", type=int, default=64)
    args = parser.parse_args()

    from qdrant_client import QdrantClient
    from qdrant_client.models import Distance, PointStruct, VectorParams

    settings = Settings()
    url = args.url or settings.qdrant_url
    collection = args.collection or settings.qdrant_collection

    chunks = [Chunk.model_validate(row) for row in read_jsonl(args.chunks)]
    encoder = SentenceTransformerEncoder(DEFAULT_EMBEDDING_MODELS.get(args.model, args.model))
    vectors, _ = encoder.encode_documents(
        [chunk.text for chunk in chunks], batch_size=args.batch_size
    )

    client = QdrantClient(url=url)
    client.recreate_collection(
        collection_name=collection,
        vectors_config=VectorParams(size=vectors.shape[1], distance=Distance.COSINE),
    )

    for start in range(0, len(chunks), args.batch_size):
        batch_chunks = chunks[start : start + args.batch_size]
        batch_vectors = vectors[start : start + args.batch_size]
        points = [
            PointStruct(
                id=str(uuid.uuid5(uuid.NAMESPACE_URL, chunk.chunk_id)),
                vector=vector.tolist(),
                payload={
                    "chunk_id": chunk.chunk_id,
                    "paper_id": chunk.paper_id,
                    "title": chunk.title,
                    "text": chunk.text,
                    "categories": chunk.categories,
                    "chunk_index": chunk.chunk_index,
                },
            )
            for chunk, vector in zip(batch_chunks, batch_vectors, strict=True)
        ]
        client.upsert(collection_name=collection, points=points)

    print(f"Indexed {len(chunks)} chunks into {url}/{collection}")


if __name__ == "__main__":
    main()
