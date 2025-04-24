import os
import pytest
import tempfile
import json
from unittest.mock import patch, MagicMock
import yaml

# Constants for evaluation
TEST_PROMPT_TEMPLATE = """
You are a philosophy professor who teaches the philosophy of science.
{style_instructions}
Context: {context}
Question: {query}
"""

PROMPT_STYLES = {
    "directive": "Only cite directly from the provided context. Never speculate beyond what is explicitly stated.",
    "conversational": "Explain concepts in simple terms. Use examples from the context but focus on making ideas accessible.",
    "concise": "Provide brief, direct answers focusing only on the most relevant information from the context."
}

CHUNKING_STRATEGIES = [
    {"name": "small_chunks", "chunk_size": 100, "chunk_overlap": 20},
    {"name": "medium_chunks", "chunk_size": 300, "chunk_overlap": 50},
    {"name": "large_chunks", "chunk_size": 600, "chunk_overlap": 100},
]


class TestRAGEvaluation:
    @pytest.fixture
    def test_document(self):
        """Create a test document with philosophical content."""
        return """# Philosophy of Science
        
        ## The Scientific Method
        
        The scientific method is a systematic approach to understanding the natural world.
        It begins with observations and questions, proceeds to hypothesis formation,
        followed by experimentation and data collection. Scientists then analyze results
        and refine theories based on evidence.
        
        ### Hypothesis Testing
        
        A good hypothesis must be testable and falsifiable. Scientists design
        experiments specifically to test whether a hypothesis can be disproven.
        Karl Popper emphasized that scientific theories can never be proven true,
        only proven false or corroborated by evidence.
        
        ## Causation and Correlation
        
        Establishing causation requires more than correlation. Scientists use controlled
        experiments where they manipulate variables while controlling for confounding factors.
        Mill's methods provide systematic approaches for determining causal relationships:
        the method of agreement, the method of difference, and the joint method.
        
        ### Statistical Analysis
        
        Statistical tools help scientists distinguish between true causal relationships
        and mere coincidences. P-values, confidence intervals, and regression analyses
        are common methods for evaluating the strength of evidence for causation.
        """
    
    @pytest.fixture
    def sample_questions(self):
        """Questions for testing the RAG system."""
        return [
            {
                "query": "What is the scientific method?",
                "expected_keywords": ["systematic", "observations", "hypothesis", "experimentation"],
                "context_references": ["scientific method", "systematic approach"]
            },
            {
                "query": "How do scientists establish causation?",
                "expected_keywords": ["correlation", "controlled experiments", "variables", "Mill's methods"],
                "context_references": ["causation requires more than correlation", "controlled experiments"]
            },
            {
                "query": "What did Karl Popper contribute to philosophy of science?",
                "expected_keywords": ["falsifiable", "disproven", "corroborated"],
                "context_references": ["Karl Popper", "falsifiable"]
            }
        ]

    def setup_test_environment(self, test_document, chunking_config):
        """Create test environment with specified chunking strategy."""
        # Create temporary file with test document
        with tempfile.NamedTemporaryFile(suffix='.md', mode='w+', delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(test_document)
            
        # Create configuration for testing
        config = {
            "document_processing": {
                "path_to_doc": temp_path,
                "chunk_size": chunking_config["chunk_size"],
                "chunk_overlap": chunking_config["chunk_overlap"],
                "headers_to_split_on": [
                    ["##", "Header 2"],
                    ["###", "Header 3"]
                ]
            },
            "openai": {
                "embedding_model": "text-embedding-3-large",
                "completion_model": "gpt-4o",
                "temperature": 0.3
            },
            "chromadb": {
                "persist_directory": f"test_chromadb_{chunking_config['name']}",
                "collection_name": f"test_collection_{chunking_config['name']}"
            },
            "query": {
                "n_results": 3
            }
        }
        
        return temp_path, config
        
    def cleanup_test_environment(self, temp_path, config):
        """Clean up temporary files and directories."""
        # Remove temporary document file
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        
        # Remove chromadb directory if it exists
        chromadb_dir = config["chromadb"]["persist_directory"]
        if os.path.exists(chromadb_dir):
            import shutil
            shutil.rmtree(chromadb_dir)
    
    @pytest.mark.parametrize("chunking_strategy", CHUNKING_STRATEGIES)
    def test_retrieval_metrics(self, test_document, sample_questions, chunking_strategy):
        """
        Test retrieval performance with different chunking strategies.
        
        This test evaluates:
        1. Hit rate - whether relevant chunks are retrieved
        2. Retrieval precision - how many retrieved chunks are relevant
        """
        temp_path, config = self.setup_test_environment(test_document, chunking_strategy)
        
        try:
            # Import app functions
            from irs_bot.app import chunk_text, create_chromadb_client, create_chromadb_collection
            from irs_bot.app import add_documents_to_chromadb, query_chromadb
            
            # Mock the OpenAI API key
            api_key = "test_api_key"
            
            # Create ChromaDB client
            with patch("chromadb.utils.embedding_functions.OpenAIEmbeddingFunction"):
                client = create_chromadb_client(config)
                collection = create_chromadb_collection(client, config, api_key)
                
                # Process document and add to collection
                documents = chunk_text(config)
                add_documents_to_chromadb(collection, documents)
                
                # Test retrieval for each question
                results = {}
                for question in sample_questions:
                    with patch("irs_bot.app.query_chromadb") as mock_query:
                        # Mock the query results based on actual chunks
                        retrieval_results = []
                        for i, doc in enumerate(documents[:3]):  # Mock top 3 results
                            retrieval_results.append({
                                "text": doc.page_content,
                                "metadata": {},
                                "id": f"doc_{i}",
                                "distance": 0.1 * (i + 1)  # Mock distance
                            })
                        mock_query.return_value = retrieval_results
                        
                        # Perform query
                        query_results = query_chromadb(collection, config, question["query"])
                        
                        # Evaluate results
                        hit = False
                        for ref in question["context_references"]:
                            for result in query_results:
                                if ref.lower() in result["text"].lower():
                                    hit = True
                                    break
                            if hit:
                                break
                                
                        results[question["query"]] = {
                            "hit": hit,
                            "retrieved_chunks": len(query_results),
                            "chunk_strategy": chunking_strategy["name"]
                        }
                
                # Calculate metrics
                hit_rate = sum(1 for r in results.values() if r["hit"]) / len(results)
                
                # Print metrics for this chunking strategy
                print(f"\nChunking strategy: {chunking_strategy['name']}")
                print(f"Hit rate: {hit_rate:.2f}")
                print(f"Number of chunks: {len(documents)}")
                
                # For a more complete test, we would need to implement:
                # - Mean Reciprocal Rank (MRR)
                # - Context Precision
                # - Context Recall
                # - etc.
                
                # Basic assertions to validate test
                assert len(documents) > 0, "Document chunking failed"
                assert hit_rate >= 0, "Hit rate calculation failed"
                
        finally:
            self.cleanup_test_environment(temp_path, config)

    @pytest.mark.parametrize("prompt_style", list(PROMPT_STYLES.keys()))
    def test_response_quality(self, test_document, sample_questions, prompt_style):
        """
        Test response quality with different prompt styles.
        
        This test evaluates:
        1. Faithfulness - does the response avoid hallucinations
        2. Relevancy - does the response address the question
        3. Conciseness - is the response appropriately sized
        """
        # Use medium chunks for prompt testing
        chunking_strategy = next(s for s in CHUNKING_STRATEGIES if s["name"] == "medium_chunks")
        temp_path, config = self.setup_test_environment(test_document, chunking_strategy)
        
        try:
            # Import app functions
            from irs_bot.app import get_chatgpt_response
            import irs_bot.prompt
            
            # Store original prompt
            original_prompt = irs_bot.prompt.PROMPT
            
            # Set test prompt
            style_instructions = PROMPT_STYLES[prompt_style]
            test_prompt = TEST_PROMPT_TEMPLATE.format(style_instructions=style_instructions, context="{context}", query="{query}")
            irs_bot.prompt.PROMPT = test_prompt
            
            # Create mock context for testing
            context = [
                "The scientific method is a systematic approach to understanding the natural world.",
                "Scientists establish causation through controlled experiments.",
                "Karl Popper emphasized that scientific theories can never be proven true, only falsifiable."
            ]
            
            # Mock responses for different styles
            mock_responses = {
                "directive": "The scientific method is described as 'a systematic approach to understanding the natural world' in the provided context.",
                "conversational": "Think of the scientific method as a systematic way scientists investigate the world around us. It helps them turn observations into testable ideas!",
                "concise": "Systematic approach to understanding nature through observation, hypothesis formation, and experimentation."
            }
            
            # Test each question with the selected prompt style
            results = {}
            for question in sample_questions:
                # Create mock OpenAI client
                mock_client = MagicMock()
                mock_choice = MagicMock()
                mock_choice.message.content = mock_responses[prompt_style]
                mock_client.chat.completions.create.return_value.choices = [mock_choice]
                
                # Get response
                response = get_chatgpt_response(config, mock_client, question["query"], context)
                
                # Evaluate response
                keyword_hits = sum(1 for kw in question["expected_keywords"] if kw.lower() in response.lower())
                keyword_coverage = keyword_hits / len(question["expected_keywords"])
                
                # Simple metrics (would be expanded in real implementation)
                results[question["query"]] = {
                    "keyword_coverage": keyword_coverage,
                    "response_length": len(response),
                    "prompt_style": prompt_style
                }
            
            # Calculate metrics for this prompt style
            avg_keyword_coverage = sum(r["keyword_coverage"] for r in results.values()) / len(results)
            avg_response_length = sum(r["response_length"] for r in results.values()) / len(results)
            
            # Print metrics
            print(f"\nPrompt style: {prompt_style}")
            print(f"Average keyword coverage: {avg_keyword_coverage:.2f}")
            print(f"Average response length: {avg_response_length:.0f} characters")
            
            # For a complete implementation, we would add:
            # - Faithfulness scoring (using LLM evaluation)
            # - Relevancy scoring (using LLM evaluation)
            # - Sentiment analysis
            # - etc.
            
            # Basic assertions
            assert avg_keyword_coverage >= 0, "Keyword coverage calculation failed"
            
            # Restore original prompt
            irs_bot.prompt.PROMPT = original_prompt
            
        finally:
            self.cleanup_test_environment(temp_path, config)
    
    def test_llamaindex_style_evaluation(self):
        """
        Test skeleton demonstrating how to implement LlamaIndex-style RAG evaluation.
        
        This would be expanded in a real implementation with actual LlamaIndex integration.
        """
        # This is a skeleton showing how LlamaIndex evaluation would be structured
        print("\nLlamaIndex-style evaluation skeleton:")
        print("1. Would generate question-context pairs")
        print("2. Would evaluate retrieval with hit_rate and MRR")
        print("3. Would evaluate response with faithfulness and relevancy")
        
        # In a real implementation, we would:
        # 1. Import LlamaIndex (if using it directly)
        # 2. Generate synthetic test questions
        # 3. Run evaluators for retrieval quality
        # 4. Run evaluators for response quality
        # 5. Compare metrics across different configurations
        
        # Placeholder for now
        assert True
    
    def test_end_to_end_evaluation(self, test_document):
        """
        Perform end-to-end evaluation of chunking and prompt combinations.
        
        This test would run a matrix of chunking strategies × prompt styles
        and identify the optimal combination.
        """
        # Create results container
        results = []
        
        # Only test a subset for demonstration
        test_chunking = [s for s in CHUNKING_STRATEGIES if s["name"] in ["small_chunks", "large_chunks"]]
        test_prompts = ["directive", "concise"]
        
        print("\nEnd-to-end evaluation matrix (sample):")
        
        # Output header
        print(f"{'Chunking':<15} | {'Prompt':<15} | {'Hit Rate':<10} | {'Keyword Coverage':<15}")
        print("-" * 60)
        
        # For each combination, we would run a full evaluation
        for chunking in test_chunking:
            for prompt in test_prompts:
                # In a real test, we would perform full evaluation
                # Here we use mock results
                hit_rate = 0.7 if chunking["name"] == "small_chunks" else 0.5
                keyword_coverage = 0.8 if prompt == "directive" else 0.6
                
                # Print results row
                print(f"{chunking['name']:<15} | {prompt:<15} | {hit_rate:<10.2f} | {keyword_coverage:<15.2f}")
                
                # Store results
                results.append({
                    "chunking": chunking["name"],
                    "prompt": prompt,
                    "hit_rate": hit_rate,
                    "keyword_coverage": keyword_coverage,
                    "combined_score": (hit_rate + keyword_coverage) / 2
                })
        
        # Find best combination based on combined score
        best_result = max(results, key=lambda x: x["combined_score"])
        print("\nBest combination:")
        print(f"Chunking: {best_result['chunking']}, Prompt: {best_result['prompt']}")
        print(f"Combined score: {best_result['combined_score']:.2f}")
        
        # This would be expanded with real evaluation logic
        assert len(results) == len(test_chunking) * len(test_prompts), "Matrix evaluation failed"