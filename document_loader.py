import os

from llama_index.readers.file import PyMuPDFReader

from config import DATA_FOLDER
from utils import validate_pdf, print_error, print_success


def load_documents():
    """
    Load all valid PDF documents from the data folder.
    """

    if not os.path.exists(DATA_FOLDER):
        raise FileNotFoundError(
            "Data folder does not exist."
        )

    pdf_files = [
        os.path.join(DATA_FOLDER, file)
        for file in os.listdir(DATA_FOLDER)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF found. Please upload a PDF first."
        )

    reader = PyMuPDFReader()

    documents = []

    for pdf in pdf_files:

        if not validate_pdf(pdf):
            print_error(
                f"Invalid PDF: {os.path.basename(pdf)}"
            )
            continue

        try:

            docs = reader.load(
                file_path=pdf
            )

            documents.extend(docs)

            print_success(
                f"Loaded: {os.path.basename(pdf)}"
            )

        except Exception as e:

            print_error(
                f"Failed to load {os.path.basename(pdf)}: {e}"
            )

    if not documents:
        raise ValueError(
            "No valid PDF documents could be loaded."
        )

    return documents


if __name__ == "__main__":

    documents = load_documents()

    print(
        f"\nTotal documents loaded: {len(documents)}"
    )

    if documents:
        print(
            "\nSample extracted text:\n"
        )

        print(
            documents[0].text[:3000]
        )