import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from modules.theme import theme

st.markdown(theme(), unsafe_allow_html=True)

st.markdown("""
<style>
.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 0.6rem;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-bottom:0.2rem;">
    <div style="font-family:'DM Serif Display',serif; font-size:2rem; color:#f0faf6;">
        📊 Mood Trends
    </div>
    <div style="font-size:0.82rem; color:#475569; margin-top:0.1rem;">
        Visualize your emotional journey over time
    </div>
</div>
""", unsafe_allow_html=True)
st.divider()

# ── Color map ─────────────────────────────────────────────────────────────────
MOOD_COLORS = {
    "Joy":      "#fbbf24",
    "Sadness":  "#7dd3fc",
    "Fear":     "#a78bfa",
    "Anger":    "#fb7185",
    "Love":     "#f472b6",
    "Surprise": "#fb923c",
    "Neutral":  "#6ee7b7",
}

SAMPLE_DATA = [
    {"Date": "2026-02-19 09:00", "Score": 0.55, "Mood": "Neutral"},
    {"Date": "2026-02-20 14:30", "Score": 0.82, "Mood": "Joy"},
    {"Date": "2026-02-21 11:00", "Score": 0.35, "Mood": "Sadness"},
    {"Date": "2026-02-22 16:00", "Score": 0.60, "Mood": "Neutral"},
    {"Date": "2026-02-23 10:00", "Score": 0.91, "Mood": "Joy"},
    {"Date": "2026-02-24 20:00", "Score": 0.45, "Mood": "Fear"},
    {"Date": "2026-02-25 09:30", "Score": 0.78, "Mood": "Joy"},
]

# ── Determine data source ─────────────────────────────────────────────────────
# NEVER overwrite session_state with sample data.
# Real mood_data is only written by ai_engine.save_mood_entry().
real_data = st.session_state.get("mood_data", [])
using_sample = len(real_data) == 0

if using_sample:
    # Show sample for visual preview — DO NOT save to session_state
    display_data = SAMPLE_DATA
    st.markdown("""
    <div style="background:rgba(125,211,252,0.06); border:1px solid rgba(125,211,252,0.18);
                border-radius:12px; padding:0.75rem 1rem; font-size:0.8rem; color:#7dd3fc;
                margin-bottom:1rem;">
        📌 Showing <strong>sample data</strong> for preview.
        Chat with your companion to generate your real mood data!
    </div>
    """, unsafe_allow_html=True)
else:
    display_data = real_data  # ← always uses the latest real entries

# ── Build DataFrame ───────────────────────────────────────────────────────────
df = pd.DataFrame(display_data)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)

# ── Summary Metrics (always from the freshest row) ────────────────────────────
latest       = df.iloc[-1]          # most recent entry after sort
latest_mood  = latest["Mood"]
latest_score = latest["Score"]
avg_score    = df["Score"].mean()
best_mood    = df.loc[df["Score"].idxmax(), "Mood"]
total_logs   = len(df)

delta_str = "N/A"
if len(df) >= 2:
    delta_val = round((latest_score - df.iloc[0]["Score"]) * 100, 1)
    delta_str = f"{'+' if delta_val >= 0 else ''}{delta_val}%"

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Current Mood",    latest_mood,              delta=delta_str)
c2.metric("Latest Score",    f"{int(latest_score*100)}%")
c3.metric("Avg Well-being",  f"{int(avg_score*100)}%")
c4.metric("Best Mood",       best_mood)
c5.metric("Total Check-ins", str(total_logs))

st.divider()

# ── Well-being Line Chart ─────────────────────────────────────────────────────
st.markdown('<div class="section-label">Well-being Over Time</div>', unsafe_allow_html=True)

point_colors = [MOOD_COLORS.get(m, "#6ee7b7") for m in df["Mood"]]

