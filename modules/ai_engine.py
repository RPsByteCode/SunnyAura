"""
SunnyAura AI Engine
Handles emotion detection, AI response generation, and mood data persistence.
"""

from groq import Groq
from huggingface_hub import InferenceClient
import streamlit as st
from datetime import datetime, date

# Models 
EMOTION_MODEL = "bhadresh-savani/distilbert-base-uncased-emotion"
CHAT_MODEL    = "llama-3.3-70b-versatile"

CRISIS_KEYWORDS = [
    "suicide", "suicidal", "kill myself", "end my life", "hurt myself",
    "self harm", "self-harm", "end it all", "want to die", "no reason to live",
]

# Short casual greetings / small-talk that don't need a therapy-style response
CASUAL_TRIGGERS = [
    "hi", "hii", "hiii", "hiiii", "hey", "heyyy", "hello", "howdy", "sup",
    "what's up", "whats up", "yo", "good morning", "good evening",
    "good afternoon", "good night", "gm", "gn",
    "how are you", "how r you", "how are u", "how's it going", "hows it going",
    "how do you do", "how r u",
    "thanks", "thank you", "thankyou", "ty", "thx",
    "ok", "okay", "k", "cool", "nice", "great", "awesome", "sounds good",
    "bye", "goodbye", "see you", "see ya", "cya", "later",
    "lol", "haha", "hehe",
]


def _is_casual(text: str) -> bool:
    """Returns True if the message is a short casual greeting or small-talk."""
    cleaned = text.strip().lower().rstrip("!?. ")
    # Exact match
    if cleaned in CASUAL_TRIGGERS:
        return True
    # Starts with a casual trigger AND is a short message (<=5 words)
    if len(cleaned.split()) <= 5 and any(cleaned.startswith(t) for t in CASUAL_TRIGGERS):
        return True
    return False


@st.cache_resource
def _get_hf_client() -> InferenceClient:
    return InferenceClient(api_key=st.secrets["hf_token"])


def _get_groq_client() -> Groq:
    """Not cached — avoids stale/broken auth being stuck in cache."""
    return Groq(api_key=st.secrets["groq_token"])


def check_crisis(text: str) -> bool:
    """Returns True if the message contains crisis-level language."""
    lowered = text.lower()
    return any(keyword in lowered for keyword in CRISIS_KEYWORDS)


def get_emotion(text: str) -> tuple[str, float]:
    """
    Detects the dominant emotion in *text* using a DistilBERT classifier.
    Returns (label, score) e.g. ("sadness", 0.91).
    Falls back to ("neutral", 0.0) on any error.
    """
    try:
        client = _get_hf_client()
        results = client.text_classification(text, model=EMOTION_MODEL)
        top = sorted(results, key=lambda x: x["score"], reverse=True)[0]
        return top["label"], top["score"]
    except Exception as e:
        st.warning(f"Emotion detection unavailable: {e}")
        return "neutral", 0.0


def get_ai_response(
    user_message: str,
    emotion: str,
    chat_history: list | None = None,
) -> tuple[str, bool]:
    """
    Returns (response_text, is_casual).
    Callers use `is_casual` to decide whether to show the mood badge.
    """
    casual = _is_casual(user_message)

    if casual:
        system_prompt = (
            "You are SunnyAura, a friendly and warm AI companion. "
            "The user is just greeting you or making casual small talk. "
            "Reply naturally and conversationally — exactly like a friendly person would in a chat. "
            "Keep it very short: 1-2 sentences max. "
            "No therapy language, no emotion analysis, no heavy questions."
        )
    else:
        system_prompt = (
            "You are SunnyAura, a warm, empathetic, and non-judgmental mental health companion. "
            f"The user's current detected emotion is: {emotion}. "
            "Tailor your response to that emotion. Keep replies concise (2-4 sentences). "
            "Do NOT use bullet points. Respond like a caring, supportive friend — not a therapist."
        )

    messages = [{"role": "system", "content": system_prompt}]

    if chat_history:
        for msg in chat_history[-6:]:
            messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": user_message})

    try:
        groq_client = _get_groq_client()
        response = groq_client.chat.completions.create(
            messages=messages,
            model=CHAT_MODEL,
            max_tokens=200,
            temperature=0.75,
        )
        return response.choices[0].message.content.strip(), casual

    except Exception as e:
        st.error(f"Chat response unavailable ({type(e).__name__}: {e})")
        fallbacks = {
            "sadness":  "I'm so sorry you're feeling this way. I'm here to listen.",
            "joy":      "That's wonderful! What made this moment special?",
            "anger":    "It sounds like something really frustrated you. Want to talk about it?",
            "fear":     "It's okay to feel scared sometimes. You're not alone in this.",
            "surprise": "Oh wow, that sounds unexpected! Tell me more.",
            "neutral":  "I'm here for you. Tell me more about what's on your mind.",
        }
        return fallbacks.get(emotion.lower(), "I'm listening. Tell me more."), casual


def update_streak() -> None:
    today        = date.today().isoformat()
    last_checkin = st.session_state.get("last_checkin_date", None)
    streak       = st.session_state.get("streak", 0)

    if last_checkin == today:
        return

    if last_checkin:
        from datetime import timedelta
        yesterday = (date.today() - timedelta(days=1)).isoformat()
        streak = streak + 1 if last_checkin == yesterday else 1
    else:
        streak = 1

    st.session_state["streak"]            = streak
    st.session_state["last_checkin_date"] = today


def save_mood_entry(emotion: str, score: float) -> None:
    """Appends a timestamped mood entry to st.session_state.mood_data."""
    if "mood_data" not in st.session_state:
        st.session_state.mood_data = []

    st.session_state.mood_data.append({
        "Date":  datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Score": round(score, 2),
        "Mood":  emotion.capitalize(),
    })
    update_streak()