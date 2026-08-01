"""
config.py

Central configuration file for the AI-Powered Study Assistant.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===========================
# API Configuration
# ===========================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ===========================
# Gemini Configuration
# ===========================
LLM_MODEL = "gemini-3.6-flash" # ===========================
# Embedding Model
# ===========================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ===========================
# Text Chunking
# ===========================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# ===========================
# Retrieval
# ===========================

TOP_K = 3

# ===========================
# Folder Paths
# ===========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
VECTOR_STORE = os.path.join(BASE_DIR, "vector_store")

# ===========================
# Supported File Types
# ===========================

SUPPORTED_FILES = [".pdf"] 