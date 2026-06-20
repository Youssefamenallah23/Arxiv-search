from __future__ import annotations

import re
from collections.abc import Sequence


def extract_citations(text: str) -> list[str]:
    ids = re.findall(r"\[([^\]]+)\]", text)
    expanded: list[str] = []
    for id_str in ids:
        parts = [p.strip() for p in id_str.split(",")]
        for part in parts:
            part = part.strip()
            if part:
                expanded.append(part)
    return expanded


def score_faithfulness(
    answer: str,
    chunks: Sequence[dict],
) -> tuple[float, list[dict]]:
    claims = _split_claims(answer)
    chunk_texts = [chunk["text"].lower() for chunk in chunks]
    all_text = " ".join(chunk_texts).lower()

    results: list[dict] = []
    supported = 0
    for claim in claims:
        claim_lower = claim.lower()
        is_supported = _claim_in_context(claim_lower, all_text)
        if is_supported:
            supported += 1
        results.append({"claim": claim, "supported": is_supported})

    total = len(claims)
    score = supported / total if total > 0 else 1.0
    return score, results


def score_citation_accuracy(
    answer: str,
    chunks: Sequence[dict],
) -> tuple[float, list[dict]]:
    chunk_map = {chunk["paper_id"]: chunk for chunk in chunks}
    citations = extract_citations(answer)

    if not citations:
        return 1.0, []

    results: list[dict] = []
    correct = 0
    for citation in citations:
        chunk = chunk_map.get(citation)
        if chunk is None:
            results.append(
                {
                    "citation": citation,
                    "correct": False,
                    "reason": "paper_id not in retrieved chunks",
                }
            )
            continue
        results.append({"citation": citation, "correct": True, "reason": ""})
        correct += 1

    return correct / len(citations), results


def score_completeness(
    query: str,
    answer: str,
    key_points: list[str],
) -> tuple[int, list[dict]]:
    answer_lower = answer.lower()
    covered = 0
    results: list[dict] = []
    for point in key_points:
        is_covered = point.lower() in answer_lower
        if is_covered:
            covered += 1
        results.append({"key_point": point, "covered": is_covered})

    total = len(key_points)
    if total == 0:
        return 5, results

    fraction = covered / total
    if fraction >= 0.9:
        score = 5
    elif fraction >= 0.7:
        score = 4
    elif fraction >= 0.5:
        score = 3
    elif fraction >= 0.25:
        score = 2
    else:
        score = 1

    return score, results


def _split_claims(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]


def _claim_in_context(claim: str, context: str) -> bool:
    claim_tokens = set(claim.split())
    if len(claim_tokens) < 5:
        return claim in context
    important = {t for t in claim_tokens if len(t) > 3 and not t.startswith("[")}
    if not important:
        return claim in context
    overlap = sum(1 for t in important if t in context)
    return overlap / len(important) >= 0.5
