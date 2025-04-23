import pytest

@pytest.fixture
def config():
    """
    Fixture to provide a test configuration dictionary.
    """
    return {
        "document_processing": {
            "path_to_doc": "data/complete_text.md",
            "chunk_size": 100,
            "chunk_overlap": 20,
            "headers_to_split_on": ["##", "###", "####", "#####"]
        }
    }