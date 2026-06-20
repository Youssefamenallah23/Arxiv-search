from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, PointStruct, VectorParams

from arxiv_rag.config import Settings
from arxiv_rag.embeddings import SentenceTransformerEncoder
from arxiv_rag.schema import Chunk


class QdrantIndexer:
    def __init__(
        self,
        url: str | None = None,
        path: str | None = None,
        collection: str | None = None,
    ):
        settings = Settings()
        self.collection = collection or settings.qdrant_collection
        if path:
            self.client = QdrantClient(path=path)
        else:
            self.client = QdrantClient(url=url or settings.qdrant_url)

    def create_collection(self, vector_size: int, recreate: bool = False) -> None:
        if recreate:
            self.client.recreate_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
            )
        else:
            existing = self.client.collection_exists(self.collection)
            if not existing:
                self.client.create_collection(
                    collection_name=self.collection,
                    vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
                )

    def index_chunks(
        self,
        chunks: Sequence[Chunk],
        encoder: SentenceTransformerEncoder,
        batch_size: int = 32,
    ) -> int:
        chunk_texts = [chunk.text for chunk in chunks]
        total = 0
        for start in range(0, len(chunk_texts), batch_size):
            batch_texts = chunk_texts[start : start + batch_size]
            batch_chunks = chunks[start : start + batch_size]
            vectors, _ = encoder.encode_documents(batch_texts)
            points = [
                PointStruct(
                    id=start + i,
                    vector=vectors[i].tolist(),
                    payload={
                        "chunk_id": c.chunk_id,
                        "paper_id": c.paper_id,
                        "title": c.title,
                        "text": c.text,
                    },
                )
                for i, c in enumerate(batch_chunks)
            ]
            self.client.upsert(
                collection_name=self.collection,
                points=points,
            )
            total += len(points)
        return total


class QdrantSearcher:
    def __init__(
        self,
        url: str | None = None,
        path: str | None = None,
        collection: str | None = None,
    ):
        settings = Settings()
        self.collection = collection or settings.qdrant_collection
        if path:
            self.client = QdrantClient(path=path)
        else:
            self.client = QdrantClient(url=url or settings.qdrant_url)

    def search(
        self,
        query_vector: np.ndarray,
        top_k: int = 50,
    ) -> list[tuple[str, float]]:
        response = self.client.query_points(
            collection_name=self.collection,
            query=query_vector.tolist(),
            limit=top_k,
        )
        return [(hit.payload["chunk_id"], hit.score) for hit in response.points]
