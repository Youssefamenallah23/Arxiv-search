from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="ArXiv RAG Dashboard", layout="wide")

_HERE = Path(__file__).resolve().parent.parent
DATA_PATH = str(_HERE / "reports" / "eval_test_generation.jsonl")
COST_PER_PROMPT_TOKEN = 0.0
COST_PER_COMPLETION_TOKEN = 0.0

st.title("ArXiv RAG Evaluation Dashboard")
st.caption(
    "Performance metrics across 25 test-set queries (bge-small → bge-reranker-base → gemini-3.1-flash-lite)"
)


@st.cache_data
def load_data() -> pd.DataFrame:
    rows = []
    with open(DATA_PATH) as f:
        for line in f:
            rows.append(json.loads(line))
    df = pd.json_normalize(rows)
    df = df.rename(
        columns={
            "query": "query",
            "retrieval.recall@5": "recall@5",
            "retrieval.recall@10": "recall@10",
            "retrieval.mrr": "mrr",
            "retrieval.ndcg@10": "ndcg@10",
            "generation.faithfulness": "faithfulness",
            "generation.citation_accuracy": "citation_accuracy",
            "generation.completeness": "completeness",
            "generation.latency_seconds": "latency",
            "generation.llm_usage.prompt_tokens": "prompt_tokens",
            "generation.llm_usage.completion_tokens": "completion_tokens",
            "generation.llm_usage.total_tokens": "total_tokens",
        }
    )
    return df


df = load_data()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Recall@10", f"{df['recall@10'].mean():.3f}")
col2.metric("MRR", f"{df['mrr'].mean():.3f}")
col3.metric("Faithfulness", f"{df['faithfulness'].mean():.3f}")
col4.metric("Citation Accuracy", f"{df['citation_accuracy'].mean():.3f}")
col5.metric("Avg Latency", f"{df['latency'].mean():.1f}s")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Retrieval Metrics",
        "Generation Metrics",
        "Latency Breakdown",
        "Cost Analysis",
        "Failure Analysis",
    ]
)

with tab1:
    st.subheader("Retrieval Metrics (Test Set, 25 queries)")

    avg_retrieval = pd.DataFrame(
        {
            "Metric": ["Recall@5", "Recall@10", "MRR", "NDCG@10"],
            "Score": [
                df["recall@5"].mean(),
                df["recall@10"].mean(),
                df["mrr"].mean(),
                df["ndcg@10"].mean(),
            ],
        }
    ).set_index("Metric")
    st.bar_chart(avg_retrieval, height=350)

    st.subheader("Per-Query Recall@10")
    scatter_df = df[["query", "recall@10"]].copy()
    scatter_df["query_short"] = scatter_df["query"].str[:40]
    st.scatter_chart(scatter_df, x="query_short", y="recall@10", height=350)

    with st.expander("Raw retrieval data"):
        st.dataframe(
            df[["query", "recall@5", "recall@10", "mrr", "ndcg@10"]]
            .style.highlight_min(color="#ffcccc")
            .highlight_max(color="#ccffcc"),
            use_container_width=True,
        )

with tab2:
    st.subheader("Generation Metrics")

    col_a, col_b = st.columns(2)
    with col_a:
        st.caption("Faithfulness Distribution")
        faith_bins = pd.cut(df["faithfulness"], bins=[0, 0.25, 0.5, 0.75, 1.0], right=True)
        faith_counts = faith_bins.value_counts().sort_index()
        faith_counts.index = faith_counts.index.astype(str)
        st.bar_chart(faith_counts, height=250)

    with col_b:
        st.caption("Citation Accuracy Distribution")
        cite_bins = pd.cut(df["citation_accuracy"], bins=[0, 0.25, 0.5, 0.75, 1.0], right=True)
        cite_counts = cite_bins.value_counts().sort_index()
        cite_counts.index = cite_counts.index.astype(str)
        st.bar_chart(cite_counts, height=250)

    st.caption("Completeness Scores")
    comp_counts = df["completeness"].value_counts().sort_index()
    comp_counts.index = comp_counts.index.astype(str)
    st.bar_chart(comp_counts, height=250)

    with st.expander("Low-scoring queries"):
        low_faith = df[df["faithfulness"] < 1.0][["query", "faithfulness", "citation_accuracy"]]
        if not low_faith.empty:
            st.dataframe(low_faith, use_container_width=True)
        else:
            st.info("All queries have perfect faithfulness.")

    with st.expander("Raw generation data"):
        st.dataframe(
            df[
                [
                    "query",
                    "faithfulness",
                    "citation_accuracy",
                    "completeness",
                    "latency",
                    "total_tokens",
                ]
            ],
            use_container_width=True,
        )

