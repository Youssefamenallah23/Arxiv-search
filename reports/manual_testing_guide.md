# Manual Testing Guide

## Prerequisites

```powershell
.venv\Scripts\Activate.ps1
```

## 1. Run Unit Tests

```powershell
pytest tests/ -v
```
Expected: 31 passed.

## 2. Run Lint & Type Check

```powershell
ruff check src/ tests/ scripts/
mypy src/ tests/ --ignore-missing-imports
```
Expected: no lint errors. mypy may have pre-existing false positives (pandas/numpy type narrowing).

## 3. Start the API (In-Memory Mode)

```powershell
python scripts/run_api.py --port 8000 --force-in-memory
```
Wait ~6 min for startup. Then:

```powershell
curl http://localhost:8000/health
```

Expected:
```json
{"status":"ok","corpus_size":5000,"index_loaded":true,"mode":"in-memory"}
```

```powershell
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d "{\"query\":\"attention mechanisms\"}"
```

Expected: 200 response with answer, citations, evidence, latency, usage.

## 4. Start the API (Qdrant Mode)

First ensure Qdrant DB exists at `data/qdrant_db/`. Then:

```powershell
python scripts/run_api.py --port 8000 --qdrant-path data/qdrant_db
```

Startup is ~8 seconds. Verify:

```powershell
curl http://localhost:8000/health
```

Expected:
```json
{"status":"ok","corpus_size":5000,"index_loaded":true,"mode":"qdrant"}
```

## 5. Swagger UI

Open http://localhost:8000/docs in a browser.

- Expand `GET /health` -> Try it out -> Execute
- Expand `POST /query` -> Try it out -> Enter `{"query": "diffusion models"}` -> Execute

## 6. Streamlit Chat UI

```powershell
streamlit run ui/app.py
```

Open http://localhost:8501. Type a research question. Expected: answer with citations after ~15-20s.

## 7. Streamlit Dashboard

```powershell
streamlit run ui/dashboard.py
```

Open http://localhost:8501 (different port). Explore 5 tabs:
- Retrieval Metrics
- Generation Metrics
- Latency Breakdown
- Cost Analysis
- Failure Analysis

## 8. Docker (if Docker Desktop is installed)

```powershell
$env:GEMINI_API_KEY="your-actual-key"
docker compose up -d
```

Verify all three services:
- `curl http://localhost:8000/health`
- Open http://localhost:8000/docs
- Open http://localhost:8501

Tear down:
```powershell
docker compose down
```

## 9. CLI Query Tool

```powershell
python scripts/query_arxiv.py --query "vision transformers" --top-k 5
```

Expected: ranked list of papers with scores.

## 10. Qdrant Inspection

```powershell
python -c "
from qdrant_client import QdrantClient
from arxiv_rag.config import Settings
c = QdrantClient(path='data/qdrant_db')
info = c.get_collection(Settings().qdrant_collection)
print(f'Points: {info.points_count}, Vector size: {info.config.params.vectors.size}')
"
```

Expected: `Points: 5000, Vector size: 384`.

## 11. W&B Dashboard

Open https://wandb.ai/ahmedmohmohsen8881-momo/arxiv-rag

Should see runs:
- `embedding-bge-small-validation`
- `embedding-e5-small-validation`
- `embedding-minilm-validation`
- `chunk-512-validation`
- `chunk-768-validation`
- `chunk-1024-validation`
- `reranking-validation`
- `final-eval-test-set`

## 12. Experiment Results (Summary Table)

| Experiment | recall@5 | recall@10 | MRR | NDCG@10 | Notes |
|------------|:--------:|:---------:|:---:|:-------:|-------|
| bge-small (baseline) | 0.172 | 0.268 | 0.657 | 0.317 | Best MRR |
| e5-small | 0.148 | 0.192 | 0.618 | 0.255 | Weaker |
| minilm | 0.140 | 0.216 | 0.562 | 0.258 | Fastest embed |
| reranked (bge) | 0.180 | 0.272 | 0.677 | 0.323 | +2-3% absolute |
| test split (final) | 0.208 | 0.332 | 0.632 | 0.362 | Held-out eval |
| Faithfulness | — | — | — | — | 0.962 |
| Citation Accuracy | — | — | — | — | 0.992 |
| Completeness | — | — | — | — | 1.320 |
