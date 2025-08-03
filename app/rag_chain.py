import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()


def get_rag_chain():
    db = Chroma(
        embedding_function=OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY")),
        persist_directory="../db",
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY")),
        retriever=db.as_retriever(search_kwargs={"k": 1}),
        return_source_documents=True,
    )
    return qa_chain


def query_rag(text: str) -> str:
    chain = get_rag_chain()
    return chain.run(text)
