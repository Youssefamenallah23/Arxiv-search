# Failure Analysis

Analysis of 25 test queries processed through the full RAG pipeline (bge-small → bge-reranker-base → gemini-3.1-flash-lite).

## Retrieval Failures

| Failure Category | Count | Details |
|---|---|---|
| recall@10 ≤ 0.2 | 6/25 (24%) | Only 0-2 of 10 labeled relevant papers retrieved |
| MRR < 0.5 | 8/25 (32%) | Top-ranked relevant paper is at position 3+ |
| recall@10 = 0.1 | 3/25 (12%) | Only 1 of 10 labeled relevant papers retrieved |

**Worst queries by recall@10:**
- `test-001` (0.1): "text to 3D generation with signed distance fields for audio and speech processing" — highly specific multi-condition query
- `test-011` (0.1): "vision language models with evaluation" — generic query, labeling gap
- `test-020` (0.1): "automatic evaluation of generated summaries" — generic query, labeling gap

**Root cause:** Labels are TF-IDF-derived, but retrieval uses dense embeddings (bge-small). The two methods find different relevant papers. This is a labeling methodology ceiling, not a retrieval system failure per se. For example, a query like "vision language models with evaluation" has TF-IDF-relevant papers that don't rank highly in embedding space.

## Generation Failures

### Citation Accuracy Failures (2/25)

| Query | Problem |
|---|---|
| `test-002` (0.0) | Gemini grouped multiple paper IDs into a single bracket: `[2606.13141v1, 2606.07924v1, ...]` instead of separate citations `[2606.13141v1][2606.07924v1]`. The regex extractor reads the whole comma-separated string as one ID. |
| `test-016` (0.75) | Same root cause: `[2606.11087v1, 2606.10825v1]` grouped together. |

**Fix:** Normalize comma-separated citations in `extract_citations()` or prompt Gemini to use separate brackets.

### Faithfulness Failures (7/25)

3 distinct patterns:

1. **"No information" penalty (3 queries):** When the model correctly says "the abstracts do not contain information about X," the faithfulness scorer tries to verify that claim against the abstracts. Since the claim text ("abstracts do not contain information") is not literally present in the abstracts, it's marked unsupported. This is a **scorer limitation** — the answer is actually correct and cited, but the naive overlap-based faithfulness check fails.

2. **Enumeration claim penalty (2 queries):** When the model says "the provided papers discuss X, Y, Z" as an introductory sentence, that sentence contains a summary claim that may not match any single abstract's text verbatim. The subsequent bullet points are supported, but the lead sentence gets marked unsupported.

3. **Content hallucination (1 query):** One claim about temporal grounding in software engineering was genuinely not supported by the retrieved abstracts — the model extrapolated beyond the evidence.

| Pattern | Queries | Count |
|---|---|---|
| "No information" false positive | test-001, test-002, test-005 | 3 |
| Lead sentence enumeration penalty | test-018, test-020, test-021 | 3 |
| Actual hallucination | test-007 | 1 |

### Completeness Issues

- 23/25 queries scored **1/5** (the floor)
- Only 2/25 scored **5/5**

**Root cause:** The completeness scorer checks if the query string (verbatim) appears as a substring in the answer. For most queries the answer paraphrases or narrows the topic rather than echoing the exact query text. This is a **scorer design limitation** — substring matching is too strict; a semantic similarity measure would give more meaningful scores.

## Retrieval-Generation Correlation

| recall@10 bucket | Avg Faithfulness | N |
|---|---|---|
| 0.1 | 0.861 | 3 |
| 0.2 | 0.905 | 3 |
| 0.3 | 1.000 | 6 |
| 0.4 | 0.944 | 9 |
| 0.5 | 0.875 | 4 |

Weak correlation. Counterintuitively, the best faithfulness occurs at recall@10=0.3, not at 0.5. This suggests that even with partial retrieval, Gemini generates faithful answers from what it does receive. The slight dip at 0.5 may be noise from the small sample.

## LLM Errors

`gemini-3.1-flash-lite` free tier issues during evaluation:
- 503 (Server Error): Service overloaded during peak hours
- 429 (Client Error): Rate limit exceeded (500 RPD / 15 RPM)

All retried successfully with exponential backoff (max 5 attempts, base delay 5s). No queries failed permanently.

## Recommendations

1. **Fix citation parsing** to handle comma-separated IDs within brackets
2. **Improve faithfulness scorer** to exclude meta-claims about the context (e.g., "the provided abstracts discuss...")
3. **Replace completeness scorer** with semantic similarity (e.g., BERTScore or embedding cosine similarity)
4. **Re-label with dense retrieval** instead of TF-IDF to close the labeling gap if higher recall is needed
