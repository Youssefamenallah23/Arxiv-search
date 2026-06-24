# Retrieval Strategy Comparison

## Experiment Setup

- **Corpus**: arXiv AI/ML paper abstracts (5000 chunks, 512-token chunks with proportional overlap)
- **Encoder**: `BAAI/bge-small-en-v1.5` (384-dim)
- **Split**: validation (25 queries)
- **Top-k chunks**: 50 → Top-k papers: 10
- **Fusion**: RRF with k=60
- **LLM**: `gemini-3.1-flash-lite` (free tier, 15 req/min)
- **Date**: 2026-06-24

## Results

| Mode | R@1 | R@5 | R@10 | MRR | NDCG@10 | Lat(mean) | Reform% |
|---|---|---|---|---|---|---|---|
| dense | 0.056 | 0.172 | 0.268 | 0.657 | 0.317 | 0.019s | 0% |
| hybrid | 0.060 | 0.240 | 0.344 | 0.713 | 0.401 | 0.033s | 0% |
| adaptive_dense | 0.040 | 0.164 | 0.280 | 0.550 | 0.305 | 3.890s | 88% |
| adaptive_hybrid | 0.060 | 0.220 | 0.332 | 0.724 | 0.387 | 1.804s | 96% |

## Key Findings

### Hybrid is the winner overall

**Hybrid (dense + BM25 + RRF)** achieves the best balance of metrics:
- Highest Recall@5 (+39.5% over dense), Recall@10 (+28.4% over dense)
- Highest NDCG@10 (+26.5% over dense)
- Competitive MRR (0.713, second only to adaptive_hybrid's 0.724)
- Near-zero latency overhead (0.033s vs 0.019s for dense)

### Adaptive modes underperform their non-adaptive counterparts

- **Adaptive_dense** is strictly worse than plain dense on every metric except recall@10 (0.280 vs 0.268, a marginal +4.5%). MRR drops from 0.657 → 0.550 (-16.3%).
- **Adaptive_hybrid** matches or slightly beats hybrid on MRR (0.724 vs 0.713, +1.5%) but is worse on Recall@5, Recall@10, and NDCG@10.
- Both adaptive modes trigger reformulation on the vast majority of queries (88-96%), indicating the LLM quality checker is overly aggressive.
- Latency increases by **50-200×** due to the LLM API call per query.

### Why adaptive reformulation hurts

The LLM-based quality check reformulates most queries into longer, more specific versions. While this seems beneficial, in practice:

1. The reformulated queries often shift the retrieval focus too narrowly, missing relevant papers that the original broader query would capture.
2. The RRF merge of both rounds helps but doesn't fully compensate — original query results get diluted.
3. The LLM's judgment of "sufficient" is inconsistent, leading to unnecessary reformulations.

### Recommendation

**Use hybrid retrieval (dense + BM25 + RRF)** as the default retrieval strategy. It delivers the best retrieval quality with negligible latency overhead. The adaptive LLM-based approach adds significant cost and latency with no clear benefit.

## Qualitative Examples

### Where adaptive_hybrid helped (improved ranking)

| Query | Reformulation | Effect |
|---|---|---|
| `data contamination detection with evaluation` | "What methods are used to detect data contamination in Large Language Model (LLM) training sets or benchmarks?" | More specific, better matched to relevant papers |
| `foundation models applied to stat ML tasks` | "What are the applications and methodologies for using foundation models or large language models in statistical machine learning tasks?" | Clarified "stat ML" → better coverage |

### Where adaptive_dense hurt (over-narrowing)

| Query | Reformulation | Problem |
|---|---|---|
| `robot learning with reinforcement with evaluation` | "How is evaluation integrated into reinforcement learning frameworks for robot learning, such as preference-based or autonomous policy improvement methods?" | Overly specific — missed papers on general robot RL evaluation |
| `efficient fine tuning of large language models for computer vision` | "What are the parameter-efficient fine-tuning (PEFT) techniques, such as LoRA or prefix tuning, specifically used for adapting large multimodal models to computer vision tasks?" | Too narrow — missed papers on other CV fine-tuning approaches |
