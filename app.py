import os
import streamlit as st

from query_engine import StudyAssistant

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI-Powered Study Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD ASSISTANT
# ==========================================

@st.cache_resource
def load_assistant():
    return StudyAssistant()

assistant = load_assistant()

# ==========================================
# SESSION
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# PDF COUNT
# ==========================================

pdf_folder = "data"

if os.path.exists(pdf_folder):

    pdf_files = [
        f
        for f in os.listdir(pdf_folder)
        if f.endswith(".pdf")
    ]

else:

    pdf_files = []

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

.stApp{

background:#0F1117;

}

.block-container{

padding-top:35px;
padding-left:50px;
padding-right:50px;

}

div[data-testid="stMetric"]{

background:#181A20;

padding:18px;

border-radius:15px;

border:1px solid #262A34;

text-align:center;

}

div[data-testid="stMetric"]:hover{

border:1px solid #7C5CFF;

}

hr{

border-color:#242832;

}

/* ==========================================
SIDEBAR
========================================== */

section[data-testid="stSidebar"]{

background:#171A21;

border-right:1px solid #242832;

}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{

color:white;

}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label{

color:#C9CDD5;

}

/* Button */

.stButton>button{

width:100%;

border-radius:10px;

border:1px solid #303540;

background:#232730;

color:white;

}

.stButton>button:hover{

border:1px solid #7C5CFF;

background:#2C3140;

}

/* Success Box */

div[data-testid="stAlert"]{

border-radius:12px;

}
/* ==========================================
CHAT
========================================== */

div[data-testid="stChatMessage"]{

background:#181A20;

border:1px solid #262A34;

border-radius:15px;

padding:12px;

margin-bottom:12px;

}

/* Chat Input */

div[data-testid="stChatInput"]{

background:#181A20;

border-top:1px solid #242832;

padding-top:10px;

}

/* Spinner */

div[data-testid="stSpinner"]{

color:white;

}
/* ==========================================
INFO BOXES
========================================== */

div[data-testid="stInfo"]{

border-radius:12px;

border:1px solid #303540;

background:#171A21;

}

div[data-testid="stSuccess"]{

border-radius:12px;

}

/* Divider */

hr{

border-color:#2B303B;

}
/* ==========================================
FINAL POLISH
========================================== */

.stMetric{

border-radius:15px;

}

.stMetric:hover{

transform:scale(1.02);

transition:0.25s;

}

.stChatMessage{

border-radius:15px;

}

.stButton>button{

transition:0.25s;

}

.stButton>button:hover{

transform:translateY(-2px);

}
</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.title("📚 AI-Powered Study Assistant")

st.caption(
    "Ask questions from your uploaded study materials using AI."
)

st.write("")

# ==========================================
# DASHBOARD
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(

        "📄 Loaded Documents",

        len(pdf_files)

    )

with col2:

    st.metric(

        "🤖 AI Model",

        "Gemini"

    )

with col3:

    st.metric(

        "🧠 Embedding",

        "MiniLM"

    )

st.divider()

# ==========================================
# CHAT TITLE
# ==========================================

st.subheader("💬 Ask Your Question")

st.caption(
    "Ask anything related to your uploaded PDFs."
)
# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("## 🧠 Study Assistant")

    st.success("🟢 System Ready")

    st.divider()

    # --------------------------------------

    st.subheader("📚 Loaded PDFs")

    if pdf_files:

        for pdf in pdf_files:
            st.write(f"✅ {pdf}")

    else:

        st.warning("No PDF Found")

    st.divider()

    # --------------------------------------

    st.subheader("📊 Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("PDFs", len(pdf_files))

    with col2:
        st.metric("Chat", len(st.session_state.messages))

    st.divider()

    # --------------------------------------

    st.subheader("⚙ Technologies")

    st.markdown("""
✅ Gemini

✅ LlamaIndex

✅ MiniLM

✅ PyMuPDF

✅ Streamlit
""")

    st.divider()

    # --------------------------------------

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.caption("👩‍💻 Developed by")
    st.write("**Shruti Deshmukh**")

    # ==========================================
# CHAT SECTION
# ==========================================

st.write("")

question = st.chat_input(
    "Ask anything from your uploaded PDFs..."
)

# ==========================================
# DISPLAY OLD CHAT
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ==========================================
# USER QUESTION
# ==========================================

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # ======================================
    # AI RESPONSE
    # ======================================

    with st.chat_message("assistant"):

        with st.spinner("Searching your study materials..."):

            try:

                answer = assistant.ask(question)

            except Exception as e:

                answer = f"❌ Error : {e}"

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()
    # ============================================================
# QUICK ACCESS PANEL
# ============================================================

st.write("")
st.divider()

left, right = st.columns([2, 1], gap="large")

# ============================================================
# LEFT PANEL
# ============================================================

with left:

    st.subheader("💡 Example Questions")

    st.caption("Try asking one of these questions:")

    example_questions = [

        "What is Machine Learning?",

        "Explain Deep Learning.",

        "What is NumPy?",

        "What is Pandas?",

        "Explain Classification.",

        "What is Overfitting?",

        "Explain Data Science."

    ]

    for q in example_questions:

        st.info(q)


# ============================================================
# RIGHT PANEL
# ============================================================

with right:

    st.subheader("⚡ Quick Tips")

    st.success("✔ Upload multiple PDFs")

    st.success("✔ Ask complete questions")

    st.success("✔ Ask topic-wise questions")

    st.success("✔ AI answers only from uploaded PDFs")

    st.write("")

    st.subheader("📌 Project")

    st.write("**Name**")
    st.write("AI-Powered Study Assistant")

    st.write("**Technology**")
    st.write("Gemini + LlamaIndex")

    st.write("**Embedding**")
    st.write("MiniLM")

    st.write("**Framework**")
    st.write("Streamlit")

    st.write("")

    st.success("✅ Project Ready")
    # ============================================================
# FINAL DIVIDER
# ============================================================

st.write("")
st.divider()

# ============================================================
# PROJECT INFO
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "📄 PDFs Loaded",
        len(pdf_files)
    )

with col2:

    st.metric(
        "🤖 AI Model",
        "Gemini"
    )

with col3:

    st.metric(
        "🧠 Embedding",
        "MiniLM"
    )

st.write("")

# ============================================================
# FINAL MESSAGE
# ============================================================

st.success(
    "🎉 Your AI-Powered Study Assistant is ready to answer questions from your uploaded documents."
)

st.info(
    "💡 Tip: Upload multiple PDFs and ask natural language questions for the best results."
)

st.write("")

# ============================================================
# FOOTER
# ============================================================

st.markdown(
"""
---
""")

footer_left, footer_center, footer_right = st.columns([1,2,1])

with footer_center:

    st.markdown(
        """
<div style='text-align:center;color:#9CA3AF;'>

<h4 style="color:white;margin-bottom:5px;">
📚 AI-Powered Study Assistant
</h4>

Built with ❤️ using

Python • Streamlit • Gemini • LlamaIndex • HuggingFace • PyMuPDF

<br><br>

© 2026 Shruti Deshmukh

</div>
""",
unsafe_allow_html=True
    )