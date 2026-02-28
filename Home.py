"""
SunnyAura — Home / Landing Page
"""

import streamlit as st
from modules.theme import theme

st.set_page_config(
    page_title="SunnyAura — Mental Health Companion",
    page_icon="🌿",
    layout="wide",
)

st.markdown(theme(), unsafe_allow_html=True)

# ── Custom Home-page styles ───────────────────────────────────────────────────
st.markdown("""
<style>
.hero-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #6ee7b7;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 3.2rem;
    line-height: 1.15;
    color: #f0faf6;
    margin: 0 0 1rem 0;
}
.hero-title em {
    color: #6ee7b7;
    font-style: italic;
}
.hero-sub {
    font-size: 1.05rem;
    color: #94a3b8;
    line-height: 1.7;
    max-width: 540px;
    margin-bottom: 2rem;
}
.feature-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 1.4rem 1.5rem;
    margin-bottom: 0.8rem;
    transition: all 0.25s ease;
    cursor: default;
}
.feature-card:hover {
    background: rgba(110,231,183,0.06);
    border-color: rgba(110,231,183,0.22);
    transform: translateX(4px);
}
.feature-icon {
    font-size: 1.4rem;
    margin-bottom: 0.5rem;
}
.feature-title {
    font-weight: 600;
    font-size: 0.92rem;
    color: #f0faf6;
    margin-bottom: 0.2rem;
}
.feature-desc {
    font-size: 0.82rem;
    color: #64748b;
    line-height: 1.5;
}
.stat-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(110,231,183,0.08);
    border: 1px solid rgba(110,231,183,0.18);
    border-radius: 99px;
    padding: 0.3rem 0.9rem;
    font-size: 0.78rem;
    color: #6ee7b7;
    font-weight: 500;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}
.disclaimer {
    font-size: 0.74rem;
    color: #475569;
    line-height: 1.6;
    border-top: 1px solid rgba(255,255,255,0.06);
    padding-top: 1rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 1rem 0 0.5rem 0;">
        <div style="font-family:'DM Serif Display',serif; font-size:1.4rem; color:#f0faf6;">
            🌿 SunnyAura
        </div>
        <div style="font-size:0.75rem; color:#475569; margin-top:0.2rem;">
            Your mental wellness companion
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    streak = st.session_state.get("streak", 0)
    if "streak" not in st.session_state:
        st.session_state.streak = 0

    st.markdown(f"""
    <div style="background:rgba(110,231,183,0.07); border:1px solid rgba(110,231,183,0.18);
                border-radius:12px; padding:1rem; text-align:center;">
        <div style="font-size:1.6rem; font-family:'DM Serif Display',serif; color:#6ee7b7;">
            {streak}
        </div>
        <div style="font-size:0.72rem; color:#64748b; text-transform:uppercase;
                    letter-spacing:0.1em; margin-top:0.1rem;">
            Day Streak 🔥
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.72rem; color:#475569; text-align:center; line-height:1.6;">
        A safe, private space.<br>Everything stays with you.
    </div>
    """, unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
left, right = st.columns([3, 2], gap="large")

with left:
    st.markdown("""
    <div class="hero-eyebrow">Mental Health · AI Companion</div>
    <h1 class="hero-title">
        A space to feel<br><em>heard & supported</em>
    </h1>
    <p class="hero-sub">
        SunnyAura combines empathetic AI conversation with personal tools
        to help you understand your emotions, track your well-being, and
        find calm — one day at a time.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div>
        <span class="stat-pill">🔒 Private & secure</span>
        <span class="stat-pill">🧠 Emotion-aware AI</span>
        <span class="stat-pill">📊 Mood tracking</span>
        <span class="stat-pill">🚨 Crisis support</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💬  Start Chatting Now", use_container_width=False):
        st.switch_page("pages/1_Companion_Chat.py")

with right:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💬</div>
        <div class="feature-title">Companion Chat</div>
        <div class="feature-desc">Talk to your AI companion anytime. Emotion-aware, always non-judgmental.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📓</div>
        <div class="feature-title">Personal Diary</div>
        <div class="feature-desc">Write your thoughts in a password-protected private journal.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Mood Trends</div>
        <div class="feature-desc">Visualize your emotional patterns with beautiful charts over time.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🚨</div>
        <div class="feature-title">Emergency Support</div>
        <div class="feature-desc">Helplines, SOS alerts to guardians & grounding techniques.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="disclaimer">
    ⚠️ <strong>Disclaimer:</strong> SunnyAura is an AI-powered support tool and is NOT a substitute
    for clinical diagnosis, therapy, or emergency medical intervention. Always seek professional help when needed.
</div>
""", unsafe_allow_html=True)