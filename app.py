
from io import BytesIO

import streamlit as st
from gtts import gTTS

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NovaVoice AI",
    page_icon="🎙️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #312e81, #4c1d95, #164e63);
    background-attachment: fixed;
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e1b4b, #312e81, #4c1d95);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    background: linear-gradient(135deg, #7c3aed, #2563eb, #0891b2);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 48px;
    font-weight: 800;
}

.hero p {
    color: #e0f2fe;
    font-size: 18px;
}

.feature {
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 18px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 12px;
}

div[data-testid="stTextArea"] textarea {
    background-color: #f8fafc;
    color: #111827;
    border-radius: 15px;
    border: 2px solid #818cf8;
    font-size: 16px;
}

div[data-testid="stSelectbox"] > div,
div[data-testid="stFileUploader"] {
    border-radius: 12px;
}

.stButton > button {
    background: linear-gradient(90deg, #8b5cf6, #3b82f6, #06b6d4);
    color: white;
    border: none;
    border-radius: 14px;
    font-weight: bold;
    padding: 12px 25px;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    border: 1px solid white;
    color: white;
}

.stDownloadButton > button {
    background: linear-gradient(90deg, #10b981, #059669);
    color: white;
    border-radius: 12px;
    font-weight: bold;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    padding: 15px;
    border-radius: 15px;
}

hr {
    border-color: rgba(255,255,255,0.2);
}

.footer {
    text-align: center;
    color: #cbd5e1;
    padding: 20px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Bengali": "bn",
    "Marathi": "mr",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Gujarati": "gu",
    "Urdu": "ur",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
}

ACCENTS = {
    "Indian 🇮🇳": "co.in",
    "American 🇺🇸": "com",
    "British 🇬🇧": "co.uk",
    "Australian 🇦🇺": "com.au",
}

SAMPLES = {
    "English": "Hello! Welcome to NovaVoice AI. Transform your text into beautiful speech and enjoy the magic of voice technology!",
    "Hindi": "नमस्ते! नोवा वॉइस एआई में आपका स्वागत है।",
    "Telugu": "నమస్కారం! నోవా వాయిస్ ఏఐకి స్వాగతం.",
    "Tamil": "வணக்கம்! நோவா வாய்ஸ் ஏஐக்கு வரவேற்கிறோம்.",
    "French": "Bonjour ! Bienvenue dans NovaVoice AI.",
    "Spanish": "¡Hola! Bienvenido a NovaVoice AI.",
    "Japanese": "こんにちは！NovaVoice AIへようこそ。",
    "German": "Hallo! Willkommen bei NovaVoice AI.",
}

# ---------------- FUNCTION ----------------
def synthesize(text, lang, tld, slow):
    audio_buffer = BytesIO()
    gTTS(
        text=text,
        lang=lang,
        tld=tld,
        slow=slow
    ).write_to_fp(audio_buffer)

    return audio_buffer.getvalue()

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 🎛️ Voice Studio")

lang_name = st.sidebar.selectbox(
    "🌍 Choose Language",
    list(LANGUAGES.keys())
)

accent = "Indian 🇮🇳"

if lang_name == "English":
    accent = st.sidebar.selectbox(
        "🎭 Choose Accent",
        list(ACCENTS.keys())
    )

slow = st.sidebar.toggle("🐢 Slow Voice Mode", value=False)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Voice Tips")
st.sidebar.info(
    "• Enter text in the selected language.\n\n"
    "• English accents are available only for English.\n\n"
    "• Short sentences may generate audio faster."
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ✨ About")
st.sidebar.write(
    "NovaVoice AI converts written text into speech "
    "using Google Text-to-Speech."
)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>🎙️ NovaVoice AI</h1>
    <p>Your Words. Your Voice. Your World. 🌍</p>
    <p>Transform text into speech with the magic of AI ✨</p>
</div>
""", unsafe_allow_html=True)

# ---------------- FEATURES ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature">
        <h3>🌍 Multilingual</h3>
        <p>14+ Languages</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature">
        <h3>🎭 Voice Styles</h3>
        <p>Multiple English Accents</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature">
        <h3>🎧 Audio Magic</h3>
        <p>Listen & Download</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------- INPUT ----------------
st.markdown("## 📝 Create Your Voice")

source = st.radio(
    "Choose your input method",
    ["✍️ Type Text", "📂 Upload Text File"],
    horizontal=True
)

if source == "✍️ Type Text":
    sample_choice = st.selectbox(
        "🪄 Try a sample text",
        ["None"] + list(SAMPLES.keys())
    )

    sample_text = (
        SAMPLES.get(sample_choice, "")
        if sample_choice != "None"
        else ""
    )

    text = st.text_area(
        "💬 Enter your text here",
        value=sample_text,
        height=220,
        max_chars=5000,
        placeholder="✨ Type something amazing here..."
    )

else:
    file = st.file_uploader(
        "📂 Upload your TXT file",
        type=["txt"]
    )

    text = ""

    if file is not None:
        text = file.read().decode(
            "utf-8",
            errors="ignore"
        )

        if len(text) > 5000:
            st.warning("Only the first 5000 characters can be used.")
            text = text[:5000]

        st.text_area(
            "📖 Uploaded text preview",
            text,
            height=220,
            disabled=True
        )

# ---------------- TEXT STATS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📝 Characters", len(text))

with col2:
    st.metric("🔤 Words", len(text.split()))

with col3:
    st.metric("🌍 Language", lang_name)

st.progress(min(len(text) / 5000, 1.0))

st.caption(f"📊 {len(text)} / 5000 characters")

# ---------------- GENERATE ----------------
st.markdown("---")

if st.button("🚀 Generate My Voice", use_container_width=True):

    if not text.strip():
        st.warning("⚠️ Please enter or upload some text first.")

    elif len(text) > 5000:
        st.warning("⚠️ Text must contain 5000 characters or fewer.")

    else:
        tld = ACCENTS[accent] if lang_name == "English" else "com"

        with st.spinner("✨ Creating your magical voice..."):

            try:
                audio = synthesize(
                    text,
                    LANGUAGES[lang_name],
                    tld,
                    slow
                )

                st.session_state["generated_audio"] = audio
                st.session_state["generated_text"] = text
                st.session_state["generated_language"] = lang_name

            except Exception as e:
                st.error(
                    "❌ Audio generation failed. "
                    "Check your internet connection or try again."
                )
                st.caption(str(e))

# ---------------- AUDIO OUTPUT ----------------
if "generated_audio" in st.session_state:

    st.markdown("---")

    st.markdown("""
    <div class="hero">
        <h2>🎉 Your Voice Is Ready!</h2>
        <p>Listen to your generated speech below 🎧</p>
    </div>
    """, unsafe_allow_html=True)

    st.audio(
        st.session_state["generated_audio"],
        format="audio/mp3"
    )

    st.download_button(
        "⬇️ Download Your MP3",
        data=st.session_state["generated_audio"],
        file_name="NovaVoice_Speech.mp3",
        mime="audio/mpeg",
        use_container_width=True
    )

    st.success("✨ Audio generated successfully!")

    with st.expander("📖 View Generated Text"):
        st.write(st.session_state["generated_text"])

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown("""
<div class="footer">
    💜 Powered by gTTS | Built with Streamlit <br>
    ✨ NovaVoice AI — Let Your Words Speak! ✨
</div>
""", unsafe_allow_html=True)