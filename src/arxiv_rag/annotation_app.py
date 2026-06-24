from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse

from arxiv_rag.annotation import LabelPayload, LabelStore


def create_app(
    corpus_path: str | Path = "data/raw/arxiv_corpus_2026-06-19.jsonl",
    labels_path: str | Path = "docs/eval/query_labels_2026-06-19.jsonl",
) -> FastAPI:
    app = FastAPI(title="ArXiv RAG Labeler")
    store = LabelStore(corpus_path=corpus_path, labels_path=labels_path)

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return LABELER_HTML

    @app.get("/api/status")
    def status() -> dict[str, object]:
        return store.status()

    @app.get("/api/labels")
    def labels() -> list[dict[str, object]]:
        return [label.model_dump() for label in store.list_labels()]

    @app.get("/api/search")
    def search(q: str = Query(min_length=2), limit: int = 10) -> list[dict[str, object]]:
        return store.search(q, limit=limit)

    @app.post("/api/labels")
    def add_label(payload: LabelPayload) -> dict[str, object]:
        try:
            label = store.add_label(payload)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return label.model_dump()

    @app.delete("/api/labels/{query_id}")
    def delete_label(query_id: str) -> dict[str, object]:
        deleted = store.delete_label(query_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="query_id not found")
        return {"deleted": query_id}

    return app


app = create_app()


