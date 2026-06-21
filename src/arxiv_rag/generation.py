from __future__ import annotations

import time
from collections.abc import Sequence

from arxiv_rag.config import Settings

SYSTEM_PROMPT = """You are a research assistant that answers questions about AI/ML papers.

Rules:
- Answer based ONLY on the provided paper abstracts.
- Cite papers using [paper_id] whenever you reference a specific claim.
- If the abstracts do not contain enough information to answer a question, say so.
- Do not make up information that is not in the provided abstracts.
- Be concise and specific."""


def build_context(chunks: Sequence[dict]) -> str:
    sections = []
    for chunk in chunks:
        sections.append(f"[{chunk['paper_id']}] Title: {chunk['title']}\nAbstract: {chunk['text']}")
    return "\n\n".join(sections)


def _retry_request(
    client: object,
    model_name: str,
    user_message: str,
    system_prompt: str,
    max_retries: int = 5,
    base_delay: float = 5.0,
) -> object:
    import google.genai.errors as genai_errors

    last_exc = None
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model=model_name,
                contents=user_message,
                config={"system_instruction": system_prompt},
            )
        except (genai_errors.ServerError, genai_errors.ClientError) as exc:
            last_exc = exc
            sleep_secs = base_delay * (2**attempt)
            print(
                f"  API error ({exc.code}) "
                f"attempt {attempt + 1}/{max_retries}, "
                f"retrying in {sleep_secs:.0f}s...",
                end=" ",
                flush=True,
            )
            time.sleep(sleep_secs)
    raise RuntimeError(f"Gemini API request failed after {max_retries} retries") from last_exc


def generate_answer(
    query: str,
    chunks: Sequence[dict],
    model_name: str = "gemini-3.1-flash-lite",
    system_prompt: str = SYSTEM_PROMPT,
) -> tuple[str, float, dict]:
    import time

    from google import genai

    settings = Settings()
    client = genai.Client(api_key=settings.gemini_api_key)

    context = build_context(chunks)

    user_message = f"Context:\n{context}\n\nQuestion: {query}"

    started = time.perf_counter()
    response = _retry_request(client, model_name, user_message, system_prompt)
    elapsed = time.perf_counter() - started

    usage = {}
    if hasattr(response, "usage_metadata") and response.usage_metadata:
        usage = {
            "prompt_tokens": response.usage_metadata.prompt_token_count or 0,
            "completion_tokens": response.usage_metadata.candidates_token_count or 0,
            "total_tokens": response.usage_metadata.total_token_count or 0,
        }

    answer = response.text if hasattr(response, "text") else ""
    return answer, elapsed, usage
