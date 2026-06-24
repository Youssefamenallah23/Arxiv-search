# Final Step: Production-Ready Serving, Monitoring & Deployment

## What's Done vs What's Left

| Area | Status | Notes |
|---|---|---|
| Retrieval eval (Recall@5/10, MRR, NDCG) | ✅ Done | Reported on held-out test set |
| Generation eval (Faithfulness, Citation, Completeness) | ✅ Done | 25 queries, final numbers in README |
| Failure analysis | ✅ Done | `docs/reports/failure_analysis_2026-06-20.md` |
| CLI tool | ✅ Done | `scripts/query_arxiv.py` |
| Streamlit UI | ✅ Done | `ui/app.py` — running on localhost:8501 |
| **FastAPI backend** | ❌ Not started | Need to split pipeline into HTTP API |
| **Docker Compose** | ❌ Not started | FastAPI + Qdrant containers |
| **Qdrant integration** | ❌ Not started | Currently using in-memory numpy |
| **W&B experiment logging** | ❌ Not started | Scripts have `--wandb` flag but never used |
| **Latency breakdown by stage** | ❌ Not started | Only total gen time tracked |
| **Cost analysis** | ❌ Not started | Compute vs API token costs |
| **Monitoring dashboard** | ❌ Not started | Streamlit page with charts |
| **Cloud deployment (AWS)** | ❌ Not started | EC2 instance setup |

---

## Phase 8: FastAPI Backend + Qdrant Integration

### 8.1 FastAPI Service (`src/arxiv_rag/api.py`)

Create a FastAPI app that wraps the existing pipeline:

```python
POST /query
  Body: {"query": "str", "top_k": int (optional), "context_budget": int (optional)}
  Response: {
    "answer": "str",
    "citations": ["paper_id", ...],
    "evidence": [{"paper_id": "str", "title": "str", "abstract": "str"}, ...],
    "latency": {"retrieval": float, "rerank": float, "generation": float, "total": float}
  }

GET /health
  Response: {"status": "ok", "corpus_size": int, "index_loaded": bool}
```

**Files to create:**
- `src/arxiv_rag/api.py` — FastAPI app, endpoints, startup event (load pipeline)
- `src/arxiv_rag/serving.py` — Pipeline wrapper with caching (separates web concern from logic)
- `scripts/run_api.py` — Entry point: `uvicorn arxiv_rag.api:app`

**Startup flow:**
1. On `@app.on_event("startup")`, load corpus, chunk, embed, store in memory
2. Accept queries, run retrieval + rerank + generation
3. Return structured response with per-stage latency

**Dependencies already in pyproject.toml:** `fastapi`, `uvicorn`

### 8.2 Qdrant Integration (`src/arxiv_rag/vector_store.py`)

Replace in-memory numpy index with Qdrant for persistent storage and future scalability.

**Files to create:**
- `src/arxiv_rag/vector_store.py` — Qdrant client wrapper

**Implementation:**
1. On startup, check if Qdrant collection exists
2. If not, embed all chunks and upsert into Qdrant
3. On query, embed query → search Qdrant → return top-k chunk IDs + scores
4. Add `--qdrant` flag to scripts to toggle between in-memory and Qdrant

**Why Qdrant matters:**
- Persistent index (no re-embed on restart)
- Scalable beyond 5K papers (future expansion to 50K+)
- Filtering by categories, date ranges

**Dependencies already in pyproject.toml:** `qdrant-client`

### 8.3 W&B Experiment Logging

Each experiment script (`run_embedding_experiment.py`, `run_reranking_experiment.py`, `run_generation_evaluation.py`) already has `--wandb` flag support. The logging code exists but was never invoked.

**To enable:**
1. Run with `--wandb` flag: `.\.venv\Scripts\python.exe scripts/run_embedding_experiment.py --corpus ... --labels ... --wandb`
2. Set `WANDB_PROJECT=arxiv-rag` in `.env`
3. Verify runs appear in W&B dashboard
4. Add W&B links to `docs/reports/README.md`

---

## Phase 9: Docker Compose

### 9.1 Containerization (`docker-compose.yml`)

Two services:

```yaml
services:
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - QDRANT_URL=http://qdrant:6333
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    depends_on:
      - qdrant
    volumes:
      - ./data:/app/data  # corpus file
```

**Files to create:**
- `Dockerfile` — `python:3.12-slim`, install deps, copy src
- `docker-compose.yml` — as above
- `.dockerignore` — exclude `.venv`, `.git`, node_modules, etc.

### 9.2 Test Docker Setup

```powershell
# Build and start
docker compose build
docker compose up -d

# Test health
curl http://localhost:8000/health

# Test query
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d '{"query": "diffusion models for 3D generation"}'
```

---

## Phase 10: AWS Deployment

### 10.1 EC2 Setup

