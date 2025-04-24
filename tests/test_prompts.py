import pytest
import os
from unittest.mock import patch, MagicMock
import tempfile
import importlib

class TestSystemPrompts:
    @pytest.fixture
    def test_prompts(self):
        """Define different system prompts to test."""
        return {
            "directive": """
            You are a strict philosophy professor who only cites directly from the text.
            Always reference page numbers and never speculate beyond what is explicitly stated.
            Context: {context}
            Question: {query}
            """,
            
            "conversational": """
            You are a friendly philosophy guide who helps explain concepts in simple terms.
            Use examples from the text but focus on making the ideas accessible and relatable.
            Context: {context}
            Question: {query}
            """,
            
            "socratic": """
            You are a Socratic teacher who answers with thought-provoking questions.
            Reference relevant passages but encourage deeper reflection on the material.
            Context: {context}
            Question: {query}
            """
        }
    
    @pytest.fixture
    def test_questions(self):
        """Define test questions with expected characteristics in answers."""
        return [
            {
                "query": "What is the scientific method?",
                "expected_keywords": ["hypothesis", "experiment", "theory", "observation"],
                "forbidden_terms": ["Einstein", "quantum physics"]  # Topics not in our text
            },
            {
                "query": "How do scientists establish causation?",
                "expected_keywords": ["correlation", "controlled experiment", "variables"],
                "forbidden_terms": ["artificial intelligence", "machine learning"]
            }
        ]
    
    @pytest.fixture
    def test_context(self):
        """Create test context for evaluating prompts."""
        return [
            "The scientific method involves formulating hypotheses based on observations and testing them through experiments.",
            "Scientists establish causation through controlled experiments that manipulate variables while controlling for confounding factors.",
            "Correlation does not imply causation, as two variables may be associated without one directly causing the other."
        ]
    
    @pytest.mark.parametrize("prompt_name", ["directive", "conversational", "socratic"])
    def test_different_prompts(self, monkeypatch, test_prompts, test_questions, test_context, prompt_name):
        """Test how different prompts affect response structure."""
        from irs_bot.app import get_chatgpt_response
        import irs_bot.prompt
        
        # Store original prompt
        original_prompt = irs_bot.prompt.PROMPT
        
        try:
            # Replace prompt with test prompt
            monkeypatch.setattr(irs_bot.prompt, "PROMPT", test_prompts[prompt_name])
            
            # Create mock OpenAI client
            mock_client = MagicMock()
            mock_completion = MagicMock()
            mock_choice = MagicMock()
            mock_message = MagicMock()
            
            # Set up mock chain
            mock_message.content = f"Response using {prompt_name} prompt style"
            mock_choice.message = mock_message
            mock_completion.choices = [mock_choice]
            mock_client.chat.completions.create.return_value = mock_completion
            
            # Setup test config
            config = {
                "openai": {
                    "completion_model": "gpt-4o",
                    "temperature": 0.3
                }
            }
            
            # Test with first question
            query = test_questions[0]["query"]
            response = get_chatgpt_response(config, mock_client, query, test_context)
            
            # Verify the response contains the prompt style
            assert prompt_name in response
            
            # Verify chat completion was called with the right arguments
            mock_client.chat.completions.create.assert_called_once()
            call_args = mock_client.chat.completions.create.call_args[1]
            assert call_args["model"] == config["openai"]["completion_model"]
            assert call_args["temperature"] == 0.3
            
            # Verify the prompt format
            user_message = call_args["messages"][1]["content"]
            assert "Context:" in user_message
            assert "Question:" in user_message
            assert query in user_message
            
        finally:
            # Restore original prompt
            monkeypatch.setattr(irs_bot.prompt, "PROMPT", original_prompt)
    
    def test_prompt_format_validation(self, test_prompts):
        """Test that all prompts contain the required format fields."""
        for name, prompt in test_prompts.items():
            assert "{context}" in prompt, f"Prompt '{name}' missing {{context}} placeholder"
            assert "{query}" in prompt, f"Prompt '{name}' missing {{query}} placeholder"
    
    @patch("irs_bot.app.OpenAI")
    def test_prompt_integration(self, mock_openai, test_context, monkeypatch):
        """Test that prompts correctly format with actual context and query."""
        import irs_bot.prompt
        from irs_bot.app import get_chatgpt_response
        
        # Create mock OpenAI client
        mock_client = MagicMock()
        mock_completion = MagicMock()
        mock_choice = MagicMock()
        mock_message = MagicMock()
        
        # Set up mock response
        mock_message.content = "Integrated response"
        mock_choice.message = mock_message
        mock_completion.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Setup test config
        config = {
            "openai": {
                "completion_model": "gpt-4o",
                "temperature": 0.3
            }
        }
        
        # Test the actual prompt with specific context and query
        query = "What is empiricism?"
        response = get_chatgpt_response(config, mock_client, query, test_context)
        
        # Verify chat completion was called with formatted context
        call_args = mock_client.chat.completions.create.call_args[1]
        user_message = call_args["messages"][1]["content"]
        
        # Check that context was properly formatted
        assert "\n\n".join(test_context) in user_message