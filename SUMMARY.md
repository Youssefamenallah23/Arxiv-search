# Architecture & Design Summary

## Why This Project Exists

Build a production-quality RAG system over 5,000 arXiv AI/ML papers to answer research questions with citations, using an evaluation-first methodology that prevents data leakage and overfitting.

---

## Architecture

```
User query
     |
     v
[Embedding]  bge-small-fp16 -> 384-dim vector
     |
[Retrieval]  numpy dot (in-memory) OR Qdrant cosine (persistent)
     |
[Reranking]  bge-reranker-base on top-50 results -> top-5
     |
[Generation] Gemini 3.5 Flash lite -> answer + citations
     |
     v
Structured response: {answer, citations, evidence, latency, usage}
```

### Two Retrieval Backends

| Aspect | In-Memory | Qdrant |
|--------|-----------|--------|
| Startup | ~6 min (re-embed 5000 papers) | ~8 sec (load pre-indexed) |
| Storage | None (RAM only) | Disk (SQLite, ~27 MB) |
| Dependency | None | None (local mode) |
| Query latency | ~20ms | ~27ms |
| Results | Same as Qdrant | Same as in-memory |

Same embeddings (bge-small, cosine similarity) -> identical results.

---

## Technology Choices

### sentence-transformers (bge-small-fp16)
- 384-dim vectors, fast encode (~13ms/query), good retrieval quality.
- Lightweight enough to run on consumer hardware.
- bge-reranker-base for the reranking stage (cross-encoder quality).

### Qdrant (local SQLite mode)
- Zero infrastructure: `QdrantClient(path="./data/qdrant_db")` stores everything in SQLite.
- No Docker required — works on Windows, macOS, Linux.
- 27 MB for 5000 x 384-dim vectors + payloads (paper_id, title, text).
- File lock prevents concurrent access (portalocker) — intentional safety.

### FastAPI
- Automatic OpenAPI docs at `/docs` and `/redoc`.
- Pydantic v2 for request/response validation.
- Async by default, but RAG pipeline is sync (blocking calls to Gemini/embeddings).

###  Gemini 3.5 Flash lite
- Free tier available (with rate limits handled by exponential backoff).
- Good generation quality for summarization with citations.
- Rate limits: 5 retries with 5s base delay + jitter.

### Weights & Biases
- Experiment tracking for retrieval/generation metrics.
- Logs per-model results, hyperparameters, latency, cost.
- View at: https://wandb.ai/ahmedmohmohsen8881-momo/arxiv-rag

### Streamlit
- Rapid prototyping for dashboards and chat UI.
- Dashboard: 5 tabs (retrieval, generation, latency, cost, failures).
- Chat UI: conversational interface to the RAG pipeline.

---

## Design Decisions

### 1. Evaluation-First Methodology
- Freeze a dated corpus snapshot before any labeling or experiments.
- 100 train / 25 validation / 25 test query splits.
- Validation set used for model selection (embedding, chunk size, reranker).
- Test set touched exactly once for final report — prevents overfitting.
- Corpus is never modified after labels reference it; create dated snapshots.

### 2. Chunking with Overlap
- Proportional overlap (15% of chunk size) ensures boundary context.
- Token-level splitting (whitespace) preserves paper_id provenance.
- Chunks indexed at query time for in-memory mode, pre-indexed for Qdrant.

### 3. Separated Indexing & Serving
- `scripts/index_qdrant.py` handles one-time index build.
- `scripts/run_api.py` handles serving (detects pre-existing index).
- Separation of concerns: indexing = batch op, serving = low-latency queries.

### 4. Auto-Detect Mode
- API auto-detects Qdrant DB at startup (checks for `data/qdrant_db/meta.json`).
- Falls back to in-memory mode if no Qdrant DB exists.
- `--use-qdrant` and `--force-in-memory` flags for explicit control.

### 5. Structured Evaluation Pipeline
- Retrieval metrics: Recall@k (k=1,5,10,50), MRR, NDCG@10.
- Generation metrics: Citation F1, Faithfulness (Gemini-based), Completeness.
- Bootstrap confidence intervals for all metrics.
- Failure analysis categorizes errors (missing papers, hallucinated citations, etc.).

### 6. Cost Tracking
- Token usage tracked per query (prompt + completion + total).
- Cost estimated per model tier (Gemini free vs paid, embedding vs generation).
- Dashboard tab for cost analysis.

---

## Data Flow

### Indexing path
```
arXiv API -> collect_arxiv.py -> raw JSONL snapshot (dated)
    |
    v
build_chunks.py -> chunk JSONL (dated)
    |
    v
index_qdrant.py -> Qdrant (local SQLite or server)
```

### Query path
```
User query -> embed (bge-small)
    |
    +--> Qdrant search (cosine) OR numpy dot product
    |
    v
Top 50 chunks -> rerank (bge-reranker-base) -> top 5
    |
    v
 Gemini 3.5 Flash lite -> answer with [citations]
    |
    v
Structured response
```

### Evaluation path
```
Labeled queries (train/val/test)
    |
    v
run_embedding_experiment.py  (compare models on val)
run_chunking_experiment.py   (compare sizes on val)
run_reranking_experiment.py  (compare rerankers on val)
    |
    v
run_generation_evaluation.py (test split, final report)
    |
    v
W&B logs + reports/
```

---

## File Layout

```
src/arxiv_rag/         Core library (100% coverage target)
scripts/               Runnable entry points
ui/                    Streamlit interfaces
tests/                 pytest suite (31 tests)
data/raw/              Frozen JSONL corpus snapshots
data/processed/        Pre-computed chunks
data/qdrant_db/        Persistent Qdrant vectors
eval/                  Query labels
reports/               Data cards, experiment reports, failure analysis
plans/                 Project plans & methodology docs
```
