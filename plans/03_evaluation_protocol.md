# Evaluation Protocol

**This is the most important document in the project. Write it before writing any code.**

## Research Questions

1. Can reranking improve retrieval quality for AI paper search?
2. Does better retrieval improve answer quality (faithfulness, completeness)?

## Relevance Definition

A document is relevant to a query if:
- It directly answers the query, **or**
- It contains methodology needed to answer the query

A document is **not** relevant merely because it shares keywords with the query.

**Caveat tied to the dataset:** because the corpus is title + abstract only (see `02_retrieval_system.md`), some genuinely relevant papers may not be labelable as "containing methodology" simply because the abstract doesn't include it. When labeling, judge relevance based on what the abstract actually contains, not on outside knowledge of the full paper — otherwise your ground truth will demand more than the system can ever retrieve, and your Recall numbers will look artificially low for reasons unrelated to retrieval quality.

## Query Dataset

**Total:** 150 queries.

**Split:**
| Split | Count | Purpose |
|---|---|---|
| Train | 100 | Used during experimentation (Stages 2–4 in `02_retrieval_system.md`) |
| Validation | 25 | Used for selecting final configs (which embedding model, chunk size, reranker on/off) |
| Test | 25 | Never touched until the single final report |

**Why split this way:** train queries give you a large enough pool to iterate on; validation queries let you select among configs without touching test; test queries give one honest, untouched read of final performance.

**Statistical caveat — read before reporting results:** 25 test queries is a small sample. A reported jump like "NDCG 0.61 → 0.82" can be driven by 2–3 queries and may not reflect a real, stable improvement. Report a bootstrap confidence interval alongside every test-set point estimate (resample the 25 queries with replacement, recompute the metric, repeat ~1,000 times, report the 90% interval). If asked in an interview "how confident are you in that number," the answer should be the interval, not the point estimate alone.

## Labeling Process

**Single annotator:** Amen Allah Youssef.

**Limitation (acknowledged explicitly, not hidden):** a single annotator introduces labeling bias and no inter-annotator agreement can be measured.

**Mitigation — self-consistency check:** after initial labeling, re-label a random subset of ~15 queries blind (without looking at your original labels) at least a few days later. Report the agreement rate between the two passes. This doesn't remove the single-annotator limitation, but it gives a concrete, honest number for how consistent your own judgments are, which is a defensible thing to say in an interview instead of just "yes, it's biased."

## Metrics

**Retrieval:**
- Recall@5
- Recall@10
- MRR
- NDCG@10

**Generation:** (see `04_generation_evaluation.md` for full rubric)
- Faithfulness
- Citation Accuracy

**Operational:**
- Cost per query
- P50 latency
- P95 latency

## Reporting Rules

- Validation metrics are for tuning and config selection only.
- **Final results reported anywhere (resume, write-up, dashboard) must come from the test split only**, evaluated exactly once, after every config decision (embedding model, chunk size, reranker on/off, generation context budget) is already locked in.
- If you change any config after seeing test results, that test set is burned — you must either accept the result as-is or relabel a fresh test split before trying again. No iterating against the test set.