fig_line = go.Figure()
fig_line.add_trace(go.Scatter(
    x=df["Date"], y=df["Score"],
    mode="lines+markers",
    line=dict(color="#6ee7b7", width=2.5, shape="spline"),
    marker=dict(size=9, color=point_colors, line=dict(color="#0b1120", width=2)),
    fill="tozeroy",
    fillcolor="rgba(110,231,183,0.06)",
    hovertemplate="<b>%{text}</b><br>%{x|%b %d, %H:%M}<br>Score: %{y:.0%}<extra></extra>",
    text=df["Mood"],
))
fig_line.update_layout(
    yaxis=dict(tickformat=".0%", range=[0, 1.08],
               gridcolor="rgba(255,255,255,0.04)",
               tickfont=dict(color="#475569", size=11)),
    xaxis=dict(gridcolor="rgba(255,255,255,0.04)",
               tickfont=dict(color="#475569", size=11)),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, t=10, b=0),
    height=280,
    hoverlabel=dict(bgcolor="#111827", font_color="#f0faf6", bordercolor="#6ee7b7"),
)
st.plotly_chart(fig_line, use_container_width=True)

# ── Pie + Bar side by side ────────────────────────────────────────────────────
col_pie, col_bar = st.columns(2)

with col_pie:
    st.markdown('<div class="section-label">Mood Distribution</div>', unsafe_allow_html=True)
    mood_counts = df["Mood"].value_counts().reset_index()
    mood_counts.columns = ["Mood", "Count"]
    fig_pie = px.pie(
        mood_counts, values="Count", names="Mood",
        color="Mood", color_discrete_map=MOOD_COLORS,
        hole=0.55,
    )
    fig_pie.update_traces(
        textfont=dict(color="#f0faf6", size=11),
        marker=dict(line=dict(color="#0b1120", width=2)),
    )
    fig_pie.update_layout(
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        showlegend=True,
        legend=dict(font=dict(color="#94a3b8", size=11), bgcolor="rgba(0,0,0,0)"),
        margin=dict(l=0, r=0, t=10, b=0),
        height=260,
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col_bar:
    st.markdown('<div class="section-label">Average Score by Mood</div>', unsafe_allow_html=True)
    avg_by_mood = df.groupby("Mood")["Score"].mean().reset_index()
    avg_by_mood.columns = ["Mood", "AvgScore"]
    avg_by_mood["Color"] = avg_by_mood["Mood"].map(lambda m: MOOD_COLORS.get(m, "#6ee7b7"))
    fig_bar = go.Figure(go.Bar(
        x=avg_by_mood["Mood"], y=avg_by_mood["AvgScore"],
        marker_color=avg_by_mood["Color"],
        marker_line=dict(color="#0b1120", width=1.5),
        text=[f"{int(s*100)}%" for s in avg_by_mood["AvgScore"]],
        textposition="outside",
        textfont=dict(color="#94a3b8", size=10),
    ))
    fig_bar.update_layout(
        yaxis=dict(tickformat=".0%", range=[0, 1.15],
                   gridcolor="rgba(255,255,255,0.04)",
                   tickfont=dict(color="#475569", size=10)),
        xaxis=dict(tickfont=dict(color="#94a3b8", size=11)),
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=20, b=0),
        height=260,
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ── Raw Data ──────────────────────────────────────────────────────────────────
with st.expander("🗂️ Raw Mood Data"):
    display_df = df.copy()
    display_df["Score"] = display_df["Score"].apply(lambda x: f"{int(x*100)}%")
    display_df["Date"]  = display_df["Date"].dt.strftime("%Y-%m-%d %H:%M")
    # Show newest first
    st.dataframe(display_df[::-1].reset_index(drop=True), use_container_width=True)

# ── Clear button (only show for real data) ────────────────────────────────────
if not using_sample:
    st.markdown("<br>", unsafe_allow_html=True)
    col_clr, _ = st.columns([1, 4])
    with col_clr:
        if st.button("🗑️ Clear All Data"):
            st.session_state.mood_data = []
            st.rerun()