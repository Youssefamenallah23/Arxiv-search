# ArXiv Research Assistant

Ask research questions about 5,000 AI/ML papers and get cited answers — powered by retrieval-augmented generation.

## The Problem

AI research moves fast. 5,000+ new papers appear on arXiv every month. No researcher can read them all. If you need to answer "which recent papers use diffusion models for 3D generation?", you currently have to:

1. Search arXiv by keyword — get 200 results, most irrelevant
2. Skim abstracts manually — hours of work
3. Cross-reference citations — good luck

This project automates that entire process.

## How It Works

RAG = Retrieve + Augment + Generate. When you ask a question:

```
Your question: "diffusion models for 3D generation"
       |
       v
  1. EMBED: Convert your question into a mathematical vector
     (bge-small embedding model -> 384 numbers)
       |
       v
  2. SEARCH: Find the 50 most relevant paper chunks from 5,000
     (cosine similarity against pre-computed vectors)
     Backend options: in-memory numpy (instant) or Qdrant DB (persistent)
       |
       v
  3. RERANK: Score those 50 candidates with a cross-encoder
     (bge-reranker-base picks the best 5)
       |
       v
  4. GENERATE: Send top-5 chunks + your question to Gemini
     (Gemini 3.5 Flash lite writes a cited answer)
       |
       v
  Response: answer + citations + evidence papers + timing breakdown
```

Total time: ~15-30 seconds per question.

## Results

After evaluating on a held-out test set of 25 labeled queries:

| Metric | Score | What It Means |
|--------|:-----:|---------------|
| Recall@10 | 0.332 | 33% of relevant papers appear in top 10 results |
| MRR | 0.632 | First relevant result is ranked near the top |
| NDCG@10 | 0.362 | Ranking quality weighted by relevance |
| Faithfulness | 0.962 | 96% of generated claims are supported by retrieved papers |
| Citation Accuracy | 0.992 | 99% of citations point to real, relevant papers |
| Completeness | 1.320 | Answers cover more ground than expected baselines |
| Avg response time | ~13s | Embed + search + rerank + generate |

Reranking improves retrieval by +2-3% absolute (e.g., MRR 0.657 -> 0.677) but costs ~12s per query. All experiment data on [W&B](https://wandb.ai/ahmedmohmohsen8881-momo/arxiv-rag).

## Quick Start

### Option A: Local (Python)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
Copy-Item .env.example .env
```

Edit `.env`, set `GEMINI_API_KEY`.

```powershell
# Start the API (auto-detects Qdrant DB, falls back to in-memory)
python scripts\run_api.py --port 8000
# API at http://localhost:8000, Swagger at http://localhost:8000/docs
```

Or start with persistent Qdrant storage (instant startup):
```powershell
python scripts\run_api.py --port 8000 --qdrant-path data/qdrant_db
```

### Option B: Docker

```powershell
$env:GEMINI_API_KEY="your-key"
docker compose up -d
# API at :8000, Streamlit UI at :8501, Qdrant at :6333
```

## What You Can Do

| Interface | Purpose | How to start |
|-----------|---------|--------------|
| **Chat UI** | Ask questions conversationally | `streamlit run ui/app.py` |
| **REST API** | Integrate with other tools | `python scripts/run_api.py` |
| **Dashboard** | View metrics, latency, costs | `streamlit run ui/dashboard.py` |
| **CLI** | Quick queries from terminal | `python scripts/query_arxiv.py` |
| **Labeler UI** | Create training/eval queries | `python scripts/serve_labeler.py` |

Try a query:
```powershell
curl -X POST http://localhost:8000/query ^
  -H "Content-Type: application/json" ^
  -d "{\"query\":\"attention mechanisms in transformers\"}"
```

Response includes the answer, arXiv IDs as citations, evidence excerpts, latency breakdown, and token usage.

## Architecture

```
src/arxiv_rag/        Core library
  api.py              FastAPI app (/health, /query)
  serving.py          RAGPipeline (retrieve -> rerank -> generate)
  vector_store.py     QdrantIndexer + QdrantSearcher
  retrieval.py        Vector search and evaluation
  embeddings.py       SentenceTransformer wrappers
  generation.py       Gemini API calls + evaluation scoring
  chunking.py         Split papers into overlapping chunks
  metrics.py          Recall@k, MRR, NDCG, bootstrap CI
  schema.py           Paper, Chunk, QueryLabel Pydantic models
  config.py           Settings from environment variables

scripts/              Runnable entry points
tests/                pytest suite (31 tests)
ui/                   Streamlit interfaces
data/                 Corpus snapshots + Qdrant storage
eval/                 Query labels
reports/              Experiment results
```

### Storage Backends

| Mode | Startup time | Persistence | Dependencies |
|------|:-----------:|:-----------:|:------------:|
| In-memory | ~6 min (re-embed 5K papers) | None (RAM) | None |
| Qdrant local | ~8 sec | SQLite on disk, ~27 MB | None |
| Qdrant server | ~8 sec | Docker volume | Docker |

All modes produce identical results (same embeddings, same similarity metric).

## Methodology

This project follows an **evaluation-first** protocol to prevent data leakage:

1. Freeze a dated corpus snapshot before any labeling
2. Build labeled query splits: 100 train / 25 validation / 25 test
3. Run all experiments (embedding, chunking, reranking) on train/validation only
4. Touch the test split exactly once for the final report

## Experiment Tracking

All experiment results are on [Weights & Biases](https://wandb.ai/ahmedmohmohsen8881-momo/arxiv-rag):

| Experiment | What We Tested | Winner |
|------------|---------------|--------|
| Embedding models | bge-small vs e5-small vs minilm | bge-small (MRR 0.657) |
| Chunk sizes | 512 vs 768 vs 1024 tokens | No significant difference |
| Reranking | baseline vs bge-reranker-base | Reranker wins (+0.02 MRR) |
| Test split (final) | Full pipeline on held-out data | Faithfulness 0.962 |

## Implementation Status

All features complete except AWS deployment (requires account setup).

## Project Principles

1. Corpus snapshots are dated and immutable once labeling starts
2. Validation set drives model decisions; test set is for final reporting only
3. Deployment comes last, after the pipeline is measured and proven
4. Everything is scriptable and reproducible (no manual steps)
