"""
llm_model.py

Loads the Google Gemini LLM.
"""

from llama_index.llms.google_genai import GoogleGenAI
from config import GOOGLE_API_KEY, LLM_MODEL


def load_llm():
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found in .env")

    return GoogleGenAI(
        model=LLM_MODEL,
        api_key=GOOGLE_API_KEY,
        temperature=0.2,
    )


if __name__ == "__main__":
    llm = load_llm()
    print("Gemini LLM Loaded Successfully!")
    print(llm)