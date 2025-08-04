import os
import shutil
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()


def reset_db() -> None:
    """Remove the persistent database directory if it exists."""
    shutil.rmtree("db", ignore_errors=True)


def ingest_documents(doc_names: list[str]) -> None:
    """Ingest a list of documents into the persistent Chroma database.

    The function can be called multiple times to iteratively build up the
    knowledge base.
    """

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    db = Chroma(embedding_function=embedding, persist_directory="db")

    for name in doc_names:
        loader = TextLoader(os.path.join("data", name))
        docs = loader.load()
        splits = splitter.split_documents(docs)
        db.add_documents(splits)


def remove_documents(doc_names: list[str]) -> None:
    """Delete documents from the persistent Chroma database by filename."""

    embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    db = Chroma(embedding_function=embedding, persist_directory="db")

    for name in doc_names:
        db.delete(where={"source": os.path.join("data", name)})


def main():
    reset_db()
    ingest_documents(["clean_doc.txt", "extra_clean_doc.txt", "poisoned_doc.txt", "extra_poisoned_doc.txt"])


if __name__ == "__main__":
    main()
