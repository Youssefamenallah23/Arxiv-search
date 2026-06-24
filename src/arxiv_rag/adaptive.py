from __future__ import annotations

import time
from collections.abc import Sequence

from arxiv_rag.config import Settings
from arxiv_rag.schema import Chunk

ADAPTIVE_SYSTEM_PROMPT = (
    "You are a retrieval quality checker. Given a research question "
    "and a set of retrieved paper chunks, determine whether the chunks "
    "contain enough information to answer the question.\n\n"
    "If the chunks are sufficient, respond with exactly:\n"
    "SUFFICIENT\n\n"
    "If the chunks are NOT sufficient, respond with exactly:\n"
    "REFORMULATE: <a better, more specific version of the query>\n\n"
    "Rules:\n"
    "- Be strict: if key information is missing, say REFORMULATE.\n"
    "- The new query should be more specific or use different keywords.\n"
    "- Do NOT include any other text."
)


def _llm_check(
    query: str,
    chunks: Sequence[Chunk],
    model_name: str = "gemini-3.1-flash-lite",
    max_retries: int = 5,
    base_delay: float = 4.0,
) -> tuple[bool, str | None]:
    from google import genai
    import google.genai.errors as genai_errors

    settings = Settings()
    client = genai.Client(api_key=settings.gemini_api_key)

    context_parts = []
    for chunk in chunks[:5]:
        context_parts.append(f"[{chunk.paper_id}] {chunk.title}: {chunk.text[:300]}")
    context = "\n\n".join(context_parts)

    user_message = f"Question: {query}\n\nRetrieved chunks:\n{context}"

    last_exc = None
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=user_message,
                config={"system_instruction": ADAPTIVE_SYSTEM_PROMPT},
            )
            text = response.text.strip() if hasattr(response, "text") else ""
            if text.startswith("SUFFICIENT"):
                return True, None
            if text.startswith("REFORMULATE:"):
                new_query = text[len("REFORMULATE:") :].strip()
                if new_query and new_query.lower() != query.lower():
                    return False, new_query
            return True, None
        except (genai_errors.ServerError, genai_errors.ClientError) as exc:
            last_exc = exc
            import time as _time

            sleep_secs = base_delay * (2**attempt)
            print(
                f"  LLM check ({exc.code}) "
                f"attempt {attempt + 1}/{max_retries}, "
                f"retrying in {sleep_secs:.0f}s...",
                end=" ",
                flush=True,
            )
            _time.sleep(sleep_secs)

    print(f"  LLM check failed after {max_retries} retries, assuming sufficient")
    return True, None
    if text.startswith("REFORMULATE:"):
        new_query = text[len("REFORMULATE:") :].strip()
        if new_query and new_query.lower() != query.lower():
            return False, new_query
    return True, None


class AdaptiveRetriever:
    def __init__(self, base_retriever: object, chunks: Sequence[Chunk]):
        self.base = base_retriever
        self.chunk_by_id = {c.chunk_id: c for c in chunks}

    def retrieve(self, query: str, top_k: int) -> tuple[list[Chunk], dict]:
        metadata = {
            "reformulated": False,
            "original_query": query,
            "reformulated_query": None,
            "trigger_reason": None,
            "round1_time": 0.0,
            "round2_time": 0.0,
        }

        t0 = time.perf_counter()
        round1 = self._retrieve_core(query, top_k)
        metadata["round1_time"] = time.perf_counter() - t0

        t0 = time.perf_counter()
        sufficient, new_query = _llm_check(query, round1)
        check_time = time.perf_counter() - t0

        if sufficient or new_query is None:
            return round1, metadata

        metadata["reformulated"] = True
        metadata["reformulated_query"] = new_query
        metadata["trigger_reason"] = "llm_insufficient"

        t0 = time.perf_counter()
        round2 = self._retrieve_core(new_query, top_k)
        metadata["round2_time"] = time.perf_counter() - t0
        metadata["check_time"] = check_time

        merged = self._merge_rounds(round1, round2, top_k)
        return merged, metadata

    def _retrieve_core(self, query: str, top_k: int) -> list[Chunk]:
        if hasattr(self.base, "retrieve"):
            return self.base.retrieve(query, top_k)
        raise TypeError("base_retriever must have a retrieve method")

    @staticmethod
    def _merge_rounds(
        round1: list[Chunk],
        round2: list[Chunk],
        top_k: int,
        rrf_k: int = 60,
    ) -> list[Chunk]:
        from arxiv_rag.retrieval import hybrid_fusion

        return hybrid_fusion(round1, round2, top_k, rrf_k)
