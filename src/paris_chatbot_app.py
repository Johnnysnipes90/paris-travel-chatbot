# ============================================================
# Project: AI Paris Travel Guide Chatbot (Enhanced Streamlit GUI)
# Author: Olalemi John Oluwatosin
# Company: Peterman Reality Tours (Demo Project)
# ============================================================

import os
import time
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

# ==========================
# CONFIGURATION
# ==========================
load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

st.set_page_config(
    page_title="Paris Travel Chatbot",
    page_icon="🗼",
    layout="wide",
)

# GLOBAL CSS FOR FULL WIDTH AND RESPONSIVE DESIGN
st.markdown("""
<style>
/* Make content use more screen width */
.block-container {
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* Full-width text input */
.stTextInput>div>div>input {
    width: 100% !important;
}

/* Chat bubbles responsive text wrapping */
.chat-bubble {
    max-width: 100%;
    word-wrap: break-word;
}
</style>
""", unsafe_allow_html=True)


# ==========================
# UTILITY FUNCTIONS
# ==========================
def load_api_client():
    """Initialize OpenAI client."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("❌ Missing OpenAI API Key! Please set OPENAI_API_KEY in your .env file.")
        st.stop()
    return OpenAI(api_key=api_key)


def ask_openai(client, messages):
    """Send messages to OpenAI API and return assistant response."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.3,
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"


def chat_bubble(role, text):
    """Beautiful chat bubbles for UI with responsive layout."""
    base_style = """
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 8px;
        max-width: 100%;
        word-wrap: break-word;
        font-size: 17px;
        display: inline-block;
    """

    if role == "user":
        style = f"{base_style} background-color:#DCF8C6;"
    else:
        style = f"{base_style} background-color:#FFFFFF; border:1px solid #ddd;"

    st.markdown(
        f"""
        <div class="chat-bubble" style="{style}">
            <b>{"You" if role == "user" else "AI"}:</b> {text}
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================
# SIDEBAR WITH QUICK BUTTONS
# ==========================
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg",
    use_container_width=True,
    caption="Paris – The City of Light"
)

st.sidebar.header("🌍 Quick Paris Topics")

quick_questions = [
    "Top 5 attractions in Paris",
    "Best time to visit Paris?",
    "Must-try foods in Paris",
    "How to get around Paris?",
    "Is the Louvre worth visiting?"
]

for q in quick_questions:
    if st.sidebar.button(q):
        st.session_state.user_input = q

# Reset chat button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.conversation = [
        {"role": "system", "content": (
            "You are an AI-powered Paris travel assistant. "
            "Provide concise, friendly, and accurate answers about Paris landmarks, museums, attractions, and food."
        )}
    ]
    st.sidebar.success("Chat cleared!")


# ==========================
# HERO HEADER — RESPONSIVE
# ==========================
st.markdown(
    """
    <style>
    .hero-container {
        background: linear-gradient(90deg, #1d2671, #c33764);
        padding: 30px 20px;
        border-radius: 12px;
        width: 100%;
        text-align: center;
        color: white;
    }
    @media (max-width: 768px) {
        .hero-container h1 {
            font-size: 28px !important;
        }
        .hero-container p {
            font-size: 16px !important;
        }
    }
    </style>

    <div class="hero-container">
        <h1>🗼 Paris AI Travel Guide</h1>
        <p>Your intelligent virtual companion for exploring the beauty and culture of Paris.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")


# ==========================
# SESSION INITIALIZATION
# ==========================
if "conversation" not in st.session_state:
    st.session_state.conversation = [
        {"role": "system", "content": (
            "You are an AI-powered Paris travel assistant. "
            "Provide concise, friendly, and accurate answers about Paris landmarks, museums, attractions, and food."
        )}
    ]

client = load_api_client()


# ==========================
# CHAT INPUT AREA
# ==========================
st.subheader("💬 Ask me anything about Paris")

user_input = st.text_input(
    "Your question:",
    placeholder="e.g., What should I visit first in Paris?",
    key="user_input"
)

if st.button("Send"):
    if user_input.strip():
        st.session_state.conversation.append({"role": "user", "content": user_input})

        with st.spinner("Thinking..."):
            answer = ask_openai(client, st.session_state.conversation)

            # Typing animation
            animated_text = ""
            placeholder = st.empty()
            for char in answer:
                animated_text += char
                time.sleep(0.01)
                placeholder.markdown(f"<div style='font-size:17px;'>{animated_text}</div>", unsafe_allow_html=True)

        st.session_state.conversation.append({"role": "assistant", "content": answer})
    else:
        st.warning("Please type a question before sending.")


# ==========================
# DISPLAY CHAT HISTORY
# ==========================
st.subheader("📝 Conversation History")

for msg in st.session_state.conversation[1:]:
    chat_bubble(msg["role"], msg["content"])


# ==========================
# FOOTER
# ==========================
st.markdown(
    """
    <hr>
    <div style="text-align:center; color:gray;">
        Built by <b>Olalemi John Oluwatosin</b> for Peterman Reality Tours · 2025  
        <br>Powered by OpenAI · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)