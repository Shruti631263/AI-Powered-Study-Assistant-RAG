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

        print("Initializing RAG Pipeline...\n")

        self.pipeline = RAGPipeline()

        # Load embedding model and Gemini
        self.pipeline.initialize()

        # Load PDFs and build vector index
        self.pipeline.build_index()

        # Create query engine
        self.query_engine = (
            self.pipeline.create_query_engine()
        )

        print("\nStudy Assistant Ready!\n")


    def ask(self, question: str):
        """
        Ask a question to the RAG system.

        Args:
            question: User's question.

        Returns:
            Generated answer as a string.
        """

        if not question or not question.strip():

            return "⚠️ Please enter a valid question."


        try:

            response = self.query_engine.query(
                question
            )

            return str(response)


        except Exception as e:

            error = str(e)


            # Gemini quota error
            if "429" in error:

                return (
                    "⚠️ Gemini API quota exceeded.\n\n"
                    "Please wait for the quota to reset "
                    "or use another Gemini API key."
                )


            # Gemini temporary server error
            if "503" in error:

                return (
                    "⚠️ Gemini service is temporarily busy.\n\n"
                    "Please try again after a few seconds."
                )


            # Invalid API key
            if "401" in error:

                return (
                    "⚠️ Invalid Gemini API key.\n\n"
                    "Please check your .env file."
                )


            return (
                "❌ An error occurred while processing "
                "your question.\n\n"
                f"Details: {error}"
            )


# ============================================================
# TERMINAL TEST
# ============================================================

if __name__ == "__main__":

    assistant = StudyAssistant()

    print("=" * 60)
    print("AI-Powered Study Assistant")
    print("Type 'exit' to quit.")
    print("=" * 60)


    while True:

        question = input(
            "\nAsk a Question: "
        )


        if question.lower().strip() in [
            "exit",
            "quit"
        ]:

            print("\nGoodbye!")

            break


        answer = assistant.ask(
            question
        )


        print("\nAnswer:\n")

        print(answer)