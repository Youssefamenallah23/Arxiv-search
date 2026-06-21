from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def load_dotenv(path: str | Path = ".env") -> None:
    env_path = Path(path)
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


load_dotenv()


@dataclass(frozen=True)
class Settings:
    wandb_project: str = os.getenv("WANDB_PROJECT", "arxiv-rag")
    qdrant_url: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    qdrant_collection: str = os.getenv("QDRANT_COLLECTION", "arxiv_abstract_chunks")
    gemini_api_key: str | None = os.getenv("GEMINI_API_KEY")


DEFAULT_EMBEDDING_MODELS = {
    "bge-small": "BAAI/bge-small-en-v1.5",
    "e5-small": "intfloat/e5-small-v2",
    "minilm": "sentence-transformers/all-MiniLM-L6-v2",
}

DEFAULT_RERANKER_MODEL = "BAAI/bge-reranker-base"
