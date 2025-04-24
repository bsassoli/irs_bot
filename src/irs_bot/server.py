import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import yaml
import logging

# Import app components
from irs_bot.app import (
    load_config, 
    create_chromadb_client, 
    create_chromadb_collection,
    chunk_text, 
    add_documents_to_chromadb,
    query_chromadb,
    get_chatgpt_response
)

from openai import OpenAI

# Initialize Flask app
app = Flask(__name__, 
            static_folder="../../web/static",
            template_folder="../../web/templates")

# Global variables for app state
config = None
openai_client = None
chroma_client = None
collection = None
is_initialized = False

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/api/initialize', methods=['POST'])
def initialize():
    """Initialize the app if not already initialized."""
    global config, openai_client, chroma_client, collection, is_initialized
    
    if is_initialized:
        logging.info("App already initialized, returning success")
        response = jsonify({"status": "already_initialized"})
        response.headers.add('Content-Type', 'application/json')
        return response
    
    try:
        # Load environment variables
        logging.info("Loading environment variables")
        load_dotenv()
        
        # Load configuration
        logging.info("Loading configuration from config/config.yaml")
        config = load_config("config/config.yaml")
        
        # Get OpenAI API key
        logging.info("Getting OpenAI API key")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            logging.error("OpenAI API key not found in environment variables")
            response = jsonify({"status": "error", "message": "OpenAI API key not found in environment variables"})
            response.headers.add('Content-Type', 'application/json')
            return response
        
        # Initialize OpenAI client
        logging.info("Initializing OpenAI client")
        openai_client = OpenAI(api_key=openai_api_key)
        
        # Create ChromaDB client
        logging.info("Creating ChromaDB client")
        chroma_client = create_chromadb_client(config)
        
        # Create ChromaDB collection
        logging.info("Creating ChromaDB collection")
        collection = create_chromadb_collection(chroma_client, config, openai_api_key)
        
        # Chunk text and add to ChromaDB if collection is empty
        count = collection.count()
        logging.info(f"Collection count: {count}")
        if count == 0:
            logging.info("Processing document and adding to ChromaDB")
            documents = chunk_text(config)
            add_documents_to_chromadb(collection, documents)
        
        is_initialized = True
        logging.info("Initialization complete")
        response = jsonify({"status": "success", "message": "Initialization complete"})
        response.headers.add('Content-Type', 'application/json')
        return response
    
    except Exception as e:
        logging.error(f"Initialization error: {str(e)}")
        response = jsonify({"status": "error", "message": str(e)})
        response.headers.add('Content-Type', 'application/json')
        return response

@app.route('/api/query', methods=['POST'])
def query():
    """Process a query and return the response."""
    global config, openai_client, collection, is_initialized
    
    if not is_initialized:
        logging.error("App not initialized for query")
        response = jsonify({"status": "error", "message": "App not initialized. Call /api/initialize first."})
        response.headers.add('Content-Type', 'application/json')
        return response
    
    try:
        # Get query from request
        data = request.json
        if data is None:
            logging.error("Invalid JSON payload in request")
            response = jsonify({"status": "error", "message": "Invalid JSON payload"})
            response.headers.add('Content-Type', 'application/json')
            return response
            
        user_query = data.get('query')
        
        if not user_query:
            logging.error("No query provided in request")
            response = jsonify({"status": "error", "message": "No query provided"})
            response.headers.add('Content-Type', 'application/json')
            return response
        
        # Query ChromaDB
        logging.info(f"Querying ChromaDB for: {user_query}")
        results = query_chromadb(collection, config, user_query)
        
        # Extract document texts
        document_texts = [doc["text"] for doc in results]
        logging.info(f"Found {len(document_texts)} relevant documents")
        
        # Get response from OpenAI
        logging.info("Generating response with OpenAI")
        response_text = get_chatgpt_response(config, openai_client, user_query, document_texts)
        
        logging.info("Query processed successfully")
        response = jsonify({
            "status": "success",
            "query": user_query,
            "response": response_text,
            "context": document_texts
        })
        response.headers.add('Content-Type', 'application/json')
        return response
    
    except Exception as e:
        logging.error(f"Query error: {str(e)}")
        response = jsonify({"status": "error", "message": str(e)})
        response.headers.add('Content-Type', 'application/json')
        return response

@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if the app is initialized and healthy."""
    global is_initialized
    
    logging.info(f"Health check: initialized={is_initialized}")
    response = jsonify({
        "status": "healthy" if is_initialized else "not_initialized",
        "initialized": is_initialized
    })
    response.headers.add('Content-Type', 'application/json')
    return response

def start_server(host='0.0.0.0', port=5000, debug=False):
    """Start the Flask server."""
    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('irs_bot_server.log')
        ]
    )
    
    # Start server
    start_server(debug=True)