import os
import pytest
import yaml
from unittest.mock import MagicMock, patch, mock_open
from langchain_core.documents import Document
from chromadb import Settings

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
        assert "headers_to_split_on" in config["document_processing"]
        assert "path_to_doc" in config["document_processing"]

    def test_config_contains_query_params(self):
        from irs_bot.app import load_config
        config = load_config("config/config.yaml")
        assert "query" in config
        assert "n_results" in config["query"]


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
                "embedding_model": "text-embedding-3-small",
                "completion_model": "gpt-4o",
                "temperature": 0.3
            },
            "query": {
                "n_results": 3
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
        mock_persistent_client.assert_called_once_with(
            path=mock_config["chromadb"]["persist_directory"],
            settings=Settings(anonymized_telemetry=False)
        )
        
        # Create directory to simulate that it exists (for cleanup)
        os.makedirs(mock_config["chromadb"]["persist_directory"], exist_ok=True)
        
        # Clean up
        os.rmdir(mock_config["chromadb"]["persist_directory"])
    
    @patch("irs_bot.app.ef.OpenAIEmbeddingFunction")
    def test_create_chromadb_collection(self, mock_embedding_function, mock_config):
        from irs_bot.app import create_chromadb_collection
        
        # Setup mocks
        mock_client = MagicMock()
        mock_collection = MagicMock()
        mock_client.get_or_create_collection.return_value = mock_collection
        mock_embedding = MagicMock()
        mock_embedding_function.return_value = mock_embedding
        api_key = "test_api_key"
        
        # Call the function
        collection = create_chromadb_collection(mock_client, mock_config, api_key)
        
        # Verify results
        assert collection == mock_collection
        mock_embedding_function.assert_called_once_with(
            api_key=api_key,
            model_name=mock_config["openai"]["embedding_model"]
        )
        mock_client.get_or_create_collection.assert_called_once_with(
            name=mock_config["chromadb"]["collection_name"],
            embedding_function=mock_embedding
        )
    
    def test_add_documents_to_chromadb(self):
        from irs_bot.app import add_documents_to_chromadb
        
        # Setup mocks
        mock_collection = MagicMock()
        mock_documents = [
            Document(page_content="Document 1", metadata={"source": "source1"}),
            Document(page_content="Document 2", metadata={"source": "source2"}),
            Document(page_content="Document 3", metadata={})
        ]
        
        # Call the function
        add_documents_to_chromadb(mock_collection, mock_documents)
        
        # Verify the collection's add method was called correctly
        mock_collection.add.assert_called_once()
        
        # Check the arguments
        args, kwargs = mock_collection.add.call_args
        
        # Verify documents and IDs
        assert "documents" in kwargs
        assert "ids" in kwargs
        assert "metadatas" in kwargs
        
        # Check document contents match
        assert kwargs["documents"] == ["Document 1", "Document 2", "Document 3"]
        
        # Check IDs are correctly generated
        assert len(kwargs["ids"]) == 3
        assert all(id.startswith("doc_") for id in kwargs["ids"])
        
        # Check metadatas are correctly extracted
        assert kwargs["metadatas"] == [{"source": "source1"}, {"source": "source2"}, {"source": "unknown"}]
    
    def test_query_chromadb(self, mock_config):
        from irs_bot.app import query_chromadb
        
        # Setup mocks
        mock_collection = MagicMock()
        mock_query = "Test query"
        
        # Set up mock return value for collection.query
        mock_return = {
            "documents": [["doc1", "doc2", "doc3"]],
            "metadatas": [[{"source": "src1"}, {"source": "src2"}, {"source": "src3"}]],
            "ids": [["id1", "id2", "id3"]],
            "distances": [[0.1, 0.2, 0.3]]
        }
        mock_collection.query.return_value = mock_return
        
        # Call the function
        results = query_chromadb(mock_collection, mock_config, mock_query)
        
        # Verify the collection's query method was called correctly
        mock_collection.query.assert_called_once_with(
            query_texts=[mock_query],
            n_results=mock_config["query"]["n_results"],
            include=["documents", "metadatas", "distances"]
        )
        
        # Check the structure of the returned results
        assert len(results) == 3
        
        # Check the content of the results
        assert results[0]["text"] == "doc1"
        assert results[0]["metadata"] == {"source": "src1"}
        assert results[0]["id"] == "id1"
        assert results[0]["distance"] == 0.1
        
        assert results[1]["text"] == "doc2"
        assert results[2]["text"] == "doc3"


class TestChatFunctions:
    @pytest.fixture
    def mock_config(self):
        return {
            "openai": {
                "completion_model": "gpt-4o",
                "temperature": 0.3
            }
        }
    
    def test_get_chatgpt_response(self, mock_config):
        from irs_bot.app import get_chatgpt_response
        
        # Setup mock
        mock_client = MagicMock()
        mock_choice = MagicMock()
        mock_choice.message.content = "This is a test response"
        mock_client.chat.completions.create.return_value.choices = [mock_choice]
        
        # Test data
        query = "What is science?"
        context = ["Science is a systematic approach to understanding the world", 
                   "It involves observation, experimentation, and theory development"]
        
        # Call function
        response = get_chatgpt_response(mock_config, mock_client, query, context)
        
        # Verify response
        assert response == "This is a test response"
        mock_client.chat.completions.create.assert_called_once()
        
        # Check that the correct prompt is used
        call_args = mock_client.chat.completions.create.call_args[1]
        assert call_args["model"] == mock_config["openai"]["completion_model"]
        assert len(call_args["messages"]) == 2
        assert call_args["messages"][0]["role"] == "system"
        assert call_args["messages"][1]["role"] == "user"
    
    @patch("irs_bot.app.query_chromadb")
    @patch("irs_bot.app.get_chatgpt_response")
    @patch("builtins.input")
    @patch("builtins.print")
    def test_chat_with_knowledge_base(self, mock_print, mock_input, mock_get_response, mock_query, mock_config):
        from irs_bot.app import chat_with_knowledge_base
        
        # Setup mocks
        mock_client = MagicMock()
        mock_collection = MagicMock()
        
        # Set up inputs to exit after one question
        mock_input.side_effect = ["What are Lagrange points?", "exit"]
        
        # Set up query results
        mock_query.return_value = [
            {"text": "Lagrange points are locations in space...", "metadata": {}, "id": "1", "distance": 0.1},
            {"text": "The James Webb telescope is at L2...", "metadata": {}, "id": "2", "distance": 0.2}
        ]
        
        # Set up response
        mock_get_response.return_value = "Lagrange points are special positions in space..."
        
        # Call function
        chat_with_knowledge_base(mock_config, mock_client, mock_collection)
        
        # Verify calls
        mock_query.assert_called_once_with(mock_collection, mock_config, "What are Lagrange points?")
        mock_get_response.assert_called_once()
        
        # Check that correct documents were passed
        response_args = mock_get_response.call_args[0]
        assert response_args[0] == mock_config
        assert response_args[1] == mock_client
        assert response_args[2] == "What are Lagrange points?"
        assert response_args[3] == ["Lagrange points are locations in space...", "The James Webb telescope is at L2..."]
    
    @patch("irs_bot.app.load_dotenv")
    @patch("irs_bot.app.load_config")
    @patch("irs_bot.app.os.getenv")
    @patch("irs_bot.app.OpenAI")
    @patch("irs_bot.app.create_chromadb_client")
    @patch("irs_bot.app.create_chromadb_collection")
    @patch("irs_bot.app.chunk_text")
    @patch("irs_bot.app.add_documents_to_chromadb")
    @patch("irs_bot.app.chat_with_knowledge_base")
    def test_main(self, mock_chat, mock_add_docs, mock_chunk, mock_create_collection, 
                 mock_create_client, mock_openai, mock_getenv, mock_load_config, mock_load_dotenv):
        from irs_bot.app import main
        
        # Setup mocks
        mock_config = {
            "chromadb": {"persist_directory": "test_dir", "collection_name": "test_coll"},
            "openai": {"embedding_model": "test-model"}
        }
        mock_load_config.return_value = mock_config
        mock_getenv.return_value = "test_api_key"
        
        mock_client = MagicMock()
        mock_client.close = MagicMock()
        mock_create_client.return_value = mock_client
        
        mock_collection = MagicMock()
        mock_create_collection.return_value = mock_collection
        
        mock_docs = [MagicMock(), MagicMock()]
        mock_chunk.return_value = mock_docs
        
        mock_openai_client = MagicMock()
        mock_openai.return_value = mock_openai_client
        
        # Call function
        main()
        
        # Verify calls
        mock_load_dotenv.assert_called_once()
        mock_load_config.assert_called_once_with("config/config.yaml")
        mock_getenv.assert_called_once_with("OPENAI_API_KEY")
        mock_openai.assert_called_once_with(api_key="test_api_key")
        mock_create_client.assert_called_once_with(mock_config)
        mock_create_collection.assert_called_once_with(mock_client, mock_config, "test_api_key")
        mock_chunk.assert_called_once_with(mock_config)
        mock_add_docs.assert_called_once_with(mock_collection, mock_docs)
        mock_chat.assert_called_once_with(mock_config, mock_openai_client, mock_collection)
        mock_client.close.assert_not_called()  # Fixed to match current implementation