# ArXiv Research Assistant

**Evaluation-first RAG system** over 5,000 AI/ML arXiv paper abstracts. FastAPI backend, Qdrant vector persistence, Streamlit dashboards, W&B experiment tracking.

```
query -> embed (bge-small) -> search (numpy/Qdrant) -> rerank (bge-reranker) -> generate (Gemini) -> answer + citations
```

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
Copy-Item .env.example .env
```

Edit `.env` with your API keys:
- `GEMINI_API_KEY` — generation & evaluation
- `WANDB_API_KEY` — experiment tracking (optional)

## What You Can Do

| Task | Command |
|------|---------|
| Chat UI | `.venv\Scripts\streamlit.exe run ui/app.py` |
| REST API | `.venv\Scripts\python.exe scripts\run_api.py --port 8000` |
| Monitoring dashboard | `.venv\Scripts\streamlit.exe run ui/dashboard.py` |
| CLI query | `.venv\Scripts\python.exe scripts\query_arxiv.py` |
| Label queries | `.venv\Scripts\python.exe scripts\serve_labeler.py` |
| Run experiments | `scripts/run_embedding_experiment.py --wandb` |

## Architecture

```
src/arxiv_rag/
  api.py           FastAPI app — /health, /query
  serving.py       RAGPipeline — retrieve -> rerank -> generate
  vector_store.py  QdrantIndexer + QdrantSearcher
  retrieval.py     Chunk retrieval & evaluation metrics
  embeddings.py    SentenceTransformer wrappers
  generation.py    Gemini generation + evaluation
  chunking.py      Paper -> overlapping chunks
  metrics.py       Recall@k, MRR, NDCG, bootstrap
  schema.py        Paper, Chunk, QueryLabel models
  config.py        Settings from env vars
  labels.py        Query label validation
  arxiv_api.py     arXiv API client
  io.py            JSONL read/write helpers

scripts/
  run_api.py           FastAPI entry point
  index_qdrant.py      Index chunks into Qdrant (server mode)
  search_qdrant.py     Search Qdrant from CLI
  query_arxiv.py       Interactive CLI pipeline
  run_embedding_experiment.py  Embedding comparison
  run_chunking_experiment.py   Chunk size comparison
  run_reranking_experiment.py  Reranker comparison
  collect_arxiv.py     Download paper corpus
  build_chunks.py      Pre-compute chunks for Qdrant

ui/
  app.py         Streamlit chat UI
  dashboard.py   Monitoring dashboard (5 tabs)

tests/
  test_api.py, test_serving.py, test_chunking.py,
  test_metrics.py, test_labels.py, test_annotation.py
```

## API Reference

### `GET /health`

```json
{"status": "ok", "corpus_size": 5000, "index_loaded": true, "mode": "qdrant"}
```

### `POST /query`

Request:
```json
{"query": "diffusion models for 3D generation", "top_k": 50, "context_budget": 5}
```

Response:
```json
{
  "query": "diffusion models for 3D generation",
  "answer": "Based on the provided abstracts...",
  "citations": ["2606.08957v1", "2606.13451v1"],
  "evidence": [{"paper_id": "...", "title": "...", "text": "..."}],
  "latency": {"retrieval": 0.025, "rerank": 10.367, "generation": 3.135, "total": 13.527},
  "usage": {"prompt_tokens": 899, "completion_tokens": 215, "total_tokens": 1114}
}
```

Interactive docs at `http://localhost:8000/docs`.

## Qdrant Integration

Two retrieval backends:

| Mode | Startup | Persistence | Deps |
|------|---------|-------------|------|
| In-memory | ~6 min (re-embed) | None | None |
| Qdrant (local) | ~8 sec | Disk (SQLite, 27 MB) | None |
| Qdrant (server) | ~8 sec | Qdrant server | Docker |

Index once, then instant startup:
```powershell
.venv\Scripts\python.exe scripts\run_api.py --qdrant-path data/qdrant_db
```

## Project Principles

1. Freeze a dated arXiv JSONL snapshot — never modify after labeling starts.
2. Build labeled query splits (100 train / 25 val / 25 test) before tuning.
3. Run retrieval experiments on train/validation only.
4. Touch test split once for final end-to-end report.
5. Deployment is the last priority.

## Implementation Status

| Area | Status |
|------|--------|
| Corpus collection & data card | Done |
| Query labeling & validation | Done |
| Chunking (configurable size/overlap) | Done |
| Retrieval metrics (Recall@k, MRR, NDCG) | Done |
| Embedding/chunking/reranking experiments | Done |
| Generation evaluation (faithfulness, citation) | Done |
| Failure analysis | Done |
| CLI query tool | Done |
| Streamlit chat UI | Done |
| FastAPI backend | Done |
| Qdrant vector store (local + server) | Done |
| Monitoring dashboard | Done |
| Latency & cost analysis | Done |
| W&B experiment logging | Flag exists, needs invocation |
| Docker Compose | Not started |
| AWS deployment | Not started |
