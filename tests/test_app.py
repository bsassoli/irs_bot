import os
import pytest
import yaml
from unittest.mock import MagicMock, patch, mock_open
from langchain_core.documents import Document

class TestConfig:
    def test_load_config(self):
        from irs_bot.app import load_config
        mock_config = {
            "key": "value"
        }
        with patch("builtins.open", mock_open(read_data=yaml.dump(mock_config))):
            config = load_config("dummy_path")
            assert config == mock_config
    
    def test_load_config_file_exists(self):
        from irs_bot.app import load_config
        config = load_config("config/config.yaml")
        assert isinstance(config, dict)
        
    def test_config_contains_openai_params(self):
        from irs_bot.app import load_config
        config = load_config("config/config.yaml")
        assert "openai" in config
        assert "embedding_model" in config["openai"]
        assert "temperature" in config["openai"]
        assert "completion_model" in config["openai"]

    def test_config_contains_chroma_params(self):
        from irs_bot.app import load_config
        config = load_config("config/config.yaml")
        assert "chromadb" in config
        assert "persist_directory" in config["chromadb"]
        assert "collection_name" in config["chromadb"]

    def test_config_contains_document_processing_params(self):
        from irs_bot.app import load_config
        config = load_config("config/config.yaml")
        assert "document_processing" in config
        assert "chunk_size" in config["document_processing"]
        assert "chunk_overlap" in config["document_processing"]


