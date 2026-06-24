from __future__ import annotations

import re
import time
from pathlib import Path

import numpy as np

from arxiv_rag.adaptive import AdaptiveRetriever
from arxiv_rag.chunking import chunk_papers, proportional_overlap
from arxiv_rag.embeddings import CrossEncoderReranker, SentenceTransformerEncoder
from arxiv_rag.generation import generate_answer
from arxiv_rag.labels import load_papers
from arxiv_rag.retrieval import HybridRetriever
from arxiv_rag.schema import Chunk
from arxiv_rag.vector_store import QdrantSearcher


def _extract_citations(answer: str) -> list[str]:
    ids: list[str] = []
    for match in re.finditer(r"\[([^\]]+)\]", answer):
        content = match.group(1)
        for part in content.split(","):
            part = part.strip()
            if re.match(r"^\d{4}\.\d{5}(v\d+)?$", part):
                ids.append(part)
    seen: set[str] = set()
    return [x for x in ids if not (x in seen or seen.add(x))]


class RAGPipeline:
    def __init__(
        self,
        corpus_path: str = "data/raw/arxiv_corpus_2026-06-19.jsonl",
        chunk_size: int = 512,
        embedding_model: str = "BAAI/bge-small-en-v1.5",
        reranker_model: str = "BAAI/bge-reranker-base",
        llm_model: str = "gemini-3.1-flash-lite",
        use_qdrant: bool = False,
        qdrant_path: str | None = None,
        qdrant_searcher: QdrantSearcher | None = None,
        retrieval_mode: str = "dense",
    ):
        self.chunk_size = chunk_size
        self.llm_model = llm_model
        self.use_qdrant = use_qdrant
        self.retrieval_mode = retrieval_mode

        corpus = Path(corpus_path)
        if not corpus.exists():
            raise FileNotFoundError(f"Corpus not found: {corpus}")

        self.papers = load_papers(corpus_path)
        overlap = proportional_overlap(chunk_size)
        self.chunks = chunk_papers(self.papers, chunk_size=chunk_size, overlap=overlap)
        self.chunk_by_id: dict[str, Chunk] = {c.chunk_id: c for c in self.chunks}

        self.encoder = SentenceTransformerEncoder(embedding_model)
        self.reranker = CrossEncoderReranker(reranker_model)

        if use_qdrant:
            self.qdrant_searcher = qdrant_searcher or QdrantSearcher(path=qdrant_path)
            self.chunk_vectors = None
        else:
            self.qdrant_searcher = None
            chunk_texts = [c.text for c in self.chunks]
            self.chunk_vectors, _ = self.encoder.encode_documents(chunk_texts)

        self._build_retriever()

    def _build_retriever(self) -> None:
        if self.retrieval_mode in ("hybrid", "adaptive_hybrid"):
            base = HybridRetriever(
                self.chunks,
                self.encoder,
                self.chunk_vectors,
            )
        else:
            base = None

        if self.retrieval_mode in ("adaptive_dense", "adaptive_hybrid"):
            retriever = base if base is not None else object()
            self._retriever = AdaptiveRetriever(retriever, self.chunks)
        else:
            self._retriever = base or object()

    def query(
        self,
        query: str,
        top_k: int = 50,
        context_budget: int = 5,
    ) -> dict:
        t0 = time.perf_counter()
        result = self._retrieve(query, top_k)
        retrieval_sec = time.perf_counter() - t0

        if isinstance(result, tuple):
            ranked_chunks, adaptive_meta = result
        else:
            ranked_chunks = result
            adaptive_meta = None

        t0 = time.perf_counter()
        candidates = [(c.chunk_id, c.text) for c in ranked_chunks]
        ranked_ids, _ = self.reranker.rerank(query, candidates)
        reranked = [self.chunk_by_id[cid] for cid in ranked_ids]
        rerank_sec = time.perf_counter() - t0

        budget = reranked[:context_budget]
        evidence = [{"paper_id": c.paper_id, "title": c.title, "text": c.text} for c in budget]

        answer, gen_sec, usage = generate_answer(
            query=query,
            chunks=evidence,
            model_name=self.llm_model,
        )

        citations = _extract_citations(answer)
        total = retrieval_sec + rerank_sec + gen_sec

        response = {
            "answer": answer,
            "citations": citations,
            "evidence": evidence,
            "latency": {
                "retrieval": round(retrieval_sec, 3),
                "rerank": round(rerank_sec, 3),
                "generation": round(gen_sec, 3),
                "total": round(total, 3),
            },
            "usage": usage,
            "retrieval_mode": self.retrieval_mode,
        }
        if adaptive_meta:
            response["adaptive"] = {
                "reformulated": adaptive_meta["reformulated"],
                "reformulated_query": adaptive_meta.get("reformulated_query"),
            }
        return response

    def _retrieve(self, query: str, top_k: int) -> list[Chunk] | tuple[list[Chunk], dict]:
        if self.use_qdrant:
            query_vector, _ = self.encoder.encode_queries([query])
            results = self.qdrant_searcher.search(query_vector[0], top_k=top_k)
            return [self.chunk_by_id[cid] for cid, _ in results]

        if isinstance(self._retriever, AdaptiveRetriever):
            return self._retriever.retrieve(query, top_k)

        if isinstance(self._retriever, HybridRetriever):
            return self._retriever.retrieve(query, top_k)

        query_vector, _ = self.encoder.encode_queries([query])
        scores = query_vector @ self.chunk_vectors.T
        top_indices = scores[0].argsort()[::-1][:top_k]
        return [self.chunks[i] for i in top_indices]
