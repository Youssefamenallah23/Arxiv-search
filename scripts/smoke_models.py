from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.config import DEFAULT_EMBEDDING_MODELS, DEFAULT_RERANKER_MODEL
from arxiv_rag.embeddings import CrossEncoderReranker, SentenceTransformerEncoder


def main() -> None:
    parser = argparse.ArgumentParser(description="Download and smoke-test retrieval models.")
    parser.add_argument("--models", nargs="+", default=list(DEFAULT_EMBEDDING_MODELS.keys()))
    parser.add_argument("--skip-reranker", action="store_true")
    args = parser.parse_args()

    documents = [
        "Retrieval augmented generation grounds language model answers in retrieved evidence.",
        "Diffusion models can synthesize images and 3D assets from text prompts.",
    ]
    queries = ["RAG for evidence grounded question answering"]

    for key in args.models:
        model_name = DEFAULT_EMBEDDING_MODELS.get(key, key)
        encoder = SentenceTransformerEncoder(model_name)
        doc_vectors, doc_seconds = encoder.encode_documents(documents, batch_size=2)
        query_vectors, query_seconds = encoder.encode_queries(queries, batch_size=1)
        similarity = query_vectors @ doc_vectors.T
        print(
            f"{key}: docs={doc_vectors.shape}, queries={query_vectors.shape}, "
            f"top_doc={int(similarity.argmax())}, "
            f"doc_seconds={doc_seconds:.2f}, query_seconds={query_seconds:.2f}"
        )

    if not args.skip_reranker:
        reranker = CrossEncoderReranker(DEFAULT_RERANKER_MODEL)
        ranked_ids, rerank_seconds = reranker.rerank(
            queries[0],
            [(f"doc-{index}", text) for index, text in enumerate(documents)],
            batch_size=2,
        )
        print(f"reranker: ranked_ids={ranked_ids}, seconds={rerank_seconds:.2f}")


if __name__ == "__main__":
    main()
