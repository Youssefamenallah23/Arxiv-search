# Generation Evaluation

Most RAG projects stop at retrieval. This project evaluates the actual generated answer, because that's what a user experiences — good retrieval with a hallucinated answer is still a failure.

## Research Question

Does better retrieval improve answer quality?

## Pipeline Configuration (decide before running eval, not after)

Define and lock these before generating a single answer for evaluation:
- **Context budget:** how many reranked chunks are passed to Gemini (e.g. top 5)
- **Truncation rule:** what happens if those chunks exceed the model's context window (e.g. drop lowest-ranked chunk first)

This matters because "context truncation" is one of the failure categories below — you can't diagnose a truncation failure against a rule that wasn't fixed in advance.

## Evaluation Dataset

The same 25 held-out test queries from `03_evaluation_protocol.md`. Never used during retrieval tuning. Used exactly once for the final report.

## Evaluation Rubric

For each of the 25 test answers, score:

### 1. Faithfulness
Does every claim in the answer appear in the retrieved context?
- `0` = hallucinated (claim not supported by any retrieved chunk)
- `1` = supported

Score per claim, then report the fraction of supported claims per answer.

### 2. Citation Accuracy
Can the cited paper actually support the statement attributed to it?
- `0` = incorrect citation
- `1` = correct citation

### 3. Completeness
Did the answer cover the key concepts a correct answer should include?
Scale: 1–5, with fixed anchors defined **before** scoring (write the expected key points for each query first, then score against that list):
- `1` = covered none of the expected key points
- `2` = covered a small minority
- `3` = covered about half
- `4` = covered most
- `5` = covered all expected key points

## Self-Consistency Check

You are both the system's builder and its only judge, which is a real bias risk. Mitigate it the same way as the labeling process: re-score a subset (~10 of the 25 answers) blind, without referencing your first-pass scores, at least a few days later. Report the agreement rate. This is a cheap, concrete answer to "how do you know your eval isn't just biased toward your own system."

## Failure Analysis

For every test query that scores poorly on any rubric dimension, categorize the failure using one (or more) of these fixed categories:

| Category | Definition |
|---|---|
| Retrieval failure | The relevant paper(s) were never retrieved in the top-k candidates |
| Reranker failure | Relevant paper was retrieved but the reranker pushed it out of the final top-k |
| Context truncation | Relevant content was retrieved but cut due to the context budget rule |
| Hallucination | Answer made a claim not supported by any retrieved chunk |
| Ambiguous query | The query itself has multiple reasonable interpretations |

Record category, query, and a one-line explanation for every failure.

## Deliverable: Failure Report

A short written report listing every failing query, its category, and your explanation. This is the highest interview-value artifact in the whole project — it demonstrates judgment, not just pipeline-building. Do not compress this into a single summary table; keep individual cases with enough detail that you can talk through any one of them from memory in an interview.
