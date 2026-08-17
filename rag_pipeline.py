"""
rag_pipeline.py

Creates and manages the RAG pipeline.
"""

from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceSplitter

from document_loader import load_documents
from embedding_model import load_embedding_model
from llm_model import load_llm
from prompts import QA_PROMPT

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K
)


class RAGPipeline:
    """
    Complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(self):
        self.documents = None
        self.index = None
        self.query_engine = None

    # ========================================================
    # INITIALIZE MODELS
    # ========================================================

    def initialize(self):

        print("Loading embedding model...")

        Settings.embed_model = load_embedding_model()

        print("Loading Gemini model...")

        Settings.llm = load_llm()

        print("Configuring text splitter...")

        Settings.text_splitter = SentenceSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

    # ========================================================
    # LOAD DOCUMENTS + BUILD VECTOR INDEX
    # ========================================================

    def build_index(self):

        print("Loading documents...")

        self.documents = load_documents()

        if not self.documents:
            raise ValueError(
                "No documents available to build the vector index."
            )

        print(
            f"{len(self.documents)} document(s) loaded."
        )

        print("Building vector index...")

        self.index = VectorStoreIndex.from_documents(
            self.documents
        )

        print(
            "Vector index created successfully."
        )

    # ========================================================
    # CREATE QUERY ENGINE
    # ========================================================

    def create_query_engine(self):

        if self.index is None:
            raise ValueError(
                "Vector index is not available."
            )

        self.query_engine = self.index.as_query_engine(
            similarity_top_k=TOP_K,
            response_mode="compact",
            text_qa_template=QA_PROMPT
        )

        print(
            f"Query engine ready. TOP_K = {TOP_K}"
        )

        return self.query_engine


# ============================================================
# TEST PIPELINE
# ============================================================

if __name__ == "__main__":

    pipeline = RAGPipeline()

    pipeline.initialize()

    pipeline.build_index()

    pipeline.create_query_engine()

    print(
        "\nRAG Pipeline Initialized Successfully!"
    )