with tab3:
    st.subheader("Latency Breakdown by Query")

    latency_df = df[["query", "latency"]].copy()
    latency_df["query_short"] = latency_df["query"].str[:50]
    latency_df = latency_df.sort_values("latency", ascending=False)

    st.caption("Generation latency (Gemini API call) per query")
    st.bar_chart(latency_df.set_index("query_short")["latency"], height=400)

    st.subheader("Aggregate Latency")
    total_time = df["latency"].sum()
    avg_time = df["latency"].mean()
    col_x, col_y, col_z = st.columns(3)
    col_x.metric("Total Generation Time", f"{total_time:.1f}s")
    col_y.metric("Average per Query", f"{avg_time:.2f}s")
    col_z.metric("Fastest / Slowest", f"{df['latency'].min():.1f}s / {df['latency'].max():.1f}s")

    st.caption(
        "Note: Retrieval (~0.025s) and reranking (~10s) are measured in the API but the eval data only captures generation latency."
    )

with tab4:
    st.subheader("Token Usage & Cost Estimate")

    total_prompt = df["prompt_tokens"].sum()
    total_completion = df["completion_tokens"].sum()
    total_tokens = df["total_tokens"].sum()

    col_p, col_c, col_t = st.columns(3)
    col_p.metric("Total Prompt Tokens", f"{total_prompt:,}")
    col_c.metric("Total Completion Tokens", f"{total_completion:,}")
    col_t.metric("Total Tokens", f"{total_tokens:,}")

    st.caption("Per-Query Token Usage")
    token_df = df[["query", "prompt_tokens", "completion_tokens"]].copy()
    token_df["query_short"] = token_df["query"].str[:50]
    st.bar_chart(token_df.set_index("query_short"), height=400)

    st.subheader("Cost Breakdown")
    st.markdown("""
    | Component | Cost Type | Rate | Per Query | 25 Queries |
    |---|---|---|---|---|
    | Embedding (bge-small) | Amortized compute | $0.1664/hr (t3.xlarge) | ~$0.0017 | ~$0.04 |
    | Reranking (bge-reranker-base) | Amortized compute | included above | — | — |
    | Gemini 3.1 Flash Lite | Metered API | Free tier: 500 RPD | $0 (free tier) | $0 |
    | **Total** | | | **~$0.002** | **~$0.04** |
    """)

    st.caption("Token Efficiency")
    token_df["tokens_per_query"] = token_df["prompt_tokens"] + token_df["completion_tokens"]
    st.metric("Avg Tokens per Query", f"{token_df['tokens_per_query'].mean():.0f}")

with tab5:
    st.subheader("Failure Analysis Summary")

    st.markdown("### Retrieval Failures")
    st.markdown(f"- **{6}/25 (24%)** queries have recall@10 ≤ 0.2")
    st.markdown(f"- **{8}/25 (32%)** queries have MRR < 0.5")
    st.markdown(f"- **{3}/25 (12%)** queries have recall@10 = 0.1")
    st.markdown(
        "**Root cause:** Labels derived from TF-IDF, retrieval uses dense embeddings — different relevance signals."
    )

    low_recall = df[df["recall@10"] <= 0.2][["query", "recall@10", "mrr"]].copy()
    st.dataframe(low_recall, use_container_width=True)

    st.markdown("### Generation Failures")
    st.markdown("**Citation Accuracy:**")
    low_cite = df[df["citation_accuracy"] < 1.0][["query", "citation_accuracy"]]
    if not low_cite.empty:
        st.dataframe(low_cite, use_container_width=True)
        st.markdown(
            "**Fix:** Already applied — citation extraction now handles comma-separated IDs."
        )
    else:
        st.success("No citation accuracy failures.")

    st.markdown("**Faithfulness:**")
    st.markdown("""
    - 3 false positives from "no information" answers
    - 3 lead-sentence enumeration penalties
    - 1 actual hallucination (test-007)
    """)

    st.markdown("**Completeness:**")
    st.markdown(
        f"- **{((df['completeness'] == 1).sum())}/25** scored 1/5 (floor) — naive substring scorer"
    )
    st.markdown(f"- **{((df['completeness'] == 5).sum())}/25** scored 5/5")

    with st.expander("Full failure analysis report"):
        from pathlib import Path

        report_path = Path("reports/failure_analysis_2026-06-20.md")
        if report_path.exists():
            st.markdown(report_path.read_text(encoding="utf-8"))
