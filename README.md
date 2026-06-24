# ArXiv Research Assistant

I built this to scratch a personal itch: keeping up with AI/ML papers on arXiv is impossible. There are 5,000+ new papers every month, and if you need to find something specific — "which recent papers use diffusion models for 3D generation?" — the options are keyword search (200 results, most irrelevant), skimming abstracts for hours, or relying on Twitter recommendations.

So I built a retrieval-augmented generation system over 5,000 arXiv papers. You ask a research question, it finds the most relevant papers, and generates a cited answer. This repo documents the whole thing — the experiments, the failures, and what actually worked.

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
     (dense + BM25 hybrid is the winner — 28% better than dense alone)
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

Total time: ~15-30 seconds per question. All experiment data on [W&B](https://wandb.ai/ahmedmohmohsen8881-momo/arxiv-rag).

## Results

### Retrieval: Hybrid (dense + BM25) is the clear winner

I compared four retrieval strategies on 25 validation queries. The full report is at `reports/retrieval_comparison.md`.

| Mode | R@1 | R@5 | R@10 | MRR | NDCG@10 | Latency | Reform% |
|---|---|---|---|---|---|---|---|
| dense | 0.056 | 0.172 | 0.268 | 0.657 | 0.317 | 0.02s | — |
| **hybrid** | **0.060** | **0.240** | **0.344** | 0.713 | **0.401** | **0.03s** | — |
| adaptive_dense | 0.040 | 0.164 | 0.280 | 0.550 | 0.305 | 3.89s | 88% |
| adaptive_hybrid | 0.060 | 0.220 | 0.332 | **0.724** | 0.387 | 1.80s | 96% |

Key takeaways:
- **Hybrid** beats dense across the board — recall@10 jumps from 0.268 → 0.344 (+28%), NDCG@10 from 0.317 → 0.401 (+26.5%). And it adds almost no latency (0.03s vs 0.02s).
- **Adaptive modes** (LLM-based query reformulation) were a disappointment. Despite triggering on 88-96% of queries, they either matched or underperformed their non-adaptive counterparts while being 50-200× slower. The LLM quality checker is too aggressive — it reformulates queries that didn't need it, and the narrower queries miss relevant papers the original would have caught.

Bottom line: **hybrid retrieval is the new default**. I also tried an LLM-based "adaptive" approach that reformulates bad queries — it didn't help enough to justify the cost.

### Generation: On the held-out test set

| Metric | Score | What It Means |
|--------|:-----:|---------------|
| Recall@10 | 0.332 | 33% of relevant papers appear in top 10 results |
| MRR | 0.632 | First relevant result is ranked near the top |
| NDCG@10 | 0.362 | Ranking quality weighted by relevance |
| Faithfulness | 0.962 | 96% of generated claims are supported by retrieved papers |
| Citation Accuracy | 0.992 | 99% of citations point to real, relevant papers |
| Completeness | 1.320 | Answers cover more ground than expected baselines |
| Avg response time | ~13s | Embed + search + rerank + generate |

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
  retrieval.py        Dense search, BM25, hybrid fusion (RRF)
  adaptive.py         LLM-based query reformulation + adaptive retrieval
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
| Retrieval strategy | dense vs hybrid vs adaptive_dense vs adaptive_hybrid | Hybrid (MRR 0.713, +28% R@10) |
| Test split (final) | Full pipeline on held-out data | Faithfulness 0.962 |

## Implementation Status

All features complete except AWS deployment (requires account setup).

## Project Principles

1. Corpus snapshots are dated and immutable once labeling starts
2. Validation set drives model decisions; test set is for final reporting only
3. Deployment comes last, after the pipeline is measured and proven
4. Everything is scriptable and reproducible (no manual steps)
