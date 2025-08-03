import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()


def main():
    docs = []
    for name in ["clean_doc.txt", "poisoned_doc.txt"]:
        loader = TextLoader(os.path.join("..", "data", name))
        docs.extend(loader.load())

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    splits = splitter.split_documents(docs)

    db = Chroma.from_documents(
        splits,
        embedding=OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY")),
        persist_directory="../db",
    )
    db.persist()


if __name__ == "__main__":
    main()
