# ArXiv Research Assistant

Evaluation-first RAG project over AI/ML arXiv paper titles and abstracts.

This repo follows the project rules in `plans/`:

1. Freeze a dated arXiv JSONL snapshot.
2. Build labeled query splits before tuning.
3. Run retrieval experiments on train/validation only.
4. Touch the test split once for the final end-to-end report.
5. Treat deployment as the last priority.

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
Copy-Item .env.example .env
```

Then edit `.env` with your external service credentials:

- `WANDB_API_KEY` for experiment tracking
- `GEMINI_API_KEY` for generation evaluation

## First Manual Milestone

Create and freeze the corpus:

```powershell
python scripts/collect_arxiv.py --query "cat:cs.AI OR cat:cs.CL OR cat:cs.CV OR cat:cs.LG OR cat:stat.ML" --max-results 5000 --output data/raw/arxiv_corpus_2026-06-19.jsonl
python scripts/build_data_card.py --corpus data/raw/arxiv_corpus_2026-06-19.jsonl --output reports/data_card_2026-06-19.md
```

Do not edit that JSONL snapshot after downstream labels or experiments reference it. If you need a different corpus later, create a new dated snapshot.

## Query Labels

Fill `eval/query_labels_template.jsonl` into a real label file, for example:

```powershell
Copy-Item eval/query_labels_template.jsonl eval/query_labels_2026-06-19.jsonl
```

You need 150 total queries:

- 100 train
- 25 validation
- 25 test

Validation is for selecting embeddings, chunk size, and reranking. Test is only for the final report.

Validate the file before experiments:

```powershell
python scripts/validate_labels.py --labels eval/query_labels_2026-06-19.jsonl --corpus data/raw/arxiv_corpus_2026-06-19.jsonl
```

Use these helpers while labeling:

```powershell
python scripts/generate_labeling_candidates.py --corpus data/raw/arxiv_corpus_2026-06-19.jsonl --output reports/labeling_candidates_2026-06-19.md --limit 8
python scripts/search_corpus.py --data/raw/arxiv_corpus_2026-06-19.jsonl --query "your research question" --limit 15
python scripts/label_status.py --labels eval/query_labels_2026-06-19.jsonl --corpus data/raw/arxiv_corpus_2026-06-19.jsonl
```

Model smoke test:

```powershell
python scripts/smoke_models.py
```

## Retrieval Experiments

Run these only after the label file validates.

Phase 2, embedding comparison at fixed chunk size:

```powershell
python scripts/run_embedding_experiment.py --corpus data/raw/arxiv_corpus_2026-06-19.jsonl --labels eval/query_labels_2026-06-19.jsonl --split validation --chunk-size 512 --wandb
```

Phase 3, chunking comparison with the chosen embedding model:

```powershell
python scripts/run_chunking_experiment.py --corpus data/raw/arxiv_corpus_2026-06-19.jsonl --labels eval/query_labels_2026-06-19.jsonl --model bge-small --split validation --wandb
```

Phase 4, vector search vs reranking:

```powershell
python scripts/run_reranking_experiment.py --corpus data/raw/arxiv_corpus_2026-06-19.jsonl --labels eval/query_labels_2026-06-19.jsonl --model bge-small --chunk-size 512 --split validation --wandb
```

Do not run these commands with `--split test`. The scripts intentionally only allow `train` or `validation`.

---

## Architecture

### Project Layout (new files)

```
src/arxiv_rag/
├── api.py              # FastAPI app — /health, /query endpoints
├── serving.py          # RAGPipeline class — corpus → retrieve → rerank → generate
└── vector_store.py     # QdrantIndexer + QdrantSearcher — persistent vector storage

