# Plan and Timeline

This is a rough schedule, not a contract. If a phase overruns, the response is to **cut scope within that phase**, not to extend the whole project. Deployment is the designated cut target — see priority order in `README.md`.

## Phase Breakdown

### Phase 0 — Evaluation Protocol (Week 1)
Write `03_evaluation_protocol.md` in full *before* any code. Define relevance criteria, query set, split sizes, labeling process, metrics.
**Definition of done:** the document is complete and you could hand it to someone else and they'd know exactly how to label a query.

### Phase 1 — Data Collection (Week 1–2)
Pull 5,000–10,000 papers from the ArXiv API. Store as immutable, dated JSONL snapshot (don't re-pull and silently change the corpus mid-project).
**Definition of done:** a frozen dataset file you will not touch again, plus a short data card (counts by category/year).

### Phase 2 — Embedding Experiment (Week 2)
Compare BGE-small, E5-small, MiniLM at a **fixed default chunk size** (e.g. 512 tokens). Log Recall@10, latency, storage size per model in W&B. Pick one, document why.
**Definition of done:** one paragraph stating the chosen model and the metric tradeoffs that justified it.

### Phase 3 — Chunking Experiment (Week 2–3)
Using the chosen embedding model, test chunk sizes 512 / 768 / 1024, each with a fixed ~15% overlap. Evaluate on the validation split only.
**Definition of done:** chosen chunk size documented, plus a one-line sanity check confirming the Phase 2 embedding choice still wins at this chunk size (if not, re-open Phase 2 — don't ignore the conflict).

### Phase 4 — Reranking Experiment (Week 3)
Baseline (vector search only) vs vector search + bge-reranker-base. Measure Recall@10, MRR, NDCG@10 on validation.
**Definition of done:** before/after metrics table, logged in W&B.

### Phase 5 — Generation Evaluation (Week 3–4)
Run the full pipeline (retrieval + rerank + Gemini generation) on the **test set only, once**. Score faithfulness, citation accuracy, completeness per `04_generation_evaluation.md`.
**Definition of done:** a scored table for all 25 test queries, plus the blind self-consistency check on a subset.

### Phase 6 — Failure Analysis (Week 4)
Categorize every failing query from Phase 5. Write the failure report.
**Definition of done:** a short report — this is the single highest-value document for interviews. Do not skip or rush this to save time for deployment.

### Phase 7 — Deployment (Week 5, lowest priority)
Docker + EC2 deployment, only after Phases 0–6 are done and documented.
**Definition of done:** see `05_deployment_and_monitoring.md`. If time is short, a documented "would deploy as X, here's why" writeup with local Docker Compose is an acceptable fallback — a half-finished cloud deployment is worse than a clearly-scoped local one.

### Phase 8 — Monitoring + Dashboard (Week 5, lowest priority)
Only attempted after Phase 7. Same fallback logic applies.

## Cut Rules

If you're behind schedule, cut in this order:
1. Dashboard polish (keep raw metrics in W&B instead, that's still valid evidence)
2. Cloud deployment (document the deployment plan instead of executing it)
3. Reduce test set size further only as an absolute last resort, and note the smaller n explicitly
4. Never cut: evaluation protocol, failure analysis, the test-set discipline (no peeking)
