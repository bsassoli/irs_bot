# Philosophy of Science Knowledge Assistant

A Retrieval-Augmented Generation (RAG) chatbot designed to answer questions about the "Recipes for Science" textbook.

## Overview

This project implements a RAG-based conversational AI system using:

* OpenAI's embedding and completion models
* ChromaDB for vector storage and similarity search
* Custom document chunking and retrieval logic
* Flask-based API server
* React frontend with ShadCN/UI components

## Features

* **Semantic Search**: Uses embeddings to find relevant textbook passages
* **Context-Aware Responses**: Leverages GPT-4o to generate accurate answers based on retrieved context
* **Evaluation Framework**: Tests for chunking strategies and system prompts
* **Modern UI**: Clean, responsive interface with React and ShadCN/UI

## Installation

**Clone** the repository:

```bash
git clone [repository-url]
cd irs_bot
```

Create a **virtual environment**:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install **dependencies**:

```bash
pip install -r requirements.txt
```

Set up **environment variables**:

```bash
# Create a .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## Running the Application

### Backend Server

Start the Flask server:

```bash
python run_server.py
```

This will:
- Load the configuration
- Initialize ChromaDB
- Process and embed the textbook (if not already done)
- Start the Flask API server at http://localhost:5001

### React Frontend

Navigate to the React UI directory:

```bash
cd react-ui
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm start
```

This will start the React frontend at http://localhost:3000, which will proxy API requests to the Flask server running on port 5001.

## Testing and Evaluation

### Running Tests

Run all tests:

```bash
pytest tests/
```

Run specific test files:

```bash
pytest tests/test_app.py
pytest tests/test_chunking.py
pytest tests/test_evaluation.py
```

### Evaluating Chunking Strategies

The test suite includes tests to evaluate different chunking strategies:

```bash
pytest tests/test_chunking.py::TestChunkingStrategies::test_chunk_size_variations
```

### Evaluating System Prompts

Test different system prompts:

```bash
pytest tests/test_prompts.py::TestSystemPrompts::test_different_prompts
```

### End-to-End Evaluation

Run the full evaluation matrix:

```bash
pytest tests/test_evaluation.py::TestRAGEvaluation::test_end_to_end_evaluation
```

## Configuration

The chatbot's behavior can be customized through the `config/config.yaml` file:

- **OpenAI settings**: Embedding and completion models, temperature
- **ChromaDB settings**: Persistence directory, collection name
- **Document processing**: Chunk size, chunk overlap, headers to split on
- **Query settings**: Number of results to retrieve

## Project Structure

- **src/irs_bot/**: Core application code
  - **app.py**: Main RAG logic
  - **server.py**: Flask server implementation
  - **prompt.py**: System prompt templates
- **tests/**: Test files
  - **test_app.py**: Core functionality tests
  - **test_chunking.py**: Chunking strategy tests
  - **test_prompts.py**: System prompt tests
  - **test_evaluation.py**: End-to-end evaluation
- **web/**: Flask web interface
- **react-ui/**: React frontend with ShadCN/UI
- **data/**: Contains markdown files with the textbook content
- **config/**: Configuration files

## Future Improvements

* Conversation history and context management
* Response citation and source tracking
* Multi-document support for expanded knowledge base
* Streaming responses for better UX