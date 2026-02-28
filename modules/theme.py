def theme():
    return """
    <style>
    /* ── Google Fonts ─────────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

    /* ── Design Tokens ────────────────────────────────────────────── */
    :root {
        --bg-deep:        #0b1120;
        --bg-mid:         #111827;
        --bg-card:        rgba(255,255,255,0.04);
        --bg-card-hover:  rgba(255,255,255,0.07);
        --border:         rgba(255,255,255,0.07);
        --border-accent:  rgba(110,231,183,0.25);

        --teal:           #6ee7b7;
        --teal-dim:       #34d399;
        --teal-glow:      rgba(110,231,183,0.15);
        --amber:          #fbbf24;
        --amber-dim:      rgba(251,191,36,0.12);
        --rose:           #fb7185;
        --rose-dim:       rgba(251,113,133,0.12);
        --lavender:       #a78bfa;
        --sky:            #7dd3fc;

        --text-primary:   #f0faf6;
        --text-secondary: #94a3b8;
        --text-muted:     #64748b;

        --radius-sm:  8px;
        --radius-md:  14px;
        --radius-lg:  20px;
        --radius-xl:  28px;

        --shadow-card: 0 4px 24px rgba(0,0,0,0.35);
        --shadow-glow: 0 0 40px rgba(110,231,183,0.08);
    }

    /* ── Global Reset ─────────────────────────────────────────────── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        color: var(--text-primary);
    }

    /* ── App Background ───────────────────────────────────────────── */
    [data-testid="stAppViewContainer"] {
        background: var(--bg-deep);
        background-image:
            radial-gradient(ellipse 80% 50% at 20% -10%, rgba(110,231,183,0.07) 0%, transparent 60%),
            radial-gradient(ellipse 60% 40% at 80% 100%, rgba(167,139,250,0.06) 0%, transparent 55%),
            radial-gradient(ellipse 50% 60% at 50% 50%, rgba(251,191,36,0.03) 0%, transparent 70%);
    }

    /* ── Main Content Padding ─────────────────────────────────────── */
    [data-testid="stMain"] .block-container {
        padding: 2.5rem 3rem 4rem 3rem;
        max-width: 1100px;
    }

    /* ── Sidebar ──────────────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1a2d 0%, #0b1120 100%);
        border-right: 1px solid var(--border);
    }
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--teal), var(--lavender), var(--amber));
    }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span {
        color: var(--text-secondary) !important;
        font-size: 0.82rem;
    }
    /* Sidebar nav links */
    [data-testid="stSidebarNav"] a {
        border-radius: var(--radius-sm) !important;
        margin: 2px 8px !important;
        padding: 8px 12px !important;
        transition: all 0.2s ease;
    }
    [data-testid="stSidebarNav"] a:hover {
        background: var(--teal-glow) !important;
        color: var(--teal) !important;
    }
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: var(--teal-glow) !important;
        border-left: 3px solid var(--teal) !important;
        color: var(--teal) !important;
    }

    /* ── Typography ───────────────────────────────────────────────── */
    h1, h2 {
        font-family: 'DM Serif Display', serif !important;
        letter-spacing: -0.02em;
        color: var(--text-primary) !important;
    }
    h1 { font-size: 2.4rem !important; }
    h2 { font-size: 1.7rem !important; }
    h3 { font-size: 1.2rem !important; font-weight: 600; color: var(--text-primary) !important; }

    /* Caption */
    [data-testid="stCaptionContainer"] p,
    .stCaption {
        color: var(--text-muted) !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.01em;
    }

    /* ── Buttons ──────────────────────────────────────────────────── */
    .stButton > button {
        background: linear-gradient(135deg, rgba(110,231,183,0.15), rgba(110,231,183,0.08)) !important;
        color: var(--teal) !important;
        border: 1px solid var(--border-accent) !important;
        border-radius: var(--radius-sm) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.88rem !important;
        padding: 0.5rem 1.2rem !important;
        transition: all 0.2s ease !important;
        letter-spacing: 0.01em;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, rgba(110,231,183,0.25), rgba(110,231,183,0.15)) !important;
        border-color: var(--teal-dim) !important;
        box-shadow: 0 0 16px rgba(110,231,183,0.15) !important;
        transform: translateY(-1px);
    }
    /* Primary button */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--teal-dim), #059669) !important;
        color: #0b1120 !important;
        border: none !important;
        font-weight: 600 !important;
    }
    .stButton > button[kind="primary"]:hover {
        box-shadow: 0 0 24px rgba(52,211,153,0.3) !important;
    }

    /* ── Chat Messages ────────────────────────────────────────────── */
    [data-testid="stChatMessage"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        padding: 1rem 1.2rem !important;
        margin-bottom: 0.6rem;
        box-shadow: var(--shadow-card);
        transition: border-color 0.2s;
    }
    [data-testid="stChatMessage"]:hover {
        border-color: var(--border-accent) !important;
    }
    /* User message */
    [data-testid="stChatMessage"][data-testid*="user"],
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        border-left: 3px solid var(--sky) !important;
    }
    /* Assistant message */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        border-left: 3px solid var(--teal) !important;
    }

    /* Chat input */
    [data-testid="stChatInput"] {
        background: var(--bg-mid) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-lg) !important;
        box-shadow: 0 0 0 1px transparent;
        transition: all 0.2s;
    }
    [data-testid="stChatInput"]:focus-within {
        border-color: var(--teal-dim) !important;
        box-shadow: 0 0 0 3px rgba(110,231,183,0.1) !important;
    }
    [data-testid="stChatInput"] textarea {
        font-family: 'DM Sans', sans-serif !important;
        color: var(--text-primary) !important;
        font-size: 0.9rem !important;
    }

    /* ── Metric Cards ─────────────────────────────────────────────── */
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        padding: 1.2rem 1.4rem !important;
        box-shadow: var(--shadow-card);
        transition: all 0.2s;
    }
    [data-testid="stMetric"]:hover {
        border-color: var(--border-accent) !important;
        background: var(--bg-card-hover) !important;
    }
    [data-testid="stMetricValue"] {
        font-family: 'DM Serif Display', serif !important;
        font-size: 1.8rem !important;
        color: var(--teal) !important;
    }
    [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-size: 0.78rem !important;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    [data-testid="stMetricDelta"] {
        font-size: 0.78rem !important;
    }

    /* ── Text Inputs ──────────────────────────────────────────────── */
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stNumberInput"] input {
        background: var(--bg-mid) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        color: var(--text-primary) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.88rem !important;
        transition: all 0.2s;
    }
    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus {
        border-color: var(--teal-dim) !important;
        box-shadow: 0 0 0 3px rgba(110,231,183,0.08) !important;
        outline: none !important;
    }
    /* Label */
    [data-testid="stTextInput"] label,
    [data-testid="stTextArea"] label,
    [data-testid="stSelectbox"] label,
    [data-testid="stNumberInput"] label,
    [data-testid="stMultiSelect"] label,
    [data-testid="stFileUploader"] label {
        color: var(--text-secondary) !important;
        font-size: 0.82rem !important;
        font-weight: 500;
        letter-spacing: 0.02em;
    }

    /* ── Selectbox ────────────────────────────────────────────────── */
    [data-testid="stSelectbox"] > div > div {
        background: var(--bg-mid) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        color: var(--text-primary) !important;
    }

    /* ── Alerts ───────────────────────────────────────────────────── */
    [data-testid="stAlert"] {
        border-radius: var(--radius-md) !important;
        border-left-width: 3px !important;
        font-size: 0.88rem !important;
    }
    /* success */
    [data-testid="stAlert"][data-baseweb="notification"][kind="positive"] {
        background: rgba(110,231,183,0.07) !important;
        border-color: var(--teal) !important;
    }
    /* info */
    [data-testid="stAlert"][data-baseweb="notification"][kind="info"] {
        background: rgba(125,211,252,0.07) !important;
        border-color: var(--sky) !important;
    }
    /* warning */
    [data-testid="stAlert"][data-baseweb="notification"][kind="warning"] {
        background: rgba(251,191,36,0.07) !important;
        border-color: var(--amber) !important;
    }
    /* error */
    [data-testid="stAlert"][data-baseweb="notification"][kind="error"] {
        background: rgba(251,113,133,0.07) !important;
        border-color: var(--rose) !important;
    }

    /* ── Expander ─────────────────────────────────────────────────── */
    [data-testid="stExpander"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        overflow: hidden;
    }
    [data-testid="stExpander"]:hover {
        border-color: var(--border-accent) !important;
    }
    [data-testid="stExpander"] summary {
        font-weight: 500 !important;
        color: var(--text-secondary) !important;
        font-size: 0.88rem !important;
        padding: 0.8rem 1rem !important;
    }

    /* ── Tabs ─────────────────────────────────────────────────────── */
    [data-testid="stTabs"] [role="tablist"] {
        background: var(--bg-mid) !important;
        border-radius: var(--radius-sm) !important;
        border: 1px solid var(--border) !important;
        padding: 4px !important;
        gap: 4px;
    }
    [data-testid="stTabs"] [role="tab"] {
        border-radius: calc(var(--radius-sm) - 2px) !important;
        color: var(--text-muted) !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        padding: 6px 16px !important;
        transition: all 0.2s;
    }
    [data-testid="stTabs"] [role="tab"][aria-selected="true"] {
        background: var(--teal-glow) !important;
        color: var(--teal) !important;
        border-bottom: none !important;
    }

    /* ── Divider ──────────────────────────────────────────────────── */
    hr {
        border: none !important;
        border-top: 1px solid var(--border) !important;
        margin: 1.5rem 0 !important;
    }

    /* ── Spinner ──────────────────────────────────────────────────── */
    [data-testid="stSpinner"] > div {
        border-top-color: var(--teal) !important;
    }

    /* ── Progress bar ─────────────────────────────────────────────── */
    [data-testid="stProgressBar"] > div > div {
        background: linear-gradient(90deg, var(--teal-dim), var(--lavender)) !important;
        border-radius: 99px !important;
    }
    [data-testid="stProgressBar"] > div {
        background: var(--bg-card) !important;
        border-radius: 99px !important;
    }

    /* ── Dataframe ────────────────────────────────────────────────── */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        overflow: hidden;
    }

    /* ── Multiselect tags ─────────────────────────────────────────── */
    [data-testid="stMultiSelect"] span[data-baseweb="tag"] {
        background: var(--teal-glow) !important;
        border: 1px solid var(--border-accent) !important;
        color: var(--teal) !important;
        border-radius: 99px !important;
        font-size: 0.78rem !important;
    }

    /* ── File uploader ────────────────────────────────────────────── */
    [data-testid="stFileUploader"] {
        border: 1px dashed var(--border-accent) !important;
        border-radius: var(--radius-md) !important;
        background: rgba(110,231,183,0.02) !important;
        transition: all 0.2s;
    }
    [data-testid="stFileUploader"]:hover {
        background: var(--teal-glow) !important;
        border-color: var(--teal-dim) !important;
    }

    /* ── Link buttons ─────────────────────────────────────────────── */
    [data-testid="stLinkButton"] a {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        color: var(--text-secondary) !important;
        border-radius: var(--radius-sm) !important;
        font-size: 0.85rem !important;
        transition: all 0.2s;
        text-decoration: none !important;
    }
    [data-testid="stLinkButton"] a:hover {
        border-color: var(--teal-dim) !important;
        color: var(--teal) !important;
        background: var(--teal-glow) !important;
    }

    /* ── Checkbox ─────────────────────────────────────────────────── */
    [data-testid="stCheckbox"] label {
        color: var(--text-secondary) !important;
        font-size: 0.88rem !important;
    }

    /* ── Toast ────────────────────────────────────────────────────── */
    [data-testid="stToast"] {
        background: var(--bg-mid) !important;
        border: 1px solid var(--border-accent) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-primary) !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4) !important;
    }

    /* ── Scrollbar ────────────────────────────────────────────────── */
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: rgba(110,231,183,0.2);
        border-radius: 99px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(110,231,183,0.4);
    }

    /* ── Hide Streamlit branding ──────────────────────────────────── */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """