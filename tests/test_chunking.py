import os
import pytest
import tempfile
from unittest.mock import patch, MagicMock
from langchain_core.documents import Document


class TestChunkingStrategies:
    @pytest.fixture
    def test_document(self):
        """Create a test document with predictable structure."""
        return """# Test Document
        
        ## Section 1
        Content for section 1. This is some text that will be used to test
        different chunking strategies. We need enough text to properly test
        chunking behavior with various parameters.
        
        ### Subsection 1.1
        More content for testing. This subsection contains additional information
        that can be used to evaluate how chunking handles nested headers and content
        divisions. The text should be long enough to span multiple chunks with
        smaller chunk sizes.
        
        ## Section 2
        Content for section 2. Another section to test how the chunking strategy
        handles multiple top-level sections. This section should have enough content
        to test chunk boundaries.
        
        ### Subsection 2.1
        Even more content for testing chunking strategies. This final subsection
        contains the last part of our test document. It should provide enough text
        to properly evaluate different chunking parameters.
        """
    
    @pytest.mark.parametrize("chunk_size,chunk_overlap,expected_chunks", [
        (100, 20, 6),  # Small chunks
        (300, 50, 3),  # Medium chunks
        (1000, 100, 1),  # Large single chunk
    ])
    def test_chunk_size_variations(self, test_document, chunk_size, chunk_overlap, expected_chunks):
        """Test how different chunk sizes affect document splitting."""
        # Setup config with different chunking parameters
        config = {
            "document_processing": {
                "chunk_size": chunk_size,
                "chunk_overlap": chunk_overlap,
                "headers_to_split_on": [
                    ["##", "Header 2"],
                    ["###", "Header 3"]
                ]
            }
        }
        
        # Create temporary file with test document
        with tempfile.NamedTemporaryFile(suffix='.md', mode='w+', delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(test_document)
            
        config["document_processing"]["path_to_doc"] = temp_path
        
        try:
            # Run chunking
            from irs_bot.app import chunk_text
            chunks = chunk_text(config)
            
            # Verify number of chunks is within acceptable range
            # (exact number might vary slightly due to splitting behavior)
            assert abs(len(chunks) - expected_chunks) <= 1, \
                f"Expected around {expected_chunks} chunks, got {len(chunks)}"
            
            # Verify content preservation
            full_content = "".join([chunk.page_content for chunk in chunks])
            assert "Section 1" in full_content
            assert "Section 2" in full_content
            assert "Subsection 1.1" in full_content
            assert "Subsection 2.1" in full_content
            
            # Verify chunk sizes are reasonable
            for chunk in chunks:
                # Each chunk should be less than or equal to chunk_size
                # with some flexibility for markdown headers
                assert len(chunk.page_content) <= chunk_size * 1.2, \
                    f"Chunk size {len(chunk.page_content)} exceeds expected maximum {chunk_size * 1.2}"
            
        finally:
            # Clean up
            os.unlink(temp_path)
    
    def test_header_splitting_variations(self, test_document):
        """Test how different header splitting affects document chunking."""
        # Test with different header configurations
        header_configs = [
            [["##", "Header 2"]],  # Only split on H2
            [["###", "Header 3"]],  # Only split on H3
            [["##", "Header 2"], ["###", "Header 3"]]  # Split on both
        ]
        
        results = []
        
        # Create temporary file with test document
        with tempfile.NamedTemporaryFile(suffix='.md', mode='w+', delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(test_document)
        
        try:
            from irs_bot.app import chunk_text
            
            # Test each header configuration
            for headers in header_configs:
                config = {
                    "document_processing": {
                        "path_to_doc": temp_path,
                        "chunk_size": 1000,  # Large to focus on header splitting
                        "chunk_overlap": 0,
                        "headers_to_split_on": headers
                    }
                }
                
                chunks = chunk_text(config)
                results.append(len(chunks))
                
                # Verify chunks have appropriate metadata
                for chunk in chunks:
                    assert "metadata" in dir(chunk)
                    if headers == [["##", "Header 2"]]:
                        # Should split on Section 1 and Section 2
                        if "Section" in chunk.page_content:
                            assert chunk.metadata.get("header_levels") == ["Header 2"]
            
            # Verify different header configs produce different chunk counts
            assert len(set(results)) > 1, "Different header configs should produce different chunking results"
            
        finally:
            # Clean up
            os.unlink(temp_path)
            
    def test_chunk_content_relevance(self, test_document):
        """Test that chunks maintain relevant context."""
        # Create temporary file with test document
        with tempfile.NamedTemporaryFile(suffix='.md', mode='w+', delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(test_document)
            
        try:
            from irs_bot.app import chunk_text
            
            # Test with medium chunks and both header levels
            config = {
                "document_processing": {
                    "path_to_doc": temp_path,
                    "chunk_size": 200,
                    "chunk_overlap": 50,
                    "headers_to_split_on": [
                        ["##", "Header 2"],
                        ["###", "Header 3"]
                    ]
                }
            }
            
            chunks = chunk_text(config)
            
            # Check that headers are preserved with their content
            section1_chunk = None
            subsection1_chunk = None
            
            for chunk in chunks:
                if "## Section 1" in chunk.page_content:
                    section1_chunk = chunk
                if "### Subsection 1.1" in chunk.page_content:
                    subsection1_chunk = chunk
            
            assert section1_chunk is not None, "Should have a chunk with Section 1 header"
            assert subsection1_chunk is not None, "Should have a chunk with Subsection 1.1 header"
            
            # Check that section content is with its header
            assert "Content for section 1" in section1_chunk.page_content
            assert "More content for testing" in subsection1_chunk.page_content
            
        finally:
            # Clean up
            os.unlink(temp_path)
            
    @patch("irs_bot.app.UnstructuredMarkdownLoader")
    @patch("irs_bot.app.MarkdownHeaderTextSplitter")
    @patch("irs_bot.app.RecursiveCharacterTextSplitter")
    def test_empty_document_handling(self, mock_text_splitter, mock_md_splitter, mock_loader):
        """Test how chunking handles empty documents."""
        from irs_bot.app import chunk_text
        
        # Create empty document
        mock_doc = Document(page_content="")
        mock_loader.return_value.load.return_value = [mock_doc]
        
        # Empty result from markdown splitter
        mock_md_splitter.return_value.split_text.return_value = []
        
        # Empty chunks from text splitter
        mock_text_splitter.return_value.split_documents.return_value = []
        
        # Setup config
        config = {
            "document_processing": {
                "path_to_doc": "dummy_path",
                "chunk_size": 100,
                "chunk_overlap": 20,
                "headers_to_split_on": [
                    ["##", "Header 2"],
                    ["###", "Header 3"]
                ]
            }
        }
        
        # Call the function
        chunks = chunk_text(config)
        
        # Assert empty chunks
        assert chunks == []