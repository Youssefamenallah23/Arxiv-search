# Labeling Guide

Use this guide to create `docs/eval/query_labels_2026-06-19.jsonl`.

## Rules

- Judge only the title and abstract in the frozen corpus.
- A paper is relevant if it directly answers the query or contains methodology needed to answer it.
- Do not mark a paper relevant only because it shares keywords.
- Keep the test split untouched after labeling. Do not use it to choose models, chunk size, reranking, prompt wording, or context budget.

## Recommended Workflow

1. Write a concrete research question.
2. Search the corpus for candidate papers:

```powershell
python scripts/search_corpus.py --corpus data/raw/arxiv_corpus_2026-06-19.jsonl --query "retrieval augmented generation factual question answering" --limit 15
```

3. Read the shown titles and abstracts.
4. Add one JSONL row with the relevant paper IDs.
5. Repeat until you have:
   - 100 train queries
   - 25 validation queries
   - 25 test queries
6. Validate the file:

```powershell
python scripts/validate_labels.py --labels docs/eval/query_labels_2026-06-19.jsonl --corpus data/raw/arxiv_corpus_2026-06-19.jsonl
```

## Query Design

Prefer queries that can be answered from abstracts, such as:

- Which papers use retrieval-augmented generation to improve factuality?
- Which papers evaluate hallucination in large language models?
- Which papers propose diffusion-based methods for 3D generation?
- Which papers apply reinforcement learning to robotics control?
- Which papers introduce benchmarks for multimodal reasoning?

Avoid questions that require full-paper details, such as exact training hyperparameters, ablation table values, or implementation details not likely to appear in abstracts.

## JSONL Shape

Each line must look like this:

```json
{"query_id":"train-001","split":"train","query":"Which papers use retrieval-augmented generation to improve factuality?","relevant_paper_ids":["2601.12345v1","2602.23456v2"],"notes":"Relevant abstracts explicitly discuss RAG and factuality."}
```
