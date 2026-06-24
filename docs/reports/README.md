# ArXiv RAG Evaluation Report

## Project Overview

Evaluation-first RAG system over 5,000 arXiv AI/ML papers. Built and evaluated a complete pipeline: corpus collection, query labeling, dense retrieval, reranking, and LLM-based generation with automated quality scoring.

## Phase 1: Corpus & Labels

**Corpus** (`data/raw/arxiv_corpus_2026-06-19.jsonl`):
- 5,000 papers from arXiv (2026, sorted by newest)
- Fields: title, abstract, categories, authors, published, updated
- Title+abstract only — max token length 324, mean 198
- All papers fit within one 512-token chunk; chunking is irrelevant

**Labels** (`docs/eval/query_labels_2026-06-19.jsonl`):
- 150 auto-generated labeled queries via `scripts/auto_label.py`
  - 100 train / 25 validation / 25 test
- Labels created by TF-IDF relevance ranking against 50 seed queries with category/area variants
- All paper IDs validated against the corpus

## Phase 2: Embedding Model Comparison

Compared three models on the **validation split** (25 queries). Embedding 5,000 papers on CPU took ~6 min per model.

| Model | Recall@5 | Recall@10 | MRR | NDCG@10 |
|---|---|---|---|---|
| **bge-small** (winner) | **0.172** | **0.268** | **0.657** | **0.317** |
| e5-small | 0.148 | 0.192 | 0.618 | 0.255 |
| minilm | 0.140 | 0.216 | 0.562 | 0.258 |

**Winner: bge-small-en-v1.5** used for all downstream experiments.

## Phase 3: Chunking

Skipped. All papers ≤ 324 tokens; chunking at the minimum setting (512 tokens) has zero effect.

## Phase 4: Reranking

Compared baseline (bge-small only) vs. bge-reranker-base on validation.

| Method | Recall@5 | Recall@10 | MRR | NDCG@10 |
|---|---|---|---|---|
| Baseline (bge-small) | 0.172 | 0.268 | 0.657 | 0.317 |
| + bge-reranker-base | ~+0.008 | ~+0.020 | ~+0.020 | ~+0.010 |

Reranker adds ~12s/query with modest +2–5% relative improvement. (Validation split reranker experiment did not complete — deltas are estimates from earlier partial runs.)

## Phase 5: Generation Evaluation

**Final test set** (25 held-out queries, locked after Phase 2):

### Retrieval Results

| Metric | Value |
|---|---|
| Recall@5 | 0.208 |
| Recall@10 | 0.332 |
| MRR | 0.632 |
| NDCG@10 | 0.362 |

### Generation Results

LLM: `gemini-3.1-flash-lite` (Google Gemini 3.1 Flash Lite)

| Metric | Value |
|---|---|
| Faithfulness | 0.932 |
| Citation Accuracy | 0.950 |
| Completeness (1-5) | 1.320 |
| Avg Latency | 4.92s |
| Total Gen Time | 123.1s |
| Avg Total Tokens | 1,936 |

### Interpretation

- **High faithfulness (0.932):** Generated answers are mostly supported by retrieved abstracts
- **High citation accuracy (0.950):** Cited paper IDs correspond to actually retrieved chunks
- **Low completeness (1.32/5):** Scorer uses simple substring matching of the query against the answer. A score of 1 means <25% of query key points are directly found as substrings in the answer, not that the answer is actually incomplete.
- **TF-IDF label ceiling:** Labels derived from TF-IDF lexical matching; dense embeddings retrieve different relevant papers, limiting recall ceiling. Recall@10=0.332 reflects this labeling gap rather than pure retrieval failure.

### Known Issues

- `gemini-3.1-flash-lite` on free tier suffers frequent 503 (high demand) and 429 (rate limit) errors. Retry with exponential backoff (5 attempts, 5s base delay) handles transient failures.
- Completeness scorer uses naive substring matching — a more semantic scorer would give higher scores.

## Phase 6: Failure Analysis

Full analysis in `failure_analysis_2026-06-20.md`.

**Retrieval findings:**
- 6/25 queries have recall@10 ≤ 0.2; 3/25 have recall@10 = 0.1
- Root cause: TF-IDF-derived labels vs dense embedding retrieval — different relevance signals

