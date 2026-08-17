# 📚 AI Study Assistant

An AI-powered study assistant that allows users to upload PDF study materials and ask questions about their content using **Retrieval-Augmented Generation (RAG)**.

The application processes uploaded documents, retrieves relevant information using semantic search, and generates answers using **Google Gemini**.

---

## ✨ Features

* 📤 Upload one or multiple PDF documents directly from the application
* 📚 Support for study materials from any subject
* 🔎 Semantic search over uploaded documents
* 🧠 MiniLM-based text embeddings
* 🤖 Google Gemini for answer generation
* 💬 Interactive chat interface
* 🗑 Remove uploaded documents
* 🔄 Rebuild the document index after document changes
* 🌙 Clean dark-themed user interface
* ⚡ RAG-based question answering

---

## 🛠️ Technologies Used

| Technology         | Purpose                         |
| ------------------ | ------------------------------- |
| Python             | Core programming language       |
| Streamlit          | User interface                  |
| LlamaIndex         | RAG pipeline and indexing       |
| Google Gemini      | Answer generation               |
| HuggingFace MiniLM | Text embeddings                 |
| PyMuPDF            | PDF text extraction             |
| python-dotenv      | Environment variable management |

---

## 🧠 How the System Works

```text
User
  ↓
Upload PDF
  ↓
PDF Text Extraction
  ↓
Text Chunking
  ↓
MiniLM Embeddings
  ↓
Vector Index
  ↓
User Question
  ↓
Semantic Retrieval
  ↓
Relevant Document Context
  ↓
Google Gemini
  ↓
Final Answer
```

---

## 📂 Project Structure

```text
AI-Powered-Study-Assistant-RAG/
│
├── data/
│   └── Uploaded PDF documents
│
├── screenshots/
│   ├── home.png
│   ├── document.png
│   └── question1.png
    └── question2.png
│
├── app.py
├── config.py
├── document_loader.py
├── embedding_model.py
├── llm_model.py
├── prompts.py
├── query_engine.py
├── rag_pipeline.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📸 Screenshots

### 🏠 Home Interface

![Home Interface](screenshots/home.png)

### 📤 PDF Upload

![PDF Upload](screenshots/document.png)

### 💬 AI Chat

![AI Chat](screenshots/question1.png)

![AI Chat](screenshots/question2.png)

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shruti631263/AI-Powered-Study-Assistant-RAG.git
```

### 2. Open the Project

```bash
cd AI-Powered-Study-Assistant-RAG
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

> Do not upload the `.env` file or your API key to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📖 How to Use

1. Open the application.
2. Upload one or more PDF documents using the upload area.
3. The documents are processed and indexed.
4. Ask questions about the uploaded content.
5. The RAG system retrieves relevant information.
6. Google Gemini generates the final response.
7. Documents can be removed from the sidebar when no longer needed.

---

## 🔍 Example Use Cases

The application is not limited to one subject.

Users can upload PDFs related to:

* Mathematics
* History
* English
* Science
* Computer Science
* Data Science
* Programming
* College notes
* Textbooks
* Assignments
* Any other study material in PDF format

---

## 🧩 Configuration

The project includes configurable settings for:

* Gemini model
* Embedding model
* Chunk size
* Chunk overlap
* Retrieval count
* Data and upload directories

---

## 🚀 Future Improvements

* 📌 Source and page-level citations
* 💾 Persistent chat history
* 🔐 User authentication
* 📝 Automatic document summarization
* ❓ AI-generated quizzes
* 🃏 Flashcard generation
* 🎤 Voice-based interaction
* 🌐 Multi-language support
* ⚛️ Production frontend using React

---

## 👩‍💻 Developer

**Shruti Deshmukh**

MCA Student | Data Science & AI Enthusiast

---

## 📄 License

This project is developed for educational and learning purposes.

---

⭐ If you find this project useful, consider giving the repository a star.
