from ingest import reset_db, ingest_documents, remove_documents
from test_cases import test_clean_input, test_injected_query, test_poisoned_doc


def run_all_tests():
    """Run the original test suite to inspect responses."""
    test_clean_input()
    test_injected_query()
    test_poisoned_doc()


if __name__ == "__main__":
    reset_db()
    ingest_documents(["clean_doc.txt"])
    print("\n[Base: clean_doc.txt]")
    run_all_tests()

    for name in ["extra_clean_doc.txt", "poisoned_doc.txt", "extra_poisoned_doc.txt"]:
        print(f"\n[Adding {name}]")
        ingest_documents([name])
        run_all_tests()
        print(f"[Removing {name}]")
        remove_documents([name])