class TestChunkText:
    @pytest.fixture
    def mock_config(self):
        return {
            "document_processing": {
                "path_to_doc": "data/test_document.md",
                "chunk_size": 100,
                "chunk_overlap": 20,
                "headers_to_split_on": [
                    ["##", "Header 2"],
                    ["###", "Header 3"]
                ]
            }
        }
        
    @patch("irs_bot.app.UnstructuredMarkdownLoader")
    @patch("irs_bot.app.MarkdownHeaderTextSplitter")
    @patch("irs_bot.app.RecursiveCharacterTextSplitter")
    def test_chunk_text_basic(self, mock_text_splitter, mock_md_splitter, mock_loader, mock_config):
        from irs_bot.app import chunk_text
        
        # Create sample document
        mock_doc = Document(page_content="# Test Document\n\n## Section 1\n\nTest content 1\n\n## Section 2\n\nTest content 2")
        mock_loader.return_value.load.return_value = [mock_doc]
        
        # Setup markdown splitter return value
        split_docs = [
            Document(page_content="## Section 1\n\nTest content 1", metadata={"header_levels": ["Header 2"]}),
            Document(page_content="## Section 2\n\nTest content 2", metadata={"header_levels": ["Header 2"]})
        ]
        mock_md_splitter.return_value.split_text.return_value = split_docs
        
        # Setup recursive splitter return value
        final_chunks = [
            Document(page_content="## Section 1\n\nTest content 1", metadata={"header_levels": ["Header 2"]}),
            Document(page_content="## Section 2\n\nTest content 2", metadata={"header_levels": ["Header 2"]})
        ]
        mock_text_splitter.return_value.split_documents.return_value = final_chunks
        
        # Call the function
        chunks = chunk_text(mock_config)
        
        # Assert correct results
        assert chunks == final_chunks
        mock_loader.assert_called_once_with(mock_config["document_processing"]["path_to_doc"])
        mock_md_splitter.assert_called_once_with(headers_to_split_on=mock_config["document_processing"]["headers_to_split_on"], strip_headers=False)
        mock_text_splitter.assert_called_once_with(chunk_size=mock_config["document_processing"]["chunk_size"], 
                                                  chunk_overlap=mock_config["document_processing"]["chunk_overlap"], 
                                                  length_function=len)
        
    @patch("irs_bot.app.UnstructuredMarkdownLoader")
    @patch("irs_bot.app.MarkdownHeaderTextSplitter")
    @patch("irs_bot.app.RecursiveCharacterTextSplitter")
    def test_chunk_text_empty_document(self, mock_text_splitter, mock_md_splitter, mock_loader, mock_config):
        from irs_bot.app import chunk_text
        
        # Create empty document
        mock_doc = Document(page_content="")
        mock_loader.return_value.load.return_value = [mock_doc]
        
        # Empty result from markdown splitter
        mock_md_splitter.return_value.split_text.return_value = []
        
        # Empty chunks from text splitter
        mock_text_splitter.return_value.split_documents.return_value = []
        
        # Call the function
        chunks = chunk_text(mock_config)
        
        # Assert empty chunks
        assert chunks == []
        
    @patch("irs_bot.app.UnstructuredMarkdownLoader")
    @patch("irs_bot.app.MarkdownHeaderTextSplitter")
    @patch("irs_bot.app.RecursiveCharacterTextSplitter")
    def test_chunk_text_with_multiple_documents(self, mock_text_splitter, mock_md_splitter, mock_loader, mock_config):
        from irs_bot.app import chunk_text
        
        # Create multiple sample documents
        mock_docs = [
            Document(page_content="# Doc 1\n\n## Section 1\n\nContent 1"),
            Document(page_content="# Doc 2\n\n## Section 2\n\nContent 2")
        ]
        mock_loader.return_value.load.return_value = mock_docs
        
        # Setup markdown splitter to return different docs for each input
        mock_md_splitter.return_value.split_text.side_effect = [
            [Document(page_content="## Section 1\n\nContent 1", metadata={"header_levels": ["Header 2"]})],
            [Document(page_content="## Section 2\n\nContent 2", metadata={"header_levels": ["Header 2"]})]
        ]
        
        # Setup recursive splitter to return final chunks for each input
        chunk1 = Document(page_content="## Section 1\n\nContent 1", metadata={"header_levels": ["Header 2"]})
        chunk2 = Document(page_content="## Section 2\n\nContent 2", metadata={"header_levels": ["Header 2"]})
        mock_text_splitter.return_value.split_documents.side_effect = [[chunk1], [chunk2]]
        
        # Call the function
        chunks = chunk_text(mock_config)
        
        # Assert correct results
        assert len(chunks) == 2
        assert chunks == [chunk1, chunk2]
        
    def test_integration_chunk_text(self):
        """Integration test for chunk_text with actual config and file."""
        import tempfile
        from irs_bot.app import chunk_text, load_config
        
        # Create a temporary markdown file
        with tempfile.NamedTemporaryFile(suffix='.md', mode='w+', delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write("""# Test Document
            
## Section 1
            
This is content for section 1.
            
## Section 2
            
This is content for section 2.
            
### Subsection 2.1
            
This is content for subsection 2.1.
""")
            
        try:
            # Load actual config
            config = load_config("config/config.yaml")
            
            # Modify config to use our temporary file
            config["document_processing"]["path_to_doc"] = temp_path
            
            # Run chunk_text
            chunks = chunk_text(config)
            
            # Verify results
            assert len(chunks) > 0
            for chunk in chunks:
                assert hasattr(chunk, 'page_content')
                assert isinstance(chunk.page_content, str)
                assert len(chunk.page_content) > 0
                assert hasattr(chunk, 'metadata')
                
        finally:
            # Clean up temp file
            os.unlink(temp_path)


class TestChromaDB:
    @pytest.fixture
    def mock_config(self):
        return {
            "chromadb": {
                "persist_directory": "test_chromadb",
                "collection_name": "test_collection"
            },
            "openai": {
                "embedding_model": "text-embedding-3-small"
            }
        }
    
    @patch("irs_bot.app.PersistentClient")
    def test_create_chromadb_client(self, mock_persistent_client, mock_config):
        from irs_bot.app import create_chromadb_client
        
        # Setup mock
        mock_client = MagicMock()
        mock_persistent_client.return_value = mock_client
        
        # Call the function
        client = create_chromadb_client(mock_config)
        
        # Verify results
        assert client == mock_client
        mock_persistent_client.assert_called_once()
        # Verify directory was created
        assert os.path.exists(mock_config["chromadb"]["persist_directory"])
        
        # Clean up
        os.rmdir(mock_config["chromadb"]["persist_directory"])
    
    @patch("irs_bot.app.os.getenv")
    @patch("irs_bot.app.ef.OpenAIEmbeddingFunction")
    def test_create_openai_embedding_function(self, mock_embedding_function, mock_getenv, mock_config):
        from irs_bot.app import create_openai_embedding_function
        
        # Setup mocks
        mock_getenv.return_value = "test_api_key"
        mock_embedding = MagicMock()
        mock_embedding_function.return_value = mock_embedding
        
        # Call the function
        embedding_function = create_openai_embedding_function(mock_config)
        
        # Verify results
        assert embedding_function == mock_embedding
        mock_embedding_function.assert_called_once_with(
            api_key="test_api_key",
            model_name=mock_config["openai"]["embedding_model"]
        )
    
    @patch("irs_bot.app.create_openai_embedding_function")
    def test_create_chromadb_collection(self, mock_embedding_function, mock_config):
        from irs_bot.app import create_chromadb_collection
        
        # Setup mocks
        mock_client = MagicMock()
        mock_collection = MagicMock()
        mock_client.create_collection.return_value = mock_collection
        mock_embedding = MagicMock()
        mock_embedding_function.return_value = mock_embedding
        
        # Call the function
        collection = create_chromadb_collection(mock_client, mock_config)
        
        # Verify results
        assert collection == mock_collection
        mock_client.create_collection.assert_called_once_with(
            name=mock_config["chromadb"]["collection_name"],
            embedding_function=mock_embedding
        )
    
    def test_add_documents_to_chromadb(self):
        from irs_bot.app import add_documents_to_chromadb
        
        # Setup mocks
        mock_collection = MagicMock()
        mock_documents = ["doc1", "doc2", "doc3"]
        
        # Call the function
        add_documents_to_chromadb(mock_collection, mock_documents)
        
        # Verify the collection's add_documents method was called with the documents
        mock_collection.add_documents.assert_called_once_with(mock_documents)
    
    def test_query_chromadb(self):
        from irs_bot.app import query_chromadb
        
        # Setup mocks
        mock_collection = MagicMock()
        mock_results = [{"id": 1, "document": "doc1"}, {"id": 2, "document": "doc2"}]
        mock_collection.query.return_value = mock_results
        
        # Call the function
        results = query_chromadb(mock_collection, "test query")
        
        # Verify results
        assert results == mock_results
        mock_collection.query.assert_called_once_with("test query")

