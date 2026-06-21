from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.labels import load_papers
from arxiv_rag.lexical import TfidfPaperRanker

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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate candidate query/paper pairs for manual relevance labeling."
    )
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()

    papers = load_papers(args.corpus)
    ranker = TfidfPaperRanker(papers)
    lines = [
        "# Labeling Candidate Pack",
        "",
        "These are candidate queries and likely matching papers from lexical search.",
        "They are not ground truth. Review the abstracts before copying IDs into labels.",
        "",
    ]

    for index, query in enumerate(SEED_QUERIES, start=1):
        lines.extend(
            [
                f"## Candidate {index:03d}",
                "",
                f"Query: {query}",
                "",
                "Likely paper IDs:",
                "",
            ]
        )
        for rank, (paper, score) in enumerate(ranker.rank(query, args.limit), start=1):
            abstract = paper.abstract[:700]
            if len(paper.abstract) > 700:
                abstract += "..."
            lines.extend(
                [
                    f"{rank}. `{paper.paper_id}` score={score:.4f}",
                    f"   Title: {paper.title}",
                    f"   Categories: {', '.join(paper.categories)}",
                    f"   Abstract: {abstract}",
                    "",
                ]
            )
        lines.append("")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote labeling candidates to {output}")


if __name__ == "__main__":
    main()