LABELER_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ArXiv RAG Labeler</title>
  <style>
    :root {
      color-scheme: light;
      --bg: #f6f7f9;
      --panel: #ffffff;
      --ink: #17202a;
      --muted: #607085;
      --line: #d8dee8;
      --accent: #0f766e;
      --danger: #b42318;
      --soft: #e8f3f1;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Inter, Segoe UI, system-ui, sans-serif;
      background: var(--bg);
      color: var(--ink);
    }
    header {
      position: sticky;
      top: 0;
      z-index: 2;
      background: var(--panel);
      border-bottom: 1px solid var(--line);
      padding: 14px 22px;
      display: flex;
      justify-content: space-between;
      gap: 16px;
      align-items: center;
    }
    h1 { font-size: 18px; margin: 0; }
    main {
      display: grid;
      grid-template-columns: minmax(360px, 470px) minmax(0, 1fr);
      gap: 16px;
      padding: 16px;
    }
    section {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
    }
    label {
      display: block;
      color: var(--muted);
      font-size: 13px;
      margin: 12px 0 6px;
    }
    input, textarea, select {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 9px 10px;
      font: inherit;
      background: white;
    }
    textarea { min-height: 86px; resize: vertical; }
    button {
      border: 1px solid var(--accent);
      background: var(--accent);
      color: white;
      border-radius: 6px;
      padding: 9px 12px;
      font: inherit;
      cursor: pointer;
    }
    button.secondary {
      background: white;
      color: var(--accent);
    }
    button.danger {
      border-color: var(--danger);
      color: var(--danger);
      background: white;
    }
    .row { display: flex; gap: 8px; align-items: center; }
    .row > * { flex: 1; }
    .status {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 13px;
      color: var(--muted);
    }
    .pill {
      padding: 5px 8px;
      background: var(--soft);
      color: #115e59;
      border-radius: 999px;
    }
    .paper {
      border-top: 1px solid var(--line);
      padding: 13px 0;
    }
    .paper:first-child { border-top: 0; }
    .paper h3 {
      font-size: 15px;
      margin: 0 0 6px;
      line-height: 1.35;
    }
    .meta {
      color: var(--muted);
      font-size: 12px;
      margin-bottom: 8px;
    }
    .abstract {
      font-size: 13px;
      line-height: 1.5;
      color: #2f3b4a;
    }
    .selected {
      margin-top: 10px;
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .selected span {
      background: #eef2ff;
      border: 1px solid #c7d2fe;
      color: #3730a3;
      padding: 5px 8px;
      border-radius: 999px;
      font-size: 12px;
    }
    .error { color: var(--danger); font-size: 13px; white-space: pre-wrap; }
    .labels-list {
      max-height: 260px;
      overflow: auto;
      border-top: 1px solid var(--line);
      margin-top: 12px;
    }
    .label-item {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 8px;
      padding: 8px 0;
      border-bottom: 1px solid var(--line);
      font-size: 13px;
    }
    @media (max-width: 860px) {
      main { grid-template-columns: 1fr; }
      header { align-items: flex-start; flex-direction: column; }
    }
  </style>
</head>
<body>
  <header>
    <h1>ArXiv RAG Labeler</h1>
    <div id="status" class="status"></div>
  </header>
  <main>
    <section>
      <label for="query">Research question</label>
      <textarea id="query" placeholder="Which recent papers use retrieval-augmented generation for factual question answering?"></textarea>
      <div class="row" style="margin-top: 8px;">
        <button onclick="search()">Search Papers</button>
        <button class="secondary" onclick="clearSelection()">Clear Selection</button>
      </div>

      <label for="split">Split</label>
      <select id="split">
        <option value="train">train</option>
        <option value="validation">validation</option>
        <option value="test">test</option>
      </select>

      <label>Selected relevant paper IDs</label>
      <div id="selected" class="selected"></div>

      <label for="notes">Notes</label>
      <textarea id="notes" placeholder="Why these abstracts are relevant."></textarea>

      <div class="row" style="margin-top: 8px;">
        <button onclick="saveLabel()">Save Label</button>
        <button class="secondary" onclick="loadLabels()">Refresh Labels</button>
      </div>
      <p id="message" class="error"></p>

      <div class="labels-list" id="labels"></div>
    </section>

    <section>
      <div id="results"></div>
    </section>
  </main>

<script>
const selected = new Set();

async function api(path, options) {
  const response = await fetch(path, options);
  if (!response.ok) {
    const text = await response.text();
    throw new Error(text);
  }
  return await response.json();
}

async function loadStatus() {
  const data = await api('/api/status');
  const status = document.getElementById('status');
  status.innerHTML = '';
  for (const [split, item] of Object.entries(data.progress)) {
    const pill = document.createElement('span');
    pill.className = 'pill';
    pill.textContent = `${split}: ${item.actual}/${item.expected}`;
    status.appendChild(pill);
  }
  if (data.errors.length) {
    const pill = document.createElement('span');
    pill.className = 'pill';
    pill.textContent = `${data.errors.length} validation issues`;
    status.appendChild(pill);
  }
}

async function search() {
  const query = document.getElementById('query').value.trim();
  if (!query) return;
  document.getElementById('message').textContent = '';
  const papers = await api(`/api/search?q=${encodeURIComponent(query)}&limit=15`);
  const results = document.getElementById('results');
  results.innerHTML = '';
  papers.forEach((paper, index) => {
    const item = document.createElement('div');
    item.className = 'paper';
    item.innerHTML = `
      <h3>${index + 1}. ${escapeHtml(paper.title)}</h3>
      <div class="meta">${paper.paper_id} | score=${paper.score.toFixed(4)} | ${paper.categories.join(', ')}</div>
      <div class="abstract">${escapeHtml(paper.abstract)}</div>
      <div style="margin-top: 8px;"><button class="secondary">Toggle Relevant</button></div>
    `;
    item.querySelector('button').onclick = () => togglePaper(paper.paper_id);
    results.appendChild(item);
  });
}

function togglePaper(paperId) {
  if (selected.has(paperId)) selected.delete(paperId);
  else selected.add(paperId);
  renderSelected();
}

function clearSelection() {
  selected.clear();
  renderSelected();
}

function renderSelected() {
  const node = document.getElementById('selected');
  node.innerHTML = '';
  [...selected].forEach(id => {
    const item = document.createElement('span');
    item.textContent = id;
    node.appendChild(item);
  });
}

async function saveLabel() {
  const payload = {
    split: document.getElementById('split').value,
    query: document.getElementById('query').value.trim(),
    relevant_paper_ids: [...selected],
    notes: document.getElementById('notes').value.trim(),
  };
  try {
    const label = await api('/api/labels', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload),
    });
    document.getElementById('message').textContent = `Saved ${label.query_id}`;
    clearSelection();
    await loadStatus();
    await loadLabels();
  } catch (error) {
    document.getElementById('message').textContent = error.message;
  }
}

async function loadLabels() {
  const labels = await api('/api/labels');
  const list = document.getElementById('labels');
  list.innerHTML = '';
  labels.slice().reverse().forEach(label => {
    const item = document.createElement('div');
    item.className = 'label-item';
    item.innerHTML = `
      <div><strong>${label.query_id}</strong> ${escapeHtml(label.query)}<br>${label.relevant_paper_ids.join(', ')}</div>
      <button class="danger">Delete</button>
    `;
    item.querySelector('button').onclick = async () => {
      await api(`/api/labels/${label.query_id}`, {method: 'DELETE'});
      await loadStatus();
      await loadLabels();
    };
    list.appendChild(item);
  });
}

function escapeHtml(value) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

loadStatus();
loadLabels();
</script>
</body>
</html>
"""
