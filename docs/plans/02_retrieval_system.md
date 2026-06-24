# Retrieval System

## Objective

Build a retriever that finds relevant papers for a research question, with every design decision made via a logged experiment rather than asserted.

## Stage 1 — Data Collection

**Source:** ArXiv API only (no Semantic Scholar, to keep scope tight).

**Fields collected:**
- Title
- Abstract
- Categories
- Authors
- Date

**Storage:** JSONL, one paper per line.

**Reproducibility rule:** once pulled, freeze the dataset as a dated, immutable file (e.g. `arxiv_corpus_2026-06-19.jsonl`). All later experiments reference this exact file. If you need more papers later, create a new dated snapshot rather than mutating the original — otherwise nothing downstream is reproducible.

**Known limitation (documented, not discovered later):** this corpus is title + abstract only, not full text. Some technical questions (e.g. "how does X train?") may need methodology detail that isn't in the abstract. This caps the achievable Recall and Faithfulness ceiling regardless of model quality — note this explicitly in the final write-up rather than treating low scores on those queries as a retrieval bug.

## Stage 2 — Embedding Experiment

**Models compared:**
1. BGE-small
2. E5-small
3. MiniLM

**Controlled variable:** run this comparison at a single fixed default chunk size (e.g. 512 tokens, no overlap variation yet). Chunking is not yet tuned at this stage — state this explicitly so the comparison isn't confounded with a chunking decision made later.

**Metrics compared:**
- Recall@10
- Latency (embedding time per chunk)
- Storage size (index size on disk)

**Output:** pick one model, write one paragraph justifying the choice against the tradeoffs (e.g. "chose BGE-small: 4% lower Recall@10 than E5-small but 3x faster and half the storage — acceptable tradeoff for a CPU-only deployment target").

## Stage 3 — Chunking Experiment

**Configurations (run with the Stage 2 winning embedding model):**

| Config | Chunk Size | Overlap |
|---|---|---|
| A | 512 tokens | ~15% (~77 tokens) |
| B | 768 tokens | ~15% (~115 tokens) |
| C | 1024 tokens | ~15% (~154 tokens) |

Overlap is fixed proportionally across configs so it isn't a hidden confound — sentences shouldn't get silently split at chunk boundaries in some configs and not others.

**Evaluated on:** validation split only (never test).

**After choosing the best chunk size:** re-run a quick sanity check that the Stage 2 embedding model still outperforms the alternatives at this chunk size. If it doesn't, that's a real finding — document it rather than ignoring it.

## Stage 4 — Reranking Experiment

**Baseline:** vector retrieval only (Stage 2 + Stage 3 winning config).

**Experiment:** vector retrieval + BAAI/bge-reranker-base on top of the top-k candidates.

**Metrics (validation split):**
- Recall@10
- MRR
- NDCG@10

**Output:** a before/after table. This is the most "resume gold" number in the retrieval section — but it must come from real validation-split numbers, not asserted in advance.

## Logging

Every run across Stages 2–4 is logged in Weights & Biases with:
- embedding model
- chunk size + overlap
- reranker on/off
- all metrics
- dataset snapshot filename (for exact reproducibility)

**Rule:** nothing in Stages 2–4 touches the test split. Test is reserved entirely for the final, single, end-to-end report in `03_evaluation_protocol.md`.
