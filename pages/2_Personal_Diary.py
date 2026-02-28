"""
SunnyAura — Personal Diary Page
"""

import streamlit as st
import json
import os
import hashlib
from datetime import datetime

from modules.theme import theme

st.markdown(theme(), unsafe_allow_html=True)

st.markdown("""
<style>
.diary-header {
    margin-bottom: 0.2rem;
}
.diary-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem;
    color: #f0faf6;
}
.lock-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: rgba(251,191,36,0.08);
    border: 1px solid rgba(251,191,36,0.2);
    border-radius: 99px;
    padding: 0.2rem 0.75rem;
    font-size: 0.73rem;
    color: #fbbf24;
    font-weight: 500;
    margin-bottom: 1rem;
}
.entry-count {
    font-size: 0.75rem;
    color: #475569;
    letter-spacing: 0.04em;
}
.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 0.8rem;
    margin-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

DIARY_FILE   = "data/diary_entries.json"
CORRECT_HASH = hashlib.sha256("1234".encode()).hexdigest()
os.makedirs("data", exist_ok=True)

def load_entries() -> list:
    if os.path.exists(DIARY_FILE):
        try:
            with open(DIARY_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def save_entries(entries: list) -> None:
    with open(DIARY_FILE, "w") as f:
        json.dump(entries, f, indent=2)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="background:rgba(251,191,36,0.06); border:1px solid rgba(251,191,36,0.15);
                border-radius:10px; padding:0.8rem 1rem; font-size:0.78rem; color:#94a3b8;">
        🔒 Your diary entries are password protected and stored locally.
    </div>
    """, unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="diary-header">
    <div class="diary-title">📓 Personal Diary</div>
</div>
<div class="lock-badge">🔐 Password protected · Private</div>
""", unsafe_allow_html=True)

# ── Auth ──────────────────────────────────────────────────────────────────────
key = st.text_input("Security key", type="password", placeholder="Enter your diary password…",
                    label_visibility="collapsed")

if not key:
    st.markdown("""
    <div style="text-align:center; padding:2rem 1rem; color:#475569;">
        <div style="font-size:2rem; margin-bottom:0.5rem;">🔒</div>
        <div style="font-size:0.88rem;">Enter your security key above to access your diary.</div>
        <div style="font-size:0.75rem; color:#374151; margin-top:0.3rem;">Default key: 1234</div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

if hashlib.sha256(key.encode()).hexdigest() != CORRECT_HASH:
    st.error("Incorrect key. Please try again.")
    st.stop()

st.markdown("""
<div style="display:inline-flex; align-items:center; gap:0.4rem;
            background:rgba(110,231,183,0.07); border:1px solid rgba(110,231,183,0.18);
            border-radius:99px; padding:0.25rem 0.8rem;
            font-size:0.75rem; color:#6ee7b7; font-weight:500; margin-bottom:0.5rem;">
    ✓ Access granted — welcome back
</div>
""", unsafe_allow_html=True)
st.divider()

# ── New Entry ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">New Entry</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    entry_title = st.text_input("Title", placeholder="Give your entry a title…", label_visibility="collapsed")
with col2:
    mood_tag = st.selectbox(
        "Mood",
        ["😊 Happy", "😢 Sad", "😰 Anxious", "😡 Angry", "😌 Calm", "🤔 Reflective", "😴 Tired"],
        label_visibility="collapsed",
    )

entry_text = st.text_area(
    "Write here",
    height=160,
    placeholder="What's on your mind today? This is your private space…",
    label_visibility="collapsed",
)

col_btn, col_hint = st.columns([1, 4])
with col_btn:
    save_clicked = st.button("Save Entry", use_container_width=True)
with col_hint:
    st.markdown('<span style="font-size:0.75rem; color:#374151;">Your entry is stored locally & encrypted.</span>', unsafe_allow_html=True)

if save_clicked:
    if not entry_text.strip():
        st.warning("Write something before saving.")
    else:
        entries = load_entries()
        new_entry = {
            "id":      len(entries) + 1,
            "date":    datetime.now().strftime("%Y-%m-%d %H:%M"),
            "title":   entry_title.strip() or "Untitled",
            "mood":    mood_tag,
            "content": entry_text.strip(),
        }
        entries.append(new_entry)
        save_entries(entries)
        st.toast("Entry saved!", icon="📓")
        st.rerun()

st.divider()

# ── Past Entries ──────────────────────────────────────────────────────────────
entries = load_entries()

col_left, col_right = st.columns([3, 2])
with col_left:
    st.markdown('<div class="section-label">Past Entries</div>', unsafe_allow_html=True)
with col_right:
    search_query = st.text_input("Search", placeholder="🔍 Search by title or content…",
                                 label_visibility="collapsed")

if not entries:
    st.markdown("""
    <div style="text-align:center; padding:2rem 1rem; color:#475569;">
        <div style="font-size:1.8rem; margin-bottom:0.5rem;">📝</div>
        <div style="font-size:0.85rem;">No entries yet. Write your first one above.</div>
    </div>
    """, unsafe_allow_html=True)
else:
    filtered = list(reversed(entries))
    if search_query:
        q = search_query.lower()
        filtered = [
            e for e in filtered
            if q in e.get("title", "").lower() or q in e["content"].lower()
        ]

    st.markdown(f'<div class="entry-count">Showing {len(filtered)} of {len(entries)} entries</div>',
                unsafe_allow_html=True)

    for entry in filtered:
        label = f"{entry['mood']}  ·  {entry['date']}  ·  **{entry.get('title', 'Untitled')}**"
        with st.expander(label):
            st.markdown(f'<div style="font-size:0.9rem; color:#94a3b8; line-height:1.7;">{entry["content"]}</div>',
                        unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🗑️ Delete entry", key=f"del_{entry['id']}"):
                all_entries = load_entries()
                all_entries = [e for e in all_entries if e["id"] != entry["id"]]
                save_entries(all_entries)
                st.toast("Entry deleted.")
                st.rerun()