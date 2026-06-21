from __future__ import annotations

import time
from collections.abc import Sequence

import numpy as np


class SentenceTransformerEncoder:
    def __init__(self, model_name: str):
        from sentence_transformers import SentenceTransformer

        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def encode_documents(
        self,
        texts: Sequence[str],
        batch_size: int = 32,
    ) -> tuple[np.ndarray, float]:
        return self._encode([self._format_document(text) for text in texts], batch_size)

    def encode_queries(
        self,
        texts: Sequence[str],
        batch_size: int = 32,
    ) -> tuple[np.ndarray, float]:
        return self._encode([self._format_query(text) for text in texts], batch_size)

    def _encode(self, texts: Sequence[str], batch_size: int) -> tuple[np.ndarray, float]:
        started = time.perf_counter()
        vectors = self.model.encode(
            list(texts),
            batch_size=batch_size,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True,
        )
        elapsed = time.perf_counter() - started
        return np.asarray(vectors, dtype=np.float32), elapsed

    def _format_query(self, text: str) -> str:
        if "e5-" in self.model_name.lower():
            return f"query: {text}"
        return text

    def _format_document(self, text: str) -> str:
        if "e5-" in self.model_name.lower():
            return f"passage: {text}"
        return text


class CrossEncoderReranker:
    def __init__(self, model_name: str):
        from sentence_transformers import CrossEncoder

        self.model_name = model_name
        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        candidates: Sequence[tuple[str, str]],
        batch_size: int = 16,
    ) -> tuple[list[str], float]:
        started = time.perf_counter()
        pairs = [(query, text) for _, text in candidates]
        scores = self.model.predict(pairs, batch_size=batch_size)
        elapsed = time.perf_counter() - started
        ranked = sorted(
            zip(candidates, scores, strict=True), key=lambda item: float(item[1]), reverse=True
        )
        return [chunk_id for (chunk_id, _), _ in ranked], elapsed