scripts/
├── run_api.py          # Entry point: uvicorn arxiv_rag.api:app
├── index_qdrant.py     # (existing) Index pre-built chunk JSONL into Qdrant server
└── search_qdrant.py    # (existing) Search Qdrant from CLI
```

### Pipeline Flow

```
query  ──►  embed (bge-small)  ──►  search (numpy dot OR Qdrant)  ──►  rerank (bge-reranker-base)  ──►  generate (Gemini)  ──►  answer + citations + latency
```

Two retrieval backends:
- **In-memory**: numpy dot product on all chunk vectors (loaded at startup, ~6 min)
- **Qdrant**: cosine similarity search against pre-indexed Qdrant collection (~10ms)

---

## FastAPI Backend

A production-ready HTTP API wrapping the full RAG pipeline.

### Quick Start (In-Memory Mode)

```powershell
.venv\Scripts\python.exe scripts\run_api.py --port 8000
```

Startup takes ~6 minutes to load the corpus, chunk, and embed 5000 papers. After that every query is fast.

### Quick Start (Qdrant Mode — Recommended)

```powershell
# Step 1: Index once (takes ~6 min)
.venv\Scripts\python.exe -c "
from pathlib import Path
import sys; sys.path.insert(0, 'src')
from arxiv_rag.io import read_jsonl
from arxiv_rag.schema import Chunk
from arxiv_rag.config import DEFAULT_EMBEDDING_MODELS
from arxiv_rag.embeddings import SentenceTransformerEncoder
from arxiv_rag.vector_store import QdrantIndexer

chunks = [Chunk.model_validate(r) for r in read_jsonl('data/processed/chunks_512_2026-06-19.jsonl')]
encoder = SentenceTransformerEncoder(DEFAULT_EMBEDDING_MODELS['bge-small'])
indexer = QdrantIndexer(path='data/qdrant_db')
indexer.create_collection(vector_size=384, recreate=True)
indexer.index_chunks(chunks, encoder, batch_size=32)
print('Done')
"

# Step 2: Serve (instant startup — auto-detects Qdrant DB)
.venv\Scripts\python.exe scripts\run_api.py --port 8000 --qdrant-path data/qdrant_db
```

### CLI Flags for `run_api.py`

| Flag | Description |
|------|-------------|
| `--port` | Port to listen on (default: 8000) |
| `--use-qdrant` | Force Qdrant mode (auto-detected by default) |
| `--force-in-memory` | Force in-memory numpy search (re-embeds at startup) |
| `--qdrant-path` | Path to local Qdrant storage (persistent, no server needed) |

### Endpoints

#### `GET /health`

```json
{"status":"ok","corpus_size":5000,"index_loaded":true,"mode":"in-memory"}
```

#### `POST /query`

Request:
```json
{"query": "diffusion models for 3D generation", "top_k": 50, "context_budget": 5}
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `query` | string | — | Research question (required) |
| `top_k` | int | 50 | Chunks to retrieve before reranking |
| `context_budget` | int | 5 | Chunks passed to Gemini as context |

Response:
```json
{
  "query": "diffusion models for 3D generation",
  "answer": "Based on the provided abstracts...",
  "citations": ["2606.08957v1", "2606.13451v1", "2606.08953v1"],
  "evidence": [
    {"paper_id": "2606.08957v1", "title": "Rethinking 3D Shape...", "text": "..."}
  ],
  "latency": {"retrieval": 0.025, "rerank": 10.367, "generation": 3.135, "total": 13.527},
  "usage": {"prompt_tokens": 899, "completion_tokens": 215, "total_tokens": 1114}
}
```

#### Interactive Docs

Open `http://localhost:8000/docs` for Swagger UI, or `http://localhost:8000/redoc` for ReDoc.

### Testing with curl

```powershell
curl http://localhost:8000/health

curl -X POST http://localhost:8000/query ^
  -H "Content-Type: application/json" ^
  -d "{\"query\":\"attention mechanisms in transformers\"}"
```

---

## Qdrant Integration

### Why Qdrant?

The in-memory mode re-embeds all 5000 chunks on every startup — taking ~6 minutes each time. Qdrant stores precomputed embeddings persistently, so the API starts in seconds.

### Two Storage Modes

| Mode | Startup | Persistence | Dependency |
|------|---------|-------------|------------|
| In-memory | ~6 min (embed) | None | None |
| Qdrant (local) | ~8 sec | Disk (SQLite, 27 MB) | None (local) |
| Qdrant (server) | ~8 sec | Qdrant server | Docker (qdrant/qdrant) |

### Local Mode (No Docker Needed)

`QdrantClient(path="./data/qdrant_db")` uses SQLite on disk — no server required. Data is stored at `data/qdrant_db/`:

