from __future__ import annotations

import argparse
import random
from collections import Counter
from pathlib import Path
import sys
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.labels import load_papers, EXPECTED_SPLITS, validate_labels
from arxiv_rag.lexical import TfidfPaperRanker
from arxiv_rag.schema import QueryLabel
from arxiv_rag.io import write_jsonl


SEED_QUERIES = [
    "retrieval augmented generation for factual question answering",
    "multi turn retrieval augmented generation with reranking",
    "hallucination detection and factuality evaluation in large language models",
    "LLM agents for scientific literature analysis",
    "multimodal reasoning benchmark for vision language models",
    "video retrieval augmented generation and temporal grounding",
    "diffusion model for 3D generation",
    "text to 3D generation with signed distance fields",
    "robot learning with reinforcement learning and imitation learning",
    "vision language models for robotics control",
    "privacy preserving machine learning with differential privacy",
    "model watermarking and provenance for generative AI",
    "efficient fine tuning of large language models",
    "parameter efficient adaptation for multimodal models",
    "long context language model retrieval and memory",
    "uncertainty estimation for large language models",
    "AI safety evaluation benchmark",
    "alignment of large language models with human preferences",
    "synthetic data generation for training language models",
    "data contamination detection in language model benchmarks",
    "medical image segmentation with foundation models",
    "graph neural networks for scientific discovery",
    "time series forecasting with transformers",
    "speech recognition with self supervised learning",
    "code generation benchmark for large language models",
    "mathematical reasoning in large language models",
    "tool use planning for language model agents",
    "semantic search with dense retrieval and sparse retrieval",
    "cross lingual information retrieval",
    "low resource machine translation with language models",
    "federated learning for foundation models",
    "adversarial robustness for vision language models",
    "explainability for deep learning models",
    "causal reasoning in machine learning",
    "reinforcement learning from human feedback",
    "automatic evaluation of generated summaries",
    "document question answering with retrieval",
    "knowledge graph augmented language models",
    "continual learning for neural networks",
    "domain adaptation for computer vision",
    "remote sensing image understanding with foundation models",
    "autonomous driving perception with multimodal learning",
    "anomaly detection using deep learning",
    "AI generated image detection",
    "audio language models and speech understanding",
    "personalized recommendation with large language models",
    "neural information retrieval reranking",
    "benchmark for agentic AI systems",
    "efficient inference for large language models",
    "quantization of neural networks",
]

CATEGORY_AREAS = {
    "cs.CL": "natural language processing",
    "cs.CV": "computer vision",
    "cs.RO": "robotics",
    "cs.CR": "security and cryptography",
    "cs.IR": "information retrieval",
    "cs.HC": "human computer interaction",
    "cs.SE": "software engineering",
    "eess.AS": "audio and speech processing",
    "eess.IV": "image and video processing",
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Auto-generate query labels from seed queries and the corpus."
    )
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--min-score", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    papers = load_papers(args.corpus)
    ranker = TfidfPaperRanker(papers)
    rng = random.Random(args.seed)

    labels: list[QueryLabel] = []
    used_queries: set[str] = set()

    category_counts = Counter(cat for paper in papers for cat in paper.categories)
    top_cats = [cat for cat, _ in category_counts.most_common(30)]

    def is_duplicate(q: str) -> bool:
        q_lower = q.lower().strip()
        if q_lower in used_queries:
            return True
        for existing in used_queries:
            if (
                len(set(q_lower.split()) & set(existing.split()))
                / max(len(set(q_lower.split()) | set(existing.split())), 1)
                > 0.7
            ):
                return True
        return False

    def make_label(query: str) -> QueryLabel | None:
        if is_duplicate(query):
            return None
        results = ranker.rank(query, limit=args.top_k)
        relevant_ids = [paper.paper_id for paper, score in results if score >= args.min_score]
        if len(relevant_ids) < 2:
            return None
        used_queries.add(query.lower().strip())
        return QueryLabel(
            query_id="",
            split="train",
            query=query,
            relevant_paper_ids=relevant_ids,
            notes="auto-generated by auto_label.py via TF-IDF relevance ranking",
        )

    for seed in SEED_QUERIES:
        label = make_label(seed)
        if label:
            labels.append(label)

    for seed in SEED_QUERIES[:30]:
        tokens = seed.split()
        if len(tokens) >= 5:
            prefix = " ".join(tokens[: len(tokens) // 2])
            for suffix in ["with evaluation", "survey", "benchmark comparison"]:
                variant = f"{prefix} {suffix}"
                label = make_label(variant)
                if label:
                    labels.append(label)
                    break

    for seed in SEED_QUERIES:
        seed_lower = seed.lower()
        for cat, area in CATEGORY_AREAS.items():
            if area not in seed_lower:
                cat_query = f"{seed} for {area}"
                label = make_label(cat_query)
                if label:
                    labels.append(label)
                    if len(labels) % 10 == 0:
                        break
        if len(labels) >= 130:
            break

    for cat in top_cats[:15]:
        area = CATEGORY_AREAS.get(cat, cat.replace(".", " "))
        topics = [
            f"recent advances in {area} with deep learning",
            f"benchmark datasets and evaluation for {area}",
            f"foundation models applied to {area} tasks",
        ]
        for topic in topics:
            if len(labels) >= 150:
                break
            label = make_label(topic)
            if label:
                labels.append(label)

    label = make_label("multimodal learning across vision language and audio modalities")
    label = make_label("self supervised representation learning techniques")
    label = make_label("large language model training and optimization methods")

    rng.shuffle(labels)

    final_labels: list[QueryLabel] = []
    splits = {
        "train": EXPECTED_SPLITS["train"],
        "validation": EXPECTED_SPLITS["validation"],
        "test": EXPECTED_SPLITS["test"],
    }
    current_split = "train"
    split_counters: dict[str, int] = {"train": 0, "validation": 0, "test": 0}
    split_indices: dict[str, int] = {"train": 0, "validation": 0, "test": 0}

    for label in labels:
        for s in ["train", "validation", "test"]:
            if split_counters[s] < splits[s]:
                current_split = s
                break
        split_counters[current_split] += 1
        split_indices[current_split] += 1
        label.query_id = f"{current_split}-{split_indices[current_split]:03d}"
        label.split = current_split
        final_labels.append(label)
        if split_counters[current_split] >= splits[current_split]:
            if current_split == "train":
                current_split = "validation"
            elif current_split == "validation":
                current_split = "test"

    errors = validate_labels(final_labels, papers)
    if errors:
        print("Validation errors:")
        for err in errors:
            print(f"  ERROR: {err}")
        raise SystemExit(1)

    write_jsonl(args.output, [label.model_dump() for label in final_labels])
    print(f"Wrote {len(final_labels)} labels to {args.output}")
    for s, expected in EXPECTED_SPLITS.items():
        actual = sum(1 for label in final_labels if label.split == s)
        print(f"  {s}: {actual}/{expected}")


if __name__ == "__main__":
    main()
