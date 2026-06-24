# Deployment and Monitoring

**This is the lowest-priority section of the project. Do not start here, and do not let it expand to match the depth of the evaluation work — that depth belongs in `02`–`04`.**

## Sequencing Rule

Deployment happens **only after** the retrieval system, evaluation protocol, and generation evaluation (including the failure report) are complete and documented. If time runs short before reaching this phase, a clearly written "here's how I would deploy this, and why" section with a local Docker Compose setup is an acceptable substitute for a live cloud deployment.

## Containerization

**Tool:** Docker.

**Components:**
- FastAPI (serving layer)
- Qdrant (vector DB)

Keep this to a docker-compose file with two services. No orchestration beyond that is needed at this scale.

## AWS Deployment

**Target:** a single EC2 instance.

**Instance type decision:** justify the choice using your own latency numbers from `02_retrieval_system.md`/monitoring data rather than asserting it. Since the embedding model, reranker, and vector search are all small/CPU-feasible models, a CPU-only instance (e.g. t3.large/t3.xlarge class) should be sufficient — state the actual P95 latency you measured on CPU and use that number to justify not paying for a GPU instance.

**Document:**
- Instance type chosen, and the latency data that justified it
- Monthly cost estimate
- Deployment steps (concise — a numbered list is enough, this doesn't need its own essay)

## Monitoring

Track latency broken down **by pipeline stage**, not just end-to-end — this is what makes a later optimization claim ("P95 reduced from X to Y") credible instead of a hollow number:

1. Embedding time
2. Retrieval time
3. Reranking time
4. LLM generation time
5. Total request time

**Latency percentiles:** P50, P95, P99 — for each stage above, not just the total.

## Cost Metrics

Be precise about what "cost" means for each component, since the stack mixes self-hosted and metered services:

- **Embedding cost / Retrieval cost:** these run on self-hosted open-weight models on your EC2 box — there's no per-call API cost. Report this as amortized compute cost (EC2 $/hour ÷ measured queries/hour), not as a fabricated per-call price.
- **LLM cost:** this is a real metered API cost (Gemini, billed per token) — report it directly from API usage.
- **Total cost per query:** sum of the above, clearly labeled by which parts are amortized vs metered.

## Cache Metrics

If you implement a semantic cache layer (optional — cut this first if time is short):
- Hit rate
- Miss rate

## Final Deliverable

A simple dashboard (a basic Streamlit page or a few charts is enough — this doesn't need to be a polished product) showing:
- Retrieval metrics (from the test-set report in `03_evaluation_protocol.md`)
- Latency metrics, by stage
- Cost metrics
- Generation metrics (from `04_generation_evaluation.md`)

This dashboard is the visual evidence backing your resume claims — it should pull directly from your logged W&B runs and test-set results, not from numbers typed in separately.
