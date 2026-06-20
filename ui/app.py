from __future__ import annotations

import sys
import time
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arxiv_rag.chunking import chunk_papers, proportional_overlap
from arxiv_rag.config import DEFAULT_EMBEDDING_MODELS
from arxiv_rag.embeddings import SentenceTransformerEncoder, CrossEncoderReranker
from arxiv_rag.generation import generate_answer
from arxiv_rag.labels import load_papers


CORPUS_PATH = "data/raw/arxiv_corpus_2026-06-19.jsonl"
CHUNK_SIZE = 512
TOP_K_CHUNKS = 50
TOP_K_PAPERS = 10
CONTEXT_BUDGET = 5


@st.cache_resource
def load_pipeline():
    papers = load_papers(CORPUS_PATH)
    overlap = proportional_overlap(CHUNK_SIZE)
    chunks = chunk_papers(papers, chunk_size=CHUNK_SIZE, overlap=overlap)
    chunk_by_id = {chunk.chunk_id: chunk for chunk in chunks}
    encoder = SentenceTransformerEncoder(
        DEFAULT_EMBEDDING_MODELS.get("bge-small", "BAAI/bge-small-en-v1.5")
    )
    chunk_texts = [chunk.text for chunk in chunks]
    chunk_vectors, embed_sec = encoder.encode_documents(chunk_texts)

    reranker = CrossEncoderReranker("BAAI/bge-reranker-base")

    return {
        "papers": papers,
        "chunks": chunks,
        "chunk_by_id": chunk_by_id,
        "encoder": encoder,
        "chunk_vectors": chunk_vectors,
        "reranker": reranker,
    }


def search(pipeline, query: str, top_k_chunks: int, context_budget: int):
    encoder = pipeline["encoder"]
    chunk_vectors = pipeline["chunk_vectors"]
    chunks = pipeline["chunks"]
    chunk_by_id = pipeline["chunk_by_id"]
    reranker = pipeline["reranker"]

    t0 = time.perf_counter()
    query_vector, _ = encoder.encode_queries([query])
    scores = query_vector @ chunk_vectors.T
    top_indices = scores[0].argsort()[::-1][:top_k_chunks]
    ranked_chunks = [chunks[i] for i in top_indices]
    retrieval_sec = time.perf_counter() - t0

    t0 = time.perf_counter()
    candidates = [(chunk.chunk_id, chunk.text) for chunk in ranked_chunks]
    ranked_chunk_ids, _ = reranker.rerank(query, candidates)
    reranked_chunks = [chunk_by_id[cid] for cid in ranked_chunk_ids]
    rerank_sec = time.perf_counter() - t0

    budget = reranked_chunks[:context_budget]
    chunk_dicts = [
        {"chunk_id": c.chunk_id, "paper_id": c.paper_id, "title": c.title, "text": c.text}
        for c in budget
    ]

    return chunk_dicts, retrieval_sec, rerank_sec


st.set_page_config(
    page_title="ArXiv RAG",
    page_icon="📄",
    layout="wide",
)

st.title("📄 ArXiv Research Assistant")
st.markdown(
    "Ask questions about AI/ML papers from the ArXiv corpus. "
    "Answers are generated from paper abstracts using "
    "bge-small embeddings + bge-reranker + Gemini 3.1 Flash Lite."
)

with st.sidebar:
    st.header("About")
    st.markdown(
        "**Corpus:** 5,000 AI/ML papers from arXiv (title + abstract)\n\n"
        "**Pipeline:** bge-small → bge-reranker-base → gemini-3.1-flash-lite\n\n"
        "**Evaluation:** Recall@10=0.332, Faithfulness=0.932, "
        "Citation Acc=0.950\n\n"
        "[View full report](../reports/README.md)"
    )

    with st.expander("Settings"):
        show_evidence = st.checkbox("Show retrieved abstracts", value=True)
        top_k = st.slider("Top-K chunks", 10, 100, TOP_K_CHUNKS)
        context = st.slider("Context budget", 1, 10, CONTEXT_BUDGET)

st.info("Loading pipeline (corpus, embeddings, reranker) — this takes ~6 minutes on CPU...")
with st.spinner("Loading..."):
    pipeline = load_pipeline()
st.success("Pipeline loaded!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "evidence" in msg and msg["evidence"]:
            with st.expander("View evidence"):
                for c in msg["evidence"]:
                    st.markdown(f"**[{c['paper_id']}] {c['title']}**")
                    st.text(c["text"][:400] + ("..." if len(c["text"]) > 400 else ""))

if prompt := st.chat_input("Ask a question about AI/ML papers..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("_Searching corpus..._")

        try:
            chunk_dicts, retrieval_sec, rerank_sec = search(
                pipeline, prompt, top_k_chunks=top_k, context_budget=context
            )

            placeholder.markdown("_Generating answer with Gemini..._")
            answer, gen_sec, usage = generate_answer(
                query=prompt,
                chunks=chunk_dicts,
            )
            total = retrieval_sec + rerank_sec + gen_sec

            answer_text = f"{answer}\n\n---\n"
            answer_text += f"🕒 {total:.1f}s total (retrieval {retrieval_sec:.1f}s"
            answer_text += f" · rerank {rerank_sec:.1f}s · gen {gen_sec:.1f}s)"
            if usage:
                answer_text += f" · tokens: {usage.get('total_tokens', 0)}"
            placeholder.markdown(answer_text)

            evidence_list = None
            if show_evidence:
                with st.expander(f"View evidence ({len(chunk_dicts)} chunks)", expanded=False):
                    for c in chunk_dicts:
                        st.markdown(f"**[{c['paper_id']}] {c['title']}**")
                        st.text(c["text"][:400] + ("..." if len(c["text"]) > 400 else ""))
                    evidence_list = chunk_dicts

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer_text,
                    "evidence": evidence_list if show_evidence else None,
                }
            )

        except Exception as exc:
            placeholder.error(f"Error: {exc}")
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": f"Error: {exc}",
                }
            )