```powershell
# 1. Launch EC2 instance
#    - AMI: Ubuntu 24.04 LTS
#    - Instance: t3.xlarge (4 vCPU, 16 GB RAM — enough for CPU inference)
#    - Storage: 30 GB gp3

# 2. SSH in and install Docker
sudo apt update && sudo apt install -y docker.io docker-compose-v2

# 3. Clone the repo and copy the corpus
git clone <repo-url> /home/ubuntu/arxiv
scp data/raw/arxiv_corpus_2026-06-19.jsonl ubuntu@<ip>:/home/ubuntu/arxiv/data/raw/

# 4. Start services
cd /home/ubuntu/arxiv
docker compose up -d

# 5. Set up reverse proxy (nginx/caddy)
#    - Caddy: single binary, auto HTTPS via Let's Encrypt
```

### 10.2 Cost Justification

Based on CPU-only latency measurements:
- Embedding: ~6 min to index 5K papers (one-time)
- Retrieval: <0.1s per query
- Reranking: ~12s per query on CPU
- Generation: ~5s per query (API call)

**Instance choice: t3.xlarge** ($0.1664/hr on-demand, ~$120/month)
- 4 vCPU, 16 GB RAM — handles reranking in parallel with API serving
- No GPU needed — all models run on CPU within acceptable latency
- Cost per query: amortized compute ($0.1664/hr / ~100 queries/hr = $0.0017/query) + API tokens ($0.0003/query for Gemini 3.1 Flash Lite) ≈ **$0.002/query**

---

## Phase 11: Monitoring Dashboard

### 11.1 Streamlit Monitoring Dashboard (`ui/dashboard.py`)

Add a new Streamlit page alongside the chat UI. Switch between them with a sidebar navigation.

**Metrics to display:**
1. **Retrieval metrics** — bar chart of Recall@5, Recall@10, MRR, NDCG@10 from test set
2. **Per-query retrieval scatter** — each query's recall@10 with query ID labels
3. **Generation metrics** — faithfulness, citation accuracy, completeness histograms
4. **Latency breakdown** — stacked bar chart showing retrieval vs rerank vs gen time per query
5. **Cost tracker** — running total cost based on token usage from eval runs
6. **Failure analysis summary** — count of queries by failure category

**Data source:** `data/results/eval_test_generation.jsonl` (already has all fields)

**Implementation:**
```python
# ui/dashboard.py
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="ArXiv RAG Dashboard", layout="wide")

# Load eval data
with open("data/results/eval_test_generation.jsonl") as f:
    rows = [json.loads(line) for line in f]

# Tab 1: Retrieval metrics
# Tab 2: Generation metrics
# Tab 3: Latency analysis
# Tab 4: Cost analysis
```

---

## Phase 12: Latency & Cost Analysis

### 12.1 Latency Breakdown

Instrument the pipeline to log per-stage timing on every query:

| Stage | Measured In | Current Data |
|---|---|---|
| Retrieval (embed query + search) | `scripts/query_arxiv.py` | Not tracked separately |
| Reranking | `scripts/query_arxiv.py` | ~12s on CPU |
| Generation | `generation.py` | ~4.9s avg (Gemini API) |
| Total | `scripts/query_arxiv.py` | Not tracked |

**Fix:** Add timing to `search()` in `ui/app.py` (already partially done — retrieval_sec, rerank_sec, gen_sec are captured but need to be logged persistently).

### 12.2 Cost Analysis

| Component | Cost Type | Rate | Per Query |
|---|---|---|---|
| Embedding (bge-small) | Amortized compute | $0.1664/hr (t3.xlarge) | ~$0.0017 |
| Reranking (bge-reranker-base) | Amortized compute | Included above | — |
| Gemini 3.1 Flash Lite | Metered API | Free tier: 500 RPD | $0 (free tier) |
| **Total** | | | **~$0.002** (or $0 on free tier) |

---

## Implementation Order

```
Priority 1: FastAPI backend (8.1)
    └─ Enables: Docker (9), Cloud (10), CURL testing

Priority 2: Qdrant integration (8.2)
    └─ Enables: persistent index, Docker Compose with real DB

Priority 3: Docker Compose (9)
    └─ Enables: reproducible local deployment

Priority 4: Monitoring dashboard (11)
    └─ Uses existing eval data, no new infra needed

Priority 5: Latency & cost analysis (12)
    └─ Document the numbers, finalize README

Priority 6: AWS deployment (10)
    └─ Lowest priority, good to have

Priority 7: W&B logging (8.3)
    └─ Nice to have, `--wandb` flag already exists
```

## Quick Commands Reference

```powershell
# Start current UI
.\.venv\Scripts\streamlit.exe run ui/app.py

# FastAPI (after creating api.py)
.\.venv\Scripts\uvicorn.exe arxiv_rag.api:app --port 8000

# Docker (after creating Dockerfile and docker-compose.yml)
docker compose up -d

# Run experiment with W&B logging
.\.venv\Scripts\python.exe scripts/run_embedding_experiment.py --corpus data/raw/arxiv_corpus_2026-06-19.jsonl --labels docs/eval/query_labels_2026-06-19.jsonl --split validation --wandb

# Dashboard
.\.venv\Scripts\streamlit.exe run ui/dashboard.py
```