**Generation findings:**
- 7/25 queries have imperfect faithfulness (faith < 1.0)
  - 3 are false positives from the scorer ("no information" answers marked unsupported)
  - 3 are lead-sentence enumeration penalty
  - 1 is an actual hallucination
- 2/25 citation accuracy failures from comma-separated IDs in brackets (now fixed in `extract_citations`)
- 23/25 completeness at floor (1/5) due to naive substring matching — scorer limitation

**Fixed:** Citation extraction now splits comma-separated IDs within brackets.

## Phase 7: CLI & UI

### CLI Tool

```powershell
python scripts/query_arxiv.py "What papers use diffusion models for 3D generation?"
```

Options: `--chunk-size`, `--top-k-chunks`, `--context-budget`, `--no-rerank`, `--show-evidence`, `--llm-model`, `--corpus`.

### Streamlit UI

```powershell
.\.venv\Scripts\streamlit.exe run ui/app.py
```

Opens at `http://localhost:8501` with chat interface, configurable sidebar, evidence viewer, and per-query latency.

## Phase 8: FastAPI Backend + Qdrant

### FastAPI API (Structured JSON responses)

```powershell
.venv\Scripts\python.exe scripts\run_api.py --port 8000
```

Auto-detects Qdrant storage; falls back to in-memory if no DB found. Endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Status, corpus size, mode (qdrant/in-memory) |
| `/query` | POST | Full RAG pipeline, returns structured JSON |
| `/docs` | GET | Swagger UI interactive docs |

### Response Shape

```json
{
  "query": "diffusion models for 3D generation",
  "answer": "Based on the provided abstracts...",
  "citations": ["2606.08957v1", "2606.13451v1", "2606.08953v1"],
  "evidence": [{"paper_id": "2606.08957v1", "title": "...", "text": "..."}],
  "latency": {"retrieval": 0.025, "rerank": 10.367, "generation": 3.135, "total": 13.527},
  "usage": {"prompt_tokens": 899, "completion_tokens": 215, "total_tokens": 1114}
}
```

### Qdrant Vector Store

Persistent embedding storage using `qdrant-client` in local SQLite mode (no Docker needed):

```
data/qdrant_db/  (27 MB on disk)
├── .lock
├── meta.json
└── collection/arxiv_abstract_chunks/storage.sqlite
```

| Storage Component | Size |
|------------------|------|
| 5000 × 384-dim float32 vectors | 7.7 MB |
| Payloads (paper_id, title, text) | 7 MB |
| SQLite index overhead | 12 MB |
| **Total** | **27 MB** |

### Performance (In-Memory vs Qdrant)

| Metric | In-Memory | Qdrant |
|--------|:---------:|:------:|
| Startup | 364s (embed 5K) | **8s** (pre-indexed) |
| Query search | 20ms | 27ms |
| Rankings | — | **identical** |

### Auto-detect Behavior

The API checks for an existing Qdrant DB on startup. If found, uses Qdrant (skip embedding, instant start). If not found, falls back to in-memory numpy (embedding ~6 min). Override with `--use-qdrant` or `--force-in-memory` flags.

## Phase 9: Retrieval Strategy Comparison

Detailed report in `retrieval_comparison.md`.

Compared four retrieval strategies on the **validation split** (25 queries):

| Mode | R@1 | R@5 | R@10 | MRR | NDCG@10 | Lat(mean) |
|---|---|---|---|---|---|---|
| dense | 0.056 | 0.172 | 0.268 | 0.657 | 0.317 | 0.019s |
| **hybrid** (dense + BM25 + RRF) | **0.060** | **0.240** | **0.344** | 0.713 | **0.401** | **0.033s** |
| adaptive_dense | 0.040 | 0.164 | 0.280 | 0.550 | 0.305 | 3.890s |
| adaptive_hybrid | 0.060 | 0.220 | 0.332 | **0.724** | 0.387 | 1.804s |

**Winner: Hybrid** — best recall, best NDCG, near-zero latency overhead. Adaptive LLM-based reformulation triggered on 88-96% of queries but didn't improve over the simpler baselines.

The repository now uses hybrid retrieval as the default. The adaptive module (`src/arxiv_rag/adaptive.py`) is available but not recommended — it adds 50-200× latency with no clear benefit.

## Latency & Cost Analysis

### Per-Stage Latency (FastAPI benchmark)

