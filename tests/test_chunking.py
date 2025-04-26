"""
Tests for chunking evaluation module.
"""

import os
import pytest
from typing import Dict, Any, List

from dotenv import load_dotenv
from llama_index.core.schema import Document

from irs_bot.app import load_config
from irs_bot.chunking_eval import (
    ChunkingStrategy,
    MarkdownHeaderChunkingStrategy,
    CharacterChunkingStrategy,
    TokenChunkingStrategy,
    SentenceChunkingStrategy,
    create_index_from_documents,
    evaluate_chunking_strategy
)


@pytest.fixture
def config():
    """Fixture to load the configuration."""
    return load_config("config/config.yaml")


@pytest.fixture
def api_key():
    """Fixture to get the OpenAI API key."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        pytest.skip("OPENAI_API_KEY environment variable is not set")
    return api_key


def test_markdown_header_strategy(config):
    """Test the markdown header chunking strategy."""
    # Create the strategy
    strategy = MarkdownHeaderChunkingStrategy(config)
    
    # Ensure the correct path is used
    document_path = config["document_processing"]["path_to_doc"]
    
    # Get chunks
    chunks = strategy.chunk_text(document_path)
    
    # Basic assertions
    assert chunks is not None
    assert len(chunks) > 0
    assert all(isinstance(chunk, Document) for chunk in chunks)
    assert all(len(chunk.text) > 0 for chunk in chunks)


def test_character_chunking_strategy(config):
    """Test the character chunking strategy."""
    # Create the strategy
    strategy = CharacterChunkingStrategy(config, chunk_size=256, chunk_overlap=25)
    
    # Ensure the correct path is used
    document_path = config["document_processing"]["path_to_doc"]
    
    # Get chunks
    chunks = strategy.chunk_text(document_path)
    
    # Basic assertions
    assert chunks is not None
    assert len(chunks) > 0
    assert all(isinstance(chunk, Document) for chunk in chunks)
    assert all(len(chunk.text) > 0 for chunk in chunks)
    
    # Most chunks should be close to the chunk size
    # (allowing some flexibility for splitting at natural boundaries)
    assert all(len(chunk.text) <= 350 for chunk in chunks)


def test_token_chunking_strategy(config):
    """Test the token chunking strategy."""
    # Create the strategy
    strategy = TokenChunkingStrategy(config, chunk_size=128, chunk_overlap=15)
    
    # Ensure the correct path is used
    document_path = config["document_processing"]["path_to_doc"]
    
    # Get chunks
    chunks = strategy.chunk_text(document_path)
    
    # Basic assertions
    assert chunks is not None
    assert len(chunks) > 0
    assert all(isinstance(chunk, Document) for chunk in chunks)
    assert all(len(chunk.text) > 0 for chunk in chunks)


def test_sentence_chunking_strategy(config):
    """Test the sentence chunking strategy."""
    # Create the strategy
    strategy = SentenceChunkingStrategy(config, chunk_size=3, chunk_overlap=1)
    
    # Ensure the correct path is used
    document_path = config["document_processing"]["path_to_doc"]
    
    # Get chunks
    chunks = strategy.chunk_text(document_path)
    
    # Basic assertions
    assert chunks is not None
    assert len(chunks) > 0
    assert all(isinstance(chunk, Document) for chunk in chunks)
    assert all(len(chunk.text) > 0 for chunk in chunks)


@pytest.mark.slow
def test_create_index(config, api_key):
    """Test creating an index from documents."""
    # Create a strategy
    strategy = CharacterChunkingStrategy(config, chunk_size=256, chunk_overlap=25)
    
    # Get a small sample of the document
    document_path = config["document_processing"]["path_to_doc"]
    chunks = strategy.chunk_text(document_path)[:5]  # Only use first 5 chunks for speed
    
    # Create index
    index = create_index_from_documents(
        chunks, 
        api_key, 
        config["openai"]["embedding_model"]
    )
    
    # Basic assertions
    assert index is not None
    assert index.docstore is not None
    assert len(index.docstore.docs) > 0


@pytest.mark.slow
def test_evaluate_strategy(config, api_key):
    """Test evaluating a chunking strategy."""
    # Create a strategy
    strategy = CharacterChunkingStrategy(config, chunk_size=256, chunk_overlap=25)
    
    # Get document path
    document_path = config["document_processing"]["path_to_doc"]
    
    # Only test with a small number of evaluation questions to save API calls
    metrics = evaluate_chunking_strategy(
        strategy, 
        document_path, 
        api_key, 
        config,
        num_eval_questions=2
    )
    
    # Basic assertions for the metrics
    assert metrics is not None
    assert "strategy" in metrics
    assert "document_count" in metrics
    assert "avg_document_length" in metrics
    assert "mrr" in metrics
    assert "hit_rate" in metrics
    assert "relevancy" in metrics
    
    # The strategy name should be set correctly
    assert metrics["strategy"] == strategy.name
    
    # Metrics should be in a reasonable range
    assert 0 <= metrics["mrr"] <= 1.0
    assert 0 <= metrics["hit_rate"] <= 1.0
    assert 0 <= metrics["relevancy"] <= 5.0  # Relevancy is typically on a 0-5 scale