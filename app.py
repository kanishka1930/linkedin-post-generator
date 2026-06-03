import streamlit as st
from config import get_model
from prompt_builder import generate_post
import re

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton > button {
    width: 100%;
    height: 3rem;
    border-radius: 10px;
    font-size: 18px;
    font-weight: 600;
}

.generated-post {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🚀 LinkedIn Post Generator")
st.markdown(
    "Generate professional LinkedIn posts using Gemini AI."
)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.header("⚙️ Post Settings")

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Inspirational",
            "Humorous",
            "Funny",
            "Angry",
            "Sad"
        ]
    )

    audience = st.text_input(
        "Target Audience",
        placeholder="Students, Developers, Recruiters..."
    )

    length = st.selectbox(
        "Post Length",
        [
            "Short (100–150 words)",
            "Medium (200–300 words)",
            "Long (400–500 words)"
        ]
    )

    framework = st.selectbox(
        "Framework",
        [
            "AIDA (Attention, Interest, Desire, Action)",
            "PAS (Problem, Agitate, Solution)",
            "Storytelling",
            "Listicle",
            "How-to / Tips",
            "None"
        ]
    )

# ---------------- MAIN AREA ----------------
topic = st.text_area(
    "📝 Enter Post Topic",
    placeholder="Example: Why Java is still relevant in 2026..."
)

col1, col2 = st.columns(2)

generate_btn = col1.button("✨ Generate Post")
clear_btn = col2.button("🗑 Clear")

if clear_btn:
    st.rerun()

# ---------------- GENERATE ----------------
if generate_btn:

    if not topic.strip():
        st.warning("Please enter a topic.")
        st.stop()

    try:

        with st.spinner("Generating LinkedIn Post..."):

            model = get_model()

            inputs = {
                "topic": topic,
                "tone": tone,
                "audience": audience,
                "length": length,
                "framework": framework
            }

            post = generate_post(model, inputs)

        st.success("Post Generated Successfully")

        st.subheader("📄 Generated Post")

        st.markdown(
            f"""
            <div class="generated-post">
            {post}
            </div>
            """,
            unsafe_allow_html=True
        )

        safe_name = re.sub(
            r'[^a-zA-Z0-9_]',
            '_',
            topic.strip()
        )

        file_name = f"LINKEDIN_POST_{safe_name}.txt"

        st.download_button(
            label="⬇ Download Post",
            data=post,
            file_name=file_name,
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")