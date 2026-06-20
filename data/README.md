# Data Directory

- `raw/`: immutable dated arXiv corpus snapshots.
- `processed/`: derived artifacts such as chunk JSONL files or experiment outputs.
- `qdrant_db/`: persistent Qdrant vector store (SQLite-backed, created by `QdrantIndexer`, auto-detected by FastAPI).
  - ~27 MB for 5,000 papers with 384-dim bge-small embeddings.
  - Contains `.lock` (concurrency guard), `meta.json` (collection metadata), and `collection/*/storage.sqlite`.
  - Safe to delete and re-index. Ignored by `.gitignore`.

Do not commit large JSONL snapshots. Record their filenames in experiment configs and reports.
