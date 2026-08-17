import os
import hashlib
import streamlit as st

from query_engine import StudyAssistant
from config import DATA_FOLDER


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title=" AI Study Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide Streamlit toolbar / Deploy
st.set_option("client.toolbarMode", "minimal")


# ============================================================
# DATA FOLDER
# ============================================================

os.makedirs(DATA_FOLDER, exist_ok=True)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "processed_uploads" not in st.session_state:
    st.session_state.processed_uploads = set()


# ============================================================
# RAG ASSISTANT
# ============================================================

@st.cache_resource
def load_assistant():
    return StudyAssistant()


assistant = load_assistant()


# ============================================================
# FUNCTIONS
# ============================================================

def get_pdf_files():
    if not os.path.exists(DATA_FOLDER):
        return []

    return sorted(
        [
            f
            for f in os.listdir(DATA_FOLDER)
            if f.lower().endswith(".pdf")
        ]
    )


def file_hash(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def save_uploaded_pdf(uploaded_file):
    filename = os.path.basename(uploaded_file.name)
    path = os.path.join(DATA_FOLDER, filename)

    content = uploaded_file.getvalue()
    new_hash = file_hash(content)

    if os.path.exists(path):
        with open(path, "rb") as f:
            old_hash = file_hash(f.read())

        if old_hash == new_hash:
            return False

    with open(path, "wb") as f:
        f.write(content)

    return True


def rebuild_assistant():
    load_assistant.clear()
    st.session_state.messages = []


def delete_pdf(filename):
    path = os.path.join(DATA_FOLDER, filename)

    if os.path.exists(path):
        os.remove(path)

    rebuild_assistant()
    st.rerun()


# ============================================================
# DARK THEME + HIDE STREAMLIT CONTROLS
# ============================================================

st.markdown(
    """
    <style>

    /* ------------------------------------------------------
       HIDE STREAMLIT DEPLOY / TOOLBAR
    ------------------------------------------------------ */

    [data-testid="stAppDeployButton"] {
        display: none !important;
    }

    [data-testid="stToolbar"] {
        display: none !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }


    /* ------------------------------------------------------
       APP BACKGROUND
    ------------------------------------------------------ */

    .stApp {
        background: #0B0F17;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 42px;
        padding-bottom: 50px;
        padding-left: 42px;
        padding-right: 42px;
    }


    /* ------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------ */

    section[data-testid="stSidebar"] {
        background: #11151F;
        border-right: 1px solid #252B39;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 28px;
    }


    /* ------------------------------------------------------
       TEXT
    ------------------------------------------------------ */

    h1, h2, h3, h4, h5 {
        color: #F7F8FC !important;
    }

    p, label {
        color: #AEB6C6;
    }


    /* ------------------------------------------------------
       MAIN TITLE
    ------------------------------------------------------ */

    h1 {
        font-size: 42px !important;
        font-weight: 750 !important;
        letter-spacing: -1px;
    }


    /* ------------------------------------------------------
       BUTTONS
    ------------------------------------------------------ */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid #30384B;
        background: #171C27;
        color: #E9EDF5;
        font-weight: 600;
        min-height: 42px;
    }

    .stButton > button:hover {
        border-color: #7756E8;
        background: #1C2230;
        color: #FFFFFF;
    }


    /* ------------------------------------------------------
       PRIMARY BUTTON
    ------------------------------------------------------ */

    button[kind="primary"] {
        background: #6D45E8 !important;
        border-color: #6D45E8 !important;
        color: white !important;
    }

    button[kind="primary"]:hover {
        background: #7B57F0 !important;
    }


    /* ------------------------------------------------------
       FILE UPLOADER
    ------------------------------------------------------ */

    div[data-testid="stFileUploader"] {
        background: #101621;
        border: 1px dashed #6452A7;
        border-radius: 18px;
        padding: 10px;
    }

    div[data-testid="stFileUploader"] section {
        background: transparent;
        border: none;
    }

    div[data-testid="stFileUploader"] small {
        color: #737F94;
    }


    /* ------------------------------------------------------
       CHAT
    ------------------------------------------------------ */

    div[data-testid="stChatMessage"] {
        background: #111722;
        border: 1px solid #232C3D;
        border-radius: 16px;
        padding: 14px 18px;
        margin-bottom: 14px;
    }

    div[data-testid="stChatMessage"] p {
        color: #E9EDF5;
        line-height: 1.7;
    }


    /* ------------------------------------------------------
       CHAT INPUT
    ------------------------------------------------------ */

    div[data-testid="stChatInput"] {
        background: #111722;
        border: 1px solid #343D52;
        border-radius: 15px;
    }

    div[data-testid="stChatInput"] textarea {
        color: #FFFFFF !important;
    }


    /* ------------------------------------------------------
       INFO / SUCCESS
    ------------------------------------------------------ */

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }


    /* ------------------------------------------------------
       EXPANDER
    ------------------------------------------------------ */

    div[data-testid="stExpander"] {
        background: #111722;
        border: 1px solid #252D3E;
        border-radius: 12px;
    }


    /* ------------------------------------------------------
       DIVIDER
    ------------------------------------------------------ */

    hr {
        border-color: #252C3A;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("📚 AI Study")

    st.caption(" 📚 Your AI Study Assistant")

    st.divider()

    if st.button(
        "＋  New Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### Documents")

    pdf_files = get_pdf_files()

    if pdf_files:

        for pdf in pdf_files:

            file_path = os.path.join(
                DATA_FOLDER,
                pdf
            )

            try:
                size_mb = os.path.getsize(file_path) / (
                    1024 * 1024
                )
                size_text = f"{size_mb:.2f} MB"
            except Exception:
                size_text = "PDF"

            st.write(f"📄 {pdf}")
            st.caption(size_text)

            if st.button(
                "Remove",
                key=f"remove_{pdf}",
                use_container_width=True
            ):
                delete_pdf(pdf)

    else:
        st.caption("No documents uploaded yet.")

    st.divider()

    if st.button(
        "🗑  Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.title(" 📚 AI Study Assistant")

st.caption(
    "Upload your study material and ask anything about its content."
)


# ============================================================
# UPLOAD SECTION
# ============================================================

st.subheader("Upload your study material")

st.caption(
    "Notes, textbooks, assignments or PDFs from any subject."
)

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type=["pdf"],
    accept_multiple_files=True,
    help="You can upload one or more PDF files."
)


# ============================================================
# SAVE UPLOADS
# ============================================================

new_files = []

if uploaded_files:

    for uploaded_file in uploaded_files:

        upload_key = (
            uploaded_file.name,
            file_hash(uploaded_file.getvalue())
        )

        if upload_key not in st.session_state.processed_uploads:

            saved = save_uploaded_pdf(
                uploaded_file
            )

            st.session_state.processed_uploads.add(
                upload_key
            )

            if saved:
                new_files.append(
                    uploaded_file.name
                )


# ============================================================
# AUTO PROCESS
# ============================================================

if new_files:

    with st.spinner(
        "Processing your documents..."
    ):
        rebuild_assistant()

    st.success(
        f"{len(new_files)} document(s) uploaded and processed."
    )

    st.rerun()


# ============================================================
# DOCUMENT STATUS
# ============================================================

pdf_files = get_pdf_files()

if pdf_files:

    st.caption(
        f"{len(pdf_files)} document(s) available for questions."
    )

else:

    st.info(
        "Upload a PDF above to start your study session."
    )


# ============================================================
# CHAT AREA
# ============================================================

st.divider()

st.subheader("💬 Ask anything about your documents")

if not st.session_state.messages:

    if pdf_files:

        st.info(
            "Your document is ready. "
            "Ask any question about its content."
        )

    else:

        st.info(
            "Upload a PDF and your chat will appear here."
        )


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )


# ============================================================
# INPUT
# ============================================================

question = st.chat_input(
    "Ask anything about your documents..."
)


# ============================================================
# QUESTION
# ============================================================

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching your documents..."
        ):

            try:

                answer = assistant.ask(
                    question
                )

            except Exception as e:

                answer = (
                    "Sorry, something went wrong.\n\n"
                    f"Error: `{str(e)}`"
                )

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Study • Ask questions from your uploaded documents"
)