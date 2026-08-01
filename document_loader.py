import os

from llama_index.readers.file import PyMuPDFReader

from config import DATA_FOLDER
from utils import validate_pdf, print_error, print_success


def load_documents():

    pdf_files = []

    for file in os.listdir(DATA_FOLDER):
        if file.lower().endswith(".pdf"):
            pdf_files.append(os.path.join(DATA_FOLDER, file))

    if not pdf_files:
        raise FileNotFoundError("No PDF found.")

    reader = PyMuPDFReader()

    documents = []

    for pdf in pdf_files:

        if validate_pdf(pdf):

            docs = reader.load(file_path=pdf)

            documents.extend(docs)

            print_success(f"Loaded {os.path.basename(pdf)}")

        else:
            print_error(f"Invalid PDF : {pdf}")

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print(docs[0].text[:3000])