```
data/qdrant_db/
├── .lock                           # Concurrent access lock
├── meta.json                       # Collection metadata
└── collection/
    └── arxiv_abstract_chunks/
        └── storage.sqlite           # 27 MB — vectors + payloads
```

### Storage Breakdown

| Component | Size |
|-----------|------|
| Vectors (5000 × 384 × float32) | ~7.7 MB |
| Payloads (paper_id, title, text) | ~7 MB |
| SQLite index overhead | ~12 MB |
| **Total** | **~27 MB** |

### Performance Comparison

| Phase | In-Memory | Qdrant |
|-------|:---------:|:------:|
| Startup (one-time) | 364s (embed 5K) | 0s (pre-indexed) |
| Query encode | 12ms | 13ms |
| Vector search | 20ms | 27ms |
| Results | — | **identical** |

Scores and rankings are identical between backends because both use the same bge-small embeddings with cosine similarity.

### CLI Inspection Commands

```powershell
# Collection stats
.venv\Scripts\python.exe -c "
from qdrant_client import QdrantClient
from arxiv_rag.config import Settings
c = QdrantClient(path='data/qdrant_db')
info = c.get_collection(Settings().qdrant_collection)
print(f'Points: {info.points_count}, Vector size: {info.config.params.vectors.size}, Distance: {info.config.params.vectors.distance}')
"

# View sample points
.venv\Scripts\python.exe -c "
from qdrant_client import QdrantClient
c = QdrantClient(path='data/qdrant_db')
pts = c.scroll('arxiv_abstract_chunks', limit=3, with_payload=True, with_vectors=False)
for p in pts[0]:
    print(f'{p.id}: [{p.payload[\"paper_id\"]}] {p.payload[\"title\"][:60]}')
"

# Delete and re-index
.venv\Scripts\python.exe -c "
from qdrant_client import QdrantClient
QdrantClient(path='data/qdrant_db').delete_collection('arxiv_abstract_chunks')
"
```

### Script: index_qdrant.py (existing)

Takes pre-built chunk JSONL and indexes into a Qdrant *server* (needs Docker):

```powershell
docker run -p 6333:6333 qdrant/qdrant
python scripts/index_qdrant.py --chunks data/processed/chunks_512_2026-06-19.jsonl
python scripts/search_qdrant.py --query "papers about retrieval augmented generation"
```

---

## Running the Full Stack

| Service | Port | Command |
|---------|------|---------|
| Streamlit Chat UI | 8501 | `.venv\Scripts\streamlit.exe run ui/app.py` |
| Streamlit Dashboard | 8502 | `.venv\Scripts\streamlit.exe run ui/dashboard.py` |
| FastAPI (auto-detect) | 8000 | `.venv\Scripts\python.exe scripts\run_api.py --port 8000` |
| FastAPI (force in-memory) | 8000 | `.venv\Scripts\python.exe scripts\run_api.py --port 8000 --force-in-memory` |
| FastAPI (explicit Qdrant) | 8000 | `.venv\Scripts\python.exe scripts\run_api.py --port 8000 --use-qdrant --qdrant-path data/qdrant_db` |
| Labeler UI | 8010 | `.venv\Scripts\python.exe scripts\serve_labeler.py` |

---

## Current Implementation Status

| Area | Status |
|------|--------|
| arXiv API snapshot collection | ✅ Done |
| Data card generation | ✅ Done |
| Query label validation | ✅ Done |
| Chunking utilities | ✅ Done |
| Retrieval metrics (Recall@k, MRR, NDCG) | ✅ Done |
| Embedding/chunking/reranking experiments | ✅ Done |
| Generation evaluation (faithfulness, citation, completeness) | ✅ Done |
| Failure analysis | ✅ Done |
| CLI query tool | ✅ Done |
| Streamlit chat UI | ✅ Done |
| **FastAPI backend** | **✅ Done** |
| **Qdrant vector store (local + server)** | **✅ Done** |
| **Monitoring dashboard** | **✅ Done** |
| **Latency & cost analysis** | **✅ Done** |
| W&B experiment logging (`--wandb` flag) | 🟡 Flag exists, needs invocation |
| Docker Compose | ❌ Not started |
| AWS deployment | ❌ Not started |
