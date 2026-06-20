from __future__ import annotations

from collections.abc import Sequence

import numpy as np

from arxiv_rag.schema import Paper


class TfidfPaperRanker:
    def __init__(self, papers: Sequence[Paper]):
        from sklearn.feature_extraction.text import TfidfVectorizer

        self.papers = list(papers)
        self.vectorizer = TfidfVectorizer(stop_words="english", max_features=50_000)
        self.matrix = self.vectorizer.fit_transform([paper_text(paper) for paper in self.papers])

    def rank(self, query: str, limit: int = 10) -> list[tuple[Paper, float]]:
        from sklearn.metrics.pairwise import cosine_similarity

        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix).ravel()
        ranked_indices = np.argsort(-scores)[:limit]
        return [(self.papers[index], float(scores[index])) for index in ranked_indices]


def rank_papers_tfidf(
    papers: Sequence[Paper],
    query: str,
    limit: int = 10,
) -> list[tuple[Paper, float]]:
    return TfidfPaperRanker(papers).rank(query, limit=limit)


def paper_text(paper: Paper) -> str:
    return f"{paper.title}\n{paper.abstract}"
