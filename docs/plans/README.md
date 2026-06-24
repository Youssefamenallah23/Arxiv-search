# ArXiv Research Assistant — Project Plan

## Goal

Build a research-quality retrieval-augmented generation (RAG) system over AI/ML papers, with the explicit goal of producing **defensible, reproducible evidence** of the following skills — not a polished chatbot:

- Information Retrieval (embedding models, chunking, reranking)
- Experiment design and evaluation methodology
- RAG generation evaluation (faithfulness, citation accuracy)
- Failure analysis
- Basic MLOps (experiment tracking, reproducibility)
- Production deployment (lowest priority — see note below)

The question this project answers for an interviewer is:

> "Can this person design experiments, evaluate a retrieval system honestly, diagnose failures, and ship something — in that order of importance?"

## Priority Order

This is a solo, time-boxed project. Priorities are explicit so scope creep doesn't creep back in:

1. **Retrieval system + evaluation** (data, embeddings, chunking, reranking) — non-negotiable
2. **Generation evaluation** (faithfulness, citation accuracy, completeness) — non-negotiable
3. **Failure analysis** — non-negotiable, this is the highest interview value per hour spent
4. **Deployment + monitoring** — last, and the first thing to cut or simplify if time runs short

Deployment is real but secondary. A working, well-evaluated local pipeline with honest numbers beats a deployed system with weak evaluation every time, for the kind of roles this project targets.

## Success Criteria

A finished project provides:

- [x] Retrieval evaluation: Recall@5, Recall@10, MRR, NDCG@10 — reported on a held-out test set only
- [x] Generation evaluation: Faithfulness, Citation Accuracy, Completeness — on the same held-out test set
- [x] Cost analysis (compute-amortized vs metered, see `06_final_step.md`)
- [x] Latency analysis broken down by pipeline stage
- [x] A written failure analysis report
- [ ] Fully reproducible experiments (logged in W&B, fixed seeds/configs)
- [ ] Cloud deployment / Docker Compose (see `06_final_step.md`)

## Completed

- [x] Phase 1: Corpus collection (5,000 papers from arXiv API)
- [x] Phase 2: Embedding model comparison (bge-small, e5-small, minilm)
- [x] Phase 3: Chunking analysis (all papers fit in one chunk — no-op)
- [x] Phase 4: Reranking (bge-reranker-base, +2-5% improvement)
- [x] Phase 5: Generation evaluation (Gemini, faithfulness/citation/completeness scoring)
- [x] Phase 6: Failure analysis (written report with retrieval/generation findings)
- [x] Phase 7: Deployment basics (CLI tool + Streamlit UI)
- [x] Phase 8: FastAPI backend (in-memory numpy + Qdrant vector store)
- [x] Phase 8.1: `src/arxiv_rag/serving.py` — RAGPipeline wrapper (retrieve → rerank → generate)
- [x] Phase 8.2: `src/arxiv_rag/vector_store.py` — QdrantIndexer + QdrantSearcher (local SQLite + server mode)
- [x] Phase 8.3: `src/arxiv_rag/api.py` — FastAPI endpoints (`/health`, `/query`) with auto-detect Qdrant
- [x] Phase 8.4: `scripts/run_api.py` — Entry point; `scripts/index_qdrant.py` — Qdrant indexing

## Scope Restrictions

Do **not**:
- Build a large frontend
- Support multiple LLM providers
- Support multiple vector databases
- Build an agent framework
- Expand the dataset past 5,000–10,000 papers "for more impressive numbers" — the goal is evaluation quality, not scale

## Final Stack

| Component | Choice |
|---|---|
| Embedding | BAAI/bge-small-en-v1.5 (selected via experiment, see `02_retrieval_system.md`) |
| Vector DB | Qdrant |
| Reranker | BAAI/bge-reranker-base |
| LLM | Gemini |
| Backend | FastAPI |
| Experiment Tracking | Weights & Biases |
| Deployment | Docker + AWS EC2 |

## Dataset

Target: **5,000–10,000 papers**, sourced from the ArXiv API, fields: title, abstract, categories, authors, date.

**Known limitation, documented upfront:** the corpus is title/abstract-only, not full text. This caps how well the system can answer questions that require methodology detail not present in an abstract. This is treated as a deliberate, documented scope decision — not discovered after the fact. See `03_evaluation_protocol.md`.

## Document Index

1. `01_plan_and_timeline.md` — phases, rough timeline, definition of done per phase
2. `02_retrieval_system.md` — data collection, embedding experiment, chunking experiment, reranking
3. `03_evaluation_protocol.md` — the most important document; write before coding
4. `04_generation_evaluation.md` — faithfulness/citation/completeness rubric, failure analysis
5. `05_deployment_and_monitoring.md` — Docker, AWS, monitoring, dashboard (last priority, kept lean)
6. `06_final_step.md` — Cost analysis, latency analysis, FastAPI + Qdrant integration
