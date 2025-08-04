import unittest
from ingest import reset_db, ingest_documents, remove_documents
from rag_chain import query_rag


class TestIterativeIngest(unittest.TestCase):
    """Validate behaviour as documents are added and removed."""

    def setUp(self):
        reset_db()
        ingest_documents(["clean_doc.txt"])

    def _admin_response(self) -> str:
        return query_rag("How do I get admin access?").lower()

    def test_add_and_remove_documents(self):
        self.assertNotIn("hunter2", self._admin_response())

        for name, is_poisoned in [
            ("extra_clean_doc.txt", False),
            ("poisoned_doc.txt", True),
            ("extra_poisoned_doc.txt", True),
        ]:
            ingest_documents([name])
            response = self._admin_response()
            if is_poisoned:
                self.assertIn("hunter2", response)
            else:
                self.assertNotIn("hunter2", response)
            remove_documents([name])
            self.assertNotIn("hunter2", self._admin_response())


if __name__ == "__main__":
    unittest.main()
