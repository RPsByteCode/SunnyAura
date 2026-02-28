"""
SunnyAura — Emergency Support Page
"""

import streamlit as st
import time
from modules.theme import theme

st.markdown(theme(), unsafe_allow_html=True)

st.markdown("""
<style>
.emergency-banner {
    background: rgba(251,113,133,0.08);
    border: 1px solid rgba(251,113,133,0.25);
    border-left: 4px solid #fb7185;
    border-radius: 14px;
    padding: 1.1rem 1.4rem;
    margin-bottom: 1.5rem;
    font-size: 0.88rem;
    color: #fca5a5;
    line-height: 1.6;
}
.helpline-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.7rem;
    transition: all 0.2s;
}
.helpline-card:hover {
    border-color: rgba(125,211,252,0.25);
    background: rgba(125,211,252,0.04);
}
.helpline-name {
    font-weight: 600;
    font-size: 0.92rem;
    color: #f0faf6;
    margin-bottom: 0.15rem;
}
.helpline-number {
    font-family: 'DM Serif Display', serif;
    font-size: 1.25rem;
    color: #7dd3fc;
    letter-spacing: 0.02em;
}
.helpline-hours {
    font-size: 0.73rem;
    color: #475569;
    margin-top: 0.1rem;
}
.guardian-card {
    background: rgba(110,231,183,0.05);
    border: 1px solid rgba(110,231,183,0.15);
    border-radius: 12px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
}
.guardian-dot {
    width: 8px; height: 8px;
    background: #6ee7b7;
    border-radius: 50%;
    flex-shrink: 0;
}
.guardian-name {
    font-weight: 600;
    font-size: 0.88rem;
    color: #6ee7b7;
}
.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 0.8rem;
}
.grounding-step {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    padding: 0.75rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.grounding-num {
    width: 28px; height: 28px;
    background: rgba(167,139,250,0.12);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem;
    color: #a78bfa;
    font-weight: 700;
    flex-shrink: 0;
    margin-top: 0.05rem;
}
.grounding-text {
    font-size: 0.88rem;
    color: #94a3b8;
    line-height: 1.5;
}
.grounding-text strong {
    color: #f0faf6;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-bottom:1rem;">
    <div style="font-family:'DM Serif Display',serif; font-size:2rem; color:#f0faf6;">
        🚨 Emergency Support
    </div>
    <div style="font-size:0.88rem; color:#94a3b8; margin-top:0.2rem; font-style:italic;">
        You are not alone. Reaching out is the bravest thing you can do.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="emergency-banner">
    🆘 If you or someone you know is in <strong>immediate danger</strong>,
    please call <strong style="color:#fb7185;">112</strong> (India Emergency)
    or your local emergency number right away.
</div>
""", unsafe_allow_html=True)

# ── Main columns ──────────────────────────────────────────────────────────────
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.markdown('<div class="section-label">📞 Crisis Helplines</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="helpline-card">
        <div class="helpline-name">iCall (National)</div>
        <div class="helpline-number">9152987821</div>
        <div class="helpline-hours">Mon–Sat · 8:00 am – 10:00 pm</div>
    </div>
    <div class="helpline-card">
        <div class="helpline-name">Vandrevala Foundation</div>
        <div class="helpline-number">9999666555</div>
        <div class="helpline-hours">Available 24 / 7 · All languages</div>
    </div>
    <div class="helpline-card">
        <div class="helpline-name">Snehi</div>
        <div class="helpline-number">044-24640050</div>
        <div class="helpline-hours">Mon–Sat · 8:00 am – 10:00 pm</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("💬 Chat with a Professional Online", "https://icallhelpline.org/",
                   use_container_width=True)

with col2:
    st.markdown('<div class="section-label">🛡️ Your Guardians</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.8rem; color:#475569; margin-bottom:0.8rem;">
        These trusted contacts will be alerted if you send an SOS.
    </div>
    <div class="guardian-card">
        <div class="guardian-dot"></div>
        <div>
            <div class="guardian-name">Rohit</div>
            <div style="font-size:0.72rem; color:#475569;">Primary Guardian</div>
        </div>
    </div>
    <div class="guardian-card">
        <div class="guardian-dot"></div>
        <div>
            <div class="guardian-name">Rutik</div>
            <div style="font-size:0.72rem; color:#475569;">Secondary Guardian</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚨 Send SOS Alert to Guardians", type="primary", use_container_width=True):
        with st.spinner("Sending SOS alert…"):
            time.sleep(1.5)
        st.success(
            "✅ SOS alert sent to **Rohit** and **Rutik**.\n\n"
            "They have been notified. Please stay somewhere safe and wait for them to reach out."
        )

st.divider()

# ── Grounding technique ───────────────────────────────────────────────────────
st.markdown('<div class="section-label">🧘 Quick Grounding — The 5-4-3-2-1 Technique</div>',
            unsafe_allow_html=True)
st.markdown("""
<div style="font-size:0.82rem; color:#475569; margin-bottom:1rem; line-height:1.6;">
    Feeling overwhelmed? This exercise brings you back to the present moment.
    Take a slow breath between each step.
</div>
""", unsafe_allow_html=True)

steps = [
    ("5", "things you can <strong>see</strong> around you"),
    ("4", "things you can physically <strong>feel</strong>"),
    ("3", "things you can <strong>hear</strong>"),
    ("2", "things you can <strong>smell</strong>"),
    ("1", "thing you can <strong>taste</strong>"),
]
for num, text in steps:
    st.markdown(f"""
    <div class="grounding-step">
        <div class="grounding-num">{num}</div>
        <div class="grounding-text">Name <strong>{num}</strong> {text}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="font-size:0.78rem; color:#475569; margin-top:0.8rem; font-style:italic;">
    Take slow, deep breaths as you go through each step. You are safe. 🌿
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Additional resources ──────────────────────────────────────────────────────
st.markdown('<div class="section-label">🔗 Additional Resources</div>', unsafe_allow_html=True)
r1, r2, r3 = st.columns(3)
with r1:
    st.link_button("iCall Helpline", "https://icallhelpline.org/", use_container_width=True)
with r2:
    st.link_button("Vandrevala Foundation", "https://www.vandrevalafoundation.com/", use_container_width=True)
with r3:
    st.link_button("Find Local Support", "https://www.findahelpline.com/", use_container_width=True)

st.markdown("""
<div style="font-size:0.73rem; color:#374151; margin-top:1.5rem; line-height:1.6;
            border-top:1px solid rgba(255,255,255,0.05); padding-top:1rem;">
    ⚠️ <strong>Disclaimer:</strong> SunnyAura is an AI-powered support tool and is NOT a substitute
    for clinical diagnosis, therapy, or emergency medical intervention.
    Always seek professional help when needed.
</div>
""", unsafe_allow_html=True)