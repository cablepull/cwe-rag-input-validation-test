# CWE-UNRAG: RAG Input Validation Test Suite

This repository demonstrates the vulnerability **Use of Untrusted Input in Retrieval-Augmented Generation (RAG) Prompt Construction**. It provides a minimal RAG pipeline and several tests that illustrate how untrusted input can manipulate large language models.

## Requirements
- Python 3.8+
- OpenAI API key

Install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file and set the API key:
```bash
OPENAI_API_KEY=sk-your-key
```

## Usage
1. Ingest the documents into the vector store:
    ```bash
    python app/ingest.py
    ```
2. Run the vulnerability tests:
    ```bash
    bash run_tests.sh
    ```

Test results will be printed to the console and stored in `test_outputs/logs.txt`.

## Repository Structure
```
.
├── app
│   ├── ingest.py
│   ├── rag_chain.py
│   └── test_cases.py
├── data
│   ├── clean_doc.txt
│   └── poisoned_doc.txt
├── run_tests.sh
└── requirements.txt
```

## Disclaimer
This code is intentionally vulnerable and should be used for educational purposes only.