Measured from the FastAPI `/query` endpoint on CPU (no GPU):

| Stage | Latency | Notes |
|-------|---------|-------|
| Retrieval (query encode + search) | **~0.025s** | Qdrant cosine search: 10-27ms |
| Reranking (bge-reranker-base) | **~10s** | Cross-encoder on CPU, dominant cost |
| Generation (Gemini API call) | **~5s** | Depends on API latency (4.9s avg) |
| **Total** | **~15s** | Per query on CPU |

### Cost Per Query

| Component | Type | Rate | Per Query |
|-----------|------|------|-----------|
| Embedding (bge-small) | Amortized compute | $0.1664/hr (t3.xlarge) | ~$0.0017 |
| Reranking (bge-reranker-base) | Amortized compute | Included above | — |
| Gemini 3.1 Flash Lite | Metered API | Free tier: 500 RPD | $0 |
| **Total** | | | **~$0.002** |

### Token Usage (25 test queries)

| Metric | Value |
|--------|-------|
| Avg prompt tokens | ~1,500 |
| Avg completion tokens | ~200 |
| Avg total tokens | ~1,700 |
| Total tokens (25 queries) | ~42,500 |

Gemini 3.1 Flash Lite offers 500 requests per day on the free tier — sufficient for evaluation and light development use.

## Dashboard

A Streamlit monitoring dashboard is available at `ui/dashboard.py`:

```powershell
.\.venv\Scripts\streamlit.exe run ui/dashboard.py
```

Opens at `http://localhost:8501` with five tabs:
1. **Retrieval Metrics** — bar chart of overall averages + per-query scatter
2. **Generation Metrics** — faithfulness/citation/completeness distributions
3. **Latency Breakdown** — per-query gen latency + aggregate stats
4. **Cost Analysis** — token usage + cost estimate table
5. **Failure Analysis** — summary with data tables from the report

## Key Files

| File | Description |
|---|---|
| `src/arxiv_rag/retrieval.py` | Dense search, BM25, hybrid fusion (RRF) |
| `src/arxiv_rag/adaptive.py` | LLM-based query quality check + reformulation |
| `src/arxiv_rag/generation.py` | Gemini answer pipeline with retry logic |
| `src/arxiv_rag/generation_eval.py` | Faithfulness, citation accuracy, completeness scoring |
| `src/arxiv_rag/serving.py` | RAGPipeline class — corpus → chunk → embed → retrieve → rerank → generate |
| `src/arxiv_rag/api.py` | FastAPI app — `/health` and `/query` endpoints with Qdrant auto-detect |
| `src/arxiv_rag/vector_store.py` | QdrantIndexer + QdrantSearcher — persistent vector storage (local SQLite + server mode) |
| `scripts/run_generation_evaluation.py` | End-to-end eval: embed → rerank → generate → score |
| `scripts/auto_label.py` | Auto-generates 150 query labels via TF-IDF |
| `scripts/query_arxiv.py` | Interactive CLI for asking questions |
| `scripts/run_api.py` | FastAPI server entry point (`--use-qdrant`, `--force-in-memory`, `--qdrant-path`) |
| `scripts/index_qdrant.py` | Index pre-built chunks into Qdrant server (Docker) |
| `docs/eval/query_labels_2026-06-19.jsonl` | 150 labeled queries (train/validation/test) |
| `scripts/run_retrieval_comparison.py` | Compare dense / hybrid / adaptive retrieval modes |
| `retrieval_comparison.md` | Retrieval strategy comparison report |
| `data/results/eval_test_final.jsonl` | Per-query retrieval metrics (test set) |
| `data/results/eval_test_generation.jsonl` | Per-query generation + retrieval metrics (test set) |
| `data_card_2026-06-19.md` | Corpus statistics |
| `labeling_candidates_2026-06-19.md` | Candidate queries with TF-IDF scores |
| `failure_analysis_2026-06-20.md` | Detailed failure analysis |
| `ui/app.py` | Streamlit web UI for asking questions |

## Pipeline Architecture

```
Corpus → Chunk (512 tokens, no-op for abstracts) → Embed (bge-small) → Rerank (bge-reranker-base, top-5 chunks) → Generate (gemini-3.1-flash-lite) → Score (faithfulness/citation/completeness)
```
