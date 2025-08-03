import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()


def get_rag_chain():
    db = Chroma(
        embedding_function=OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY")),
        persist_directory="db",
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY")),
        retriever=db.as_retriever(search_kwargs={"k": 1}),
        return_source_documents=True,
    )
    return qa_chain


def query_rag(text: str) -> str:
    chain = get_rag_chain()
    result = chain.invoke({"query": text})
    print("[Retrieved Documents]")
    for doc in result.get("source_documents", []):
        print(f"- {doc.page_content}")
    return result["result"]
