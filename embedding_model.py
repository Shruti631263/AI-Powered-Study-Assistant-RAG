"""
embedding_model.py

Loads the HuggingFace embedding model.
"""

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from config import EMBEDDING_MODEL


def load_embedding_model():
    """
    Load HuggingFace embedding model.

    Returns:
        HuggingFaceEmbedding
    """

    embedding_model = HuggingFaceEmbedding(
        model_name=EMBEDDING_MODEL,
        trust_remote_code=True
    )

    return embedding_model


if __name__ == "__main__":

    model = load_embedding_model()

    print("=" * 60)
    print("Embedding Model Loaded Successfully")
    print("=" * 60)
    print(model)