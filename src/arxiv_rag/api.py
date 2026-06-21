from __future__ import annotations

import logging
import os
import time
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from arxiv_rag.serving import RAGPipeline
from arxiv_rag.vector_store import QdrantSearcher

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

pipeline: RAGPipeline | None = None


def _qdrant_available(qdrant_path: str | None = None) -> bool:
    db_path = qdrant_path or os.environ.get("RAG_QDRANT_PATH") or "data/qdrant_db"
    if not Path(db_path).exists():
        return False
    try:
        searcher = QdrantSearcher(path=db_path)
        info = searcher.client.get_collection(searcher.collection)
        count = info.points_count
        return count is not None and count > 0
    except Exception:
        return False


class QueryRequest(BaseModel):
    query: str = Field(min_length=1, description="Research question or query")
    top_k: int = Field(default=50, ge=1, le=200, description="Chunks to retrieve before reranking")
    context_budget: int = Field(
        default=5, ge=1, le=50, description="Chunks passed to LLM as context"
    )


class EvidenceItem(BaseModel):
    paper_id: str
    title: str
    text: str


class LatencyBreakdown(BaseModel):
    retrieval: float
    rerank: float
    generation: float
    total: float


class UsageInfo(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class QueryResponse(BaseModel):
    query: str
    answer: str
    citations: list[str]
    evidence: list[EvidenceItem]
    latency: LatencyBreakdown
    usage: UsageInfo


class HealthResponse(BaseModel):
    status: str
    corpus_size: int
    index_loaded: bool
    mode: str
    qdrant_connected: bool = False


@asynccontextmanager
async def lifespan(app: FastAPI):
    global pipeline
    t0 = time.perf_counter()
    qdrant_path = os.environ.get("RAG_QDRANT_PATH") or None
    env = os.environ.get("RAG_USE_QDRANT", "").lower()

    if env in ("1", "true", "yes"):
        use_qdrant = True
    elif env in ("0", "false", "no"):
        use_qdrant = False
    else:
        use_qdrant = _qdrant_available(qdrant_path)
        if use_qdrant:
            logger.info("Auto-detected Qdrant storage, skipping embedding")
        else:
            logger.info("No Qdrant storage found, using in-memory (this will take ~6 min)")

    qdrant_searcher = QdrantSearcher(path=qdrant_path) if use_qdrant else None
    pipeline = RAGPipeline(
        use_qdrant=use_qdrant, qdrant_path=qdrant_path, qdrant_searcher=qdrant_searcher
    )
    elapsed = time.perf_counter() - t0
    logger.info(
        "Pipeline loaded in %.1fs (mode=%s, corpus=%d papers)",
        elapsed,
        "qdrant" if use_qdrant else "in-memory",
        len(pipeline.papers),
    )
    yield


app = FastAPI(
    title="ArXiv RAG API",
    version="0.1.0",
    description="RAG pipeline over arXiv AI/ML paper abstracts",
    lifespan=lifespan,
)


@app.get("/health", response_model=HealthResponse)
async def health():
    if pipeline is None:
        raise HTTPException(status_code=503, detail="Pipeline not loaded")
    return HealthResponse(
        status="ok",
        corpus_size=len(pipeline.papers),
        index_loaded=pipeline.chunk_vectors is not None or pipeline.use_qdrant,
        mode="qdrant" if pipeline.use_qdrant else "in-memory",
        qdrant_connected=pipeline.use_qdrant,
    )


@app.post("/query", response_model=QueryResponse)
async def query(req: QueryRequest):
    if pipeline is None:
        raise HTTPException(status_code=503, detail="Pipeline not loaded — still initializing")
    t0 = time.perf_counter()
    try:
        result = pipeline.query(
            query=req.query,
            top_k=req.top_k,
            context_budget=req.context_budget,
        )
        elapsed = time.perf_counter() - t0
        logger.info(
            "Query processed in %.1fs (query=%.40s, citations=%d, tokens=%d)",
            elapsed,
            req.query,
            len(result["citations"]),
            result["usage"].get("total_tokens", 0),
        )
        return QueryResponse(
            query=req.query,
            answer=result["answer"],
            citations=result["citations"],
            evidence=[EvidenceItem(**e) for e in result["evidence"]],
            latency=LatencyBreakdown(**result["latency"]),
            usage=UsageInfo(**result["usage"]),
        )
    except FileNotFoundError:
        logger.exception("Corpus file not found")
        raise HTTPException(
            status_code=500, detail="Corpus file not found — check data/ directory"
        ) from None
    except ValueError as exc:
        logger.exception("Invalid query parameters")
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except RuntimeError as exc:
        logger.exception("Pipeline error")
        raise HTTPException(status_code=500, detail=str(exc)) from exc
