"""
SunnyAura — Companion Chat Page
"""

import streamlit as st
from modules.theme import theme
from modules.ai_engine import check_crisis, get_emotion, get_ai_response, save_mood_entry

st.markdown(theme(), unsafe_allow_html=True)

st.markdown("""
<style>
.chat-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.3rem;
}
.chat-avatar {
    width: 44px; height: 44px;
    background: linear-gradient(135deg, #6ee7b7, #059669);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
}
.chat-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.6rem;
    color: #f0faf6;
}
.chat-sub {
    font-size: 0.8rem;
    color: #475569;
    margin-top: -0.1rem;
}
.online-dot {
    display: inline-block;
    width: 7px; height: 7px;
    background: #6ee7b7;
    border-radius: 50%;
    margin-right: 5px;
    box-shadow: 0 0 6px #6ee7b7;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%,100% { opacity: 1; }
    50% { opacity: 0.4; }
}
.mood-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    background: rgba(110,231,183,0.08);
    border: 1px solid rgba(110,231,183,0.2);
    border-radius: 99px;
    padding: 0.2rem 0.7rem;
    font-size: 0.73rem;
    color: #6ee7b7;
    font-weight: 500;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-header">
    <div class="chat-avatar">🌿</div>
    <div>
        <div class="chat-title">Your Companion</div>
        <div class="chat-sub">
            <span class="online-dot"></span>Always here to listen
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Chat history ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome message if no history
if not st.session_state.messages:
    st.markdown("""
    <div style="text-align:center; padding: 2.5rem 1rem; color: #475569;">
        <div style="font-size:2.5rem; margin-bottom:0.8rem;">🌿</div>
        <div style="font-size:1rem; color:#64748b; font-weight:500;">
            Hi there — I'm glad you're here.
        </div>
        <div style="font-size:0.82rem; color:#475569; margin-top:0.4rem; max-width:360px; margin-left:auto; margin-right:auto; line-height:1.6;">
            Share whatever's on your mind. Whether it's a big feeling or just a "hey" — I'm listening.
        </div>
    </div>
    """, unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg.get("mood_badge"):
            st.markdown(f'<div class="mood-badge">🎯 {msg["mood_badge"]}</div>', unsafe_allow_html=True)
        st.markdown(msg["content"])

# ── Chat input ────────────────────────────────────────────────────────────────
if prompt := st.chat_input("Share what's on your mind…"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Crisis check
    if check_crisis(prompt):
        crisis_msg = (
            "I'm really concerned about what you've shared. "
            "Please know you're not alone — help is available right now.\n\n"
            "📞 **iCall (National):** 9152987821 *(Mon–Sat, 8am–10pm)*\n"
            "📞 **Vandrevala Foundation:** 9999666555 *(24/7)*\n\n"
            "Would you like to visit the **Emergency** page for more support options?"
        )
        with st.chat_message("assistant"):
            st.error("⚠️ Crisis support needed")
            st.markdown(crisis_msg)
        st.session_state.messages.append({"role": "assistant", "content": crisis_msg})

    else:
        with st.spinner(""):
            emotion, score = get_emotion(prompt)
            response, is_casual = get_ai_response(
                user_message=prompt,
                emotion=emotion,
                chat_history=st.session_state.messages[:-1],
            )

        if not is_casual:
            save_mood_entry(emotion, score)

        badge_text = None
        if not is_casual:
            badge_text = f"{emotion.capitalize()} · {int(score * 100)}% confidence"

        with st.chat_message("assistant"):
            if badge_text:
                st.markdown(f'<div class="mood-badge">🎯 {badge_text}</div>', unsafe_allow_html=True)
            st.markdown(response)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "mood_badge": badge_text,
        })

# ── Footer controls ───────────────────────────────────────────────────────────
if st.session_state.get("messages"):
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("🗑️ Clear", help="Clear conversation"):
            st.session_state.messages = []
            st.rerun()