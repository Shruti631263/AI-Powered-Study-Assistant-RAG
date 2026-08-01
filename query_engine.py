"""
query_engine.py

Handles user queries using the RAG pipeline.
"""

from rag_pipeline import RAGPipeline


class StudyAssistant:
    """
    AI-Powered Study Assistant
    """

    def __init__(self):

        self.pipeline = RAGPipeline()

        print("Initializing RAG Pipeline...\n")

        self.pipeline.initialize()

        self.pipeline.build_index()

        self.query_engine = self.pipeline.create_query_engine()

        print("\nStudy Assistant Ready!\n")

    def ask(self, question: str):
        """
        Ask a question to the RAG system.
        """

        if not question.strip():
            return "⚠️ Please enter a valid question."

        try:

            response = self.query_engine.query(question)

            return str(response)

        except Exception as e:

            error = str(e)

            if "429" in error:
                return """
⚠️ Gemini API quota exceeded.

You have reached the free API limit.

Please wait for the quota to reset or use another Gemini API Key.
"""

            elif "503" in error:
                return """
⚠️ Gemini service is temporarily busy.

Please try again after a few seconds.
"""

            elif "401" in error:
                return """
⚠️ Invalid Gemini API Key.

Please check your .env file.
"""

            return f"❌ Error:\n\n{error}"


if __name__ == "__main__":

    assistant = StudyAssistant()

    print("=" * 60)
    print("AI-Powered Study Assistant")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        question = input("\nAsk a Question: ")

        if question.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break

        answer = assistant.ask(question)

        print("\nAnswer:\n")

        print(answer)