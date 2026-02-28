import streamlit as st
import json
import os
from datetime import datetime
from PIL import Image
import io
import base64
from modules.theme import theme

st.markdown(theme(), unsafe_allow_html=True)

st.markdown("""
<style>
.profile-banner {
    background: linear-gradient(135deg, rgba(110,231,183,0.07), rgba(167,139,250,0.05));
    border: 1px solid rgba(110,231,183,0.12);
    border-radius: 18px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
}
.profile-name {
    font-family: 'DM Serif Display', serif;
    font-size: 1.8rem;
    color: #f0faf6;
    line-height: 1.2;
}
.profile-meta {
    font-size: 0.78rem;
    color: #64748b;
    margin-top: 0.3rem;
    line-height: 1.8;
}
.profile-meta strong { color: #94a3b8; }
.profile-bio {
    font-size: 0.82rem;
    color: #6ee7b7;
    font-style: italic;
    margin-top: 0.3rem;
}
.streak-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: rgba(251,191,36,0.08);
    border: 1px solid rgba(251,191,36,0.2);
    border-radius: 99px;
    padding: 0.2rem 0.75rem;
    font-size: 0.73rem;
    color: #fbbf24;
    font-weight: 600;
    margin-top: 0.4rem;
}
.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 0.7rem;
    margin-top: 1.2rem;
}
.goal-item {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 0.7rem 1rem;
    margin-bottom: 0.4rem;
    transition: all 0.2s;
}
.goal-item:hover {
    border-color: rgba(110,231,183,0.15);
}
.contact-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.6rem;
}
.interest-chip {
    display: inline-block;
    background: rgba(167,139,250,0.08);
    border: 1px solid rgba(167,139,250,0.18);
    border-radius: 99px;
    padding: 0.2rem 0.7rem;
    font-size: 0.75rem;
    color: #a78bfa;
    margin: 0.2rem;
}
</style>
""", unsafe_allow_html=True)

PROFILE_FILE = "data/profile.json"
os.makedirs("data", exist_ok=True)

def load_profile() -> dict:
    if os.path.exists(PROFILE_FILE):
        try:
            with open(PROFILE_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {}

def save_profile(data: dict) -> None:
    with open(PROFILE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def image_to_base64(image_bytes: bytes) -> str:
    return base64.b64encode(image_bytes).decode("utf-8")

def base64_to_image(b64_str: str):
    return Image.open(io.BytesIO(base64.b64decode(b64_str)))

profile = load_profile()

# ── Profile Banner ────────────────────────────────────────────────────────────
avatar_col, info_col = st.columns([1, 4])

with avatar_col:
    if profile.get("avatar"):
        try:
            img = base64_to_image(profile["avatar"])
            st.image(img, width=110)
        except Exception:
            st.image("https://api.dicebear.com/7.x/thumbs/svg?seed=mindbridge", width=110)
    else:
        st.image("https://api.dicebear.com/7.x/thumbs/svg?seed=mindbridge", width=110)

with info_col:
    name = profile.get("name", "Your Name")
    age  = profile.get("age", "—")
    gender = profile.get("gender", "—")
    member_since = profile.get("member_since", datetime.now().strftime("%Y-%m-%d"))
    streak = st.session_state.get("streak", 0)

    st.markdown(f"""
    <div class="profile-name">{name}</div>
    <div class="profile-meta">
        <strong>Age:</strong> {age} &nbsp;·&nbsp;
        <strong>Gender:</strong> {gender} &nbsp;·&nbsp;
        <strong>Member since:</strong> {member_since}
    </div>
    <div class="streak-badge">🔥 {streak} day{'s' if streak != 1 else ''} streak</div>
    """, unsafe_allow_html=True)

    if profile.get("bio"):
        st.markdown(f'<div class="profile-bio">"{profile["bio"]}"</div>', unsafe_allow_html=True)

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["✏️ Edit Profile", "🎯 Goals", "🛡️ Emergency Contacts", "🎨 Interests"])

# ── Tab 1: Edit Profile ───────────────────────────────────────────────────────
with tab1:
    st.markdown('<div class="section-label">Personal Details</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name     = st.text_input("Full Name",  value=profile.get("name", ""), placeholder="e.g. Aarav Sharma")
        age      = st.number_input("Age", min_value=10, max_value=100, value=int(profile.get("age", 18)))
    with col2:
        GENDER_OPTIONS = ["Prefer not to say", "Male", "Female", "Non-binary", "Other"]
        gender   = st.selectbox("Gender", GENDER_OPTIONS,
                                index=GENDER_OPTIONS.index(profile.get("gender", "Prefer not to say")))
        pronouns = st.text_input("Pronouns (optional)", value=profile.get("pronouns", ""),
                                 placeholder="e.g. she/her")

    bio = st.text_area("Short Bio", value=profile.get("bio", ""), height=80,
                       placeholder="A little about yourself…")

    st.markdown('<div class="section-label">Profile Photo</div>', unsafe_allow_html=True)
    uploaded_photo = st.file_uploader("Upload photo", type=["png", "jpg", "jpeg"],
                                      label_visibility="collapsed")

    if st.button("💾 Save Profile"):
        updated = {
            **profile,
            "name":         name.strip() or "Your Name",
            "age":          age,
            "gender":       gender,
            "pronouns":     pronouns.strip(),
            "bio":          bio.strip(),
            "member_since": profile.get("member_since", datetime.now().strftime("%Y-%m-%d")),
        }
        if uploaded_photo is not None:
            updated["avatar"] = image_to_base64(uploaded_photo.read())
        save_profile(updated)
        st.toast("Profile saved.")
        st.rerun()

    st.divider()
    st.markdown('<div class="section-label">Check-in Streak</div>', unsafe_allow_html=True)
    streak = st.session_state.get("streak", 0)
    st.metric("Current Streak", f"{streak} day{'s' if streak != 1 else ''}")

    if streak >= 7:
        st.success("🏆 One week strong! You're doing amazing.")
    elif streak >= 3:
        st.info("✨ Great consistency! You're building a healthy habit.")
    elif streak >= 1:
        st.info("🌱 Good start! Come back tomorrow to grow your streak.")
    else:
        st.markdown("""
        <div style="font-size:0.82rem; color:#64748b; margin-top:0.3rem;">
            Chat with your Companion daily to start your streak.
        </div>
        """, unsafe_allow_html=True)

# ── Tab 2: Goals ──────────────────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="section-label">Mental Health Goals</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.8rem; color:#475569; margin-bottom:1rem;">Set intentions to guide your well-being journey.</div>',
                unsafe_allow_html=True)

    goals: list = profile.get("goals", [])

    col_inp, col_btn = st.columns([4, 1])
    with col_inp:
        new_goal = st.text_input("New goal", placeholder="e.g. Practice mindfulness for 10 minutes daily",
                                 key="new_goal_input", label_visibility="collapsed")
    with col_btn:
        if st.button("＋ Add", use_container_width=True):
            if new_goal.strip():
                goals.append({"text": new_goal.strip(), "done": False,
                               "added": datetime.now().strftime("%Y-%m-%d")})
                profile["goals"] = goals
                save_profile(profile)
                st.toast("Goal added.")
                st.rerun()
            else:
                st.warning("Type a goal first.")

    st.markdown("<br>", unsafe_allow_html=True)

    if not goals:
        st.markdown("""
        <div style="text-align:center; padding:1.5rem; color:#475569; font-size:0.85rem;">
            🎯 No goals yet — add one above to get started.
        </div>
        """, unsafe_allow_html=True)
    else:
        for i, goal in enumerate(goals):
            gcol1, gcol2, gcol3 = st.columns([0.5, 6, 0.8])
            with gcol1:
                checked = st.checkbox("", value=goal["done"], key=f"goal_{i}")
                if checked != goal["done"]:
                    goals[i]["done"] = checked
                    profile["goals"] = goals
                    save_profile(profile)
                    st.rerun()
            with gcol2:
                display = f"~~{goal['text']}~~" if goal["done"] else goal["text"]
                st.markdown(f'<div style="font-size:0.88rem; color:{"#475569" if goal["done"] else "#94a3b8"}; margin-top:0.3rem;">{goal["text"] if not goal["done"] else "~~" + goal["text"] + "~~"}</div><div style="font-size:0.7rem; color:#374151;">Added {goal.get("added", "")}</div>',
                            unsafe_allow_html=True)
            with gcol3:
                if st.button("✕", key=f"del_goal_{i}", help="Delete goal"):
                    goals.pop(i)
                    profile["goals"] = goals
                    save_profile(profile)
                    st.rerun()

        completed = sum(1 for g in goals if g["done"])
        st.markdown(f'<div style="font-size:0.75rem; color:#475569; margin-bottom:0.4rem;">{completed} / {len(goals)} completed</div>',
                    unsafe_allow_html=True)
        st.progress(completed / len(goals) if goals else 0)

# ── Tab 3: Emergency Contacts ─────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="section-label">Emergency Contacts</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.8rem; color:#475569; margin-bottom:1rem;">These people will be alerted when you send an SOS.</div>',
                unsafe_allow_html=True)

    contacts: list = profile.get("emergency_contacts", [])

    with st.expander("＋ Add New Contact", expanded=len(contacts) == 0):
        cc1, cc2 = st.columns(2)
        with cc1:
            c_name     = st.text_input("Name",         placeholder="e.g. Ankit Shelar", key="c_name")
            c_relation = st.text_input("Relationship", placeholder="e.g. Mother, Friend", key="c_rel")
        with cc2:
            c_phone = st.text_input("Phone Number",      placeholder="e.g. 9876456770",     key="c_phone")
            c_email = st.text_input("Email (optional)",  placeholder="e.g. ankit@email.com", key="c_email")

        if st.button("Save Contact"):
            if c_name.strip() and c_phone.strip():
                contacts.append({"name": c_name.strip(), "relation": c_relation.strip(),
                                  "phone": c_phone.strip(), "email": c_email.strip()})
                profile["emergency_contacts"] = contacts
                save_profile(profile)
                st.toast(f"{c_name} added.")
                st.rerun()
            else:
                st.warning("Name and phone number are required.")

    st.markdown("<br>", unsafe_allow_html=True)

    if not contacts:
        st.markdown('<div style="font-size:0.85rem; color:#475569; text-align:center; padding:1rem;">No emergency contacts saved yet.</div>',
                    unsafe_allow_html=True)
    else:
        for i, contact in enumerate(contacts):
            ec1, ec2 = st.columns([5, 1])
            with ec1:
                email_str = f" · {contact['email']}" if contact.get("email") else ""
                st.markdown(f"""
                <div class="contact-card">
                    <div style="font-weight:600; font-size:0.9rem; color:#f0faf6;">{contact['name']}</div>
                    <div style="font-size:0.75rem; color:#475569; margin-top:0.1rem;">
                        {contact.get('relation','Contact')} · {contact['phone']}{email_str}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            with ec2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("✕ Remove", key=f"del_c_{i}"):
                    contacts.pop(i)
                    profile["emergency_contacts"] = contacts
                    save_profile(profile)
                    st.toast("Contact removed.")
                    st.rerun()

# ── Tab 4: Interests & Hobbies ────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="section-label">Interests & Hobbies</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.8rem; color:#475569; margin-bottom:1rem;">Help SunnyAura know you better — these make your experience more personal.</div>',
                unsafe_allow_html=True)

    HOBBY_SUGGESTIONS = ["Reading", "Drawing / Painting", "Gaming", "Cooking", "Yoga / Meditation",
                         "Photography", "Journaling", "Gardening", "Hiking", "Music", "Dancing", "Travelling"]
    saved_hobbies = profile.get("hobbies", [])
    hobbies = st.multiselect("Hobbies", options=HOBBY_SUGGESTIONS,
                             default=[h for h in saved_hobbies if h in HOBBY_SUGGESTIONS])
    custom_hobby = st.text_input("Custom hobby", value=profile.get("custom_hobby", ""),
                                 placeholder="e.g. Origami, Rock climbing…")

    st.divider()
    fav_songs = st.text_area("Favourite songs / artists", value=profile.get("fav_songs", ""), height=70,
                              placeholder="e.g. Tum Hi Ho – Arijit Singh, Blinding Lights – The Weeknd…")
    MUSIC_GENRES = ["Pop", "Bollywood", "Hip-Hop / Rap", "R&B / Soul", "Rock", "Classical / Instrumental",
                    "Jazz", "Electronic / EDM", "Indie", "Folk / Acoustic", "Metal", "Lo-fi"]
    saved_music = profile.get("music_genres", [])
    music_genres = st.multiselect("Music genres", options=MUSIC_GENRES,
                                  default=[m for m in saved_music if m in MUSIC_GENRES])

    st.divider()
    MOVIE_GENRES = ["Comedy", "Drama", "Romance", "Thriller / Mystery", "Horror", "Sci-Fi",
                    "Fantasy / Adventure", "Action", "Animation", "Documentary", "Biography",
                    "Crime", "Slice of Life", "Anime"]
    saved_movies = profile.get("movie_genres", [])
    movie_genres = st.multiselect("Movie / show genres", options=MOVIE_GENRES,
                                  default=[m for m in saved_movies if m in MOVIE_GENRES])
    fav_movies = st.text_area("Favourite movies or shows", value=profile.get("fav_movies", ""), height=70,
                               placeholder="e.g. 3 Idiots, Inception, Friends…")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💾 Save Interests"):
        profile.update({
            "hobbies":      hobbies,
            "custom_hobby": custom_hobby.strip(),
            "fav_songs":    fav_songs.strip(),
            "music_genres": music_genres,
            "movie_genres": movie_genres,
            "fav_movies":   fav_movies.strip(),
        })
        save_profile(profile)
        st.toast("Interests saved.")
        st.rerun()

    if any([profile.get("hobbies"), profile.get("music_genres"), profile.get("movie_genres"), profile.get("fav_songs")]):
        st.divider()
        st.markdown('<div class="section-label">Your Interests at a Glance</div>', unsafe_allow_html=True)
        all_hobbies = profile.get("hobbies", []) + ([profile["custom_hobby"]] if profile.get("custom_hobby") else [])
        if all_hobbies:
            chips = "".join(f'<span class="interest-chip">{h}</span>' for h in all_hobbies)
            st.markdown(f'<div style="margin-bottom:0.5rem;"><span style="font-size:0.75rem;color:#475569;">Hobbies</span><br>{chips}</div>',
                        unsafe_allow_html=True)
        if profile.get("music_genres"):
            chips = "".join(f'<span class="interest-chip">{g}</span>' for g in profile["music_genres"])
            st.markdown(f'<div style="margin-bottom:0.5rem;"><span style="font-size:0.75rem;color:#475569;">Music</span><br>{chips}</div>',
                        unsafe_allow_html=True)
        if profile.get("fav_songs"):
            st.markdown(f'<div style="font-size:0.82rem; color:#94a3b8; margin-bottom:0.5rem;"><span style="color:#475569;font-size:0.75rem;">Favourite Artists · </span>{profile["fav_songs"]}</div>',
                        unsafe_allow_html=True)
        if profile.get("movie_genres"):
            chips = "".join(f'<span class="interest-chip">{g}</span>' for g in profile["movie_genres"])
            st.markdown(f'<div style="margin-bottom:0.5rem;"><span style="font-size:0.75rem;color:#475569;">Movies & Shows</span><br>{chips}</div>',
                        unsafe_allow_html=True)