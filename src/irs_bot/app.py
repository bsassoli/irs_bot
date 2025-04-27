import os
import yaml
import logging

from dotenv import load_dotenv
from typing import List, Dict, Any

from chromadb import PersistentClient, Settings, Collection
from openai import OpenAI
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

from irs_bot.prompt import SYSTEM_PROMPT, PROMPT

import chromadb.utils.embedding_functions as ef

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Loads the configuration file.
    """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def chunk_text(config: Dict[str, Any]) -> List[str]:
    """
    Splits the text into chunks based on the configuration.
    """
    chunks = []
    
    loader = UnstructuredMarkdownLoader(config["document_processing"]["path_to_doc"])
    logging.info(f"Loading document from: {config['document_processing']['path_to_doc']}")

    # split the Markdown document into sections based on headers
    headers_to_split_on = config["document_processing"]["headers_to_split_on"]
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on, strip_headers=False
    )
    
    chunk_size = config["document_processing"]["chunk_size"]
    chunk_overlap = config["document_processing"]["chunk_overlap"]
    
    documents = loader.load()
    logging.info(f"Loaded {len(documents)} documents from markdown file")
    
    for doc in documents:
        text = doc.page_content
        logging.info(f"Processing document with length: {len(text)}")
        split_texts = markdown_splitter.split_text(text)
        logging.info(f"Split into {len(split_texts)} sections based on headers")
        
        # Further split the text into smaller chunks
        recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len
        )
        split_texts = recursive_splitter.split_documents(split_texts)
        logging.info(f"Further split into {len(split_texts)} chunks")
        
        # Add the split texts to the chunks list
        chunks.extend(split_texts)

    logging.info(f"Total chunks created: {len(chunks)}")
    if chunks:
        logging.info(f"First chunk preview: {chunks[0].page_content[:100]}...")
    
    return chunks

def create_chromadb_client(config: Dict[str, Any]):
    """
    Creates a ChromaDB client with the specified configuration.
    
    Args:
        config: Configuration dictionary containing ChromaDB settings.
        
    Returns:
        ChromaDB client instance.
    """
    
    # Ensure the persist directory exists
    persist_directory = config["chromadb"]["persist_directory"]
    
    # Create and return the client
    client = PersistentClient(
        path=persist_directory,
        settings=Settings(
            anonymized_telemetry=False
        )
    )
    
    return client

def create_chromadb_collection(client, config: Dict[str, Any], api_key: str):
    """
    Creates a ChromaDB collection with the specified configuration.
    
    Args:
        client: ChromaDB client instance.
        config: Configuration dictionary containing collection settings.
        api_key: OpenAI API key.
        
    Returns:
        ChromaDB collection instance.
    """
    # Test OpenAI API key first
    try:
        logging.info("Testing OpenAI API key...")
        test_client = OpenAI(api_key=api_key)
        test_response = test_client.embeddings.create(
            model=config["openai"]["embedding_model"],
            input="Test input"
        )
        logging.info("OpenAI API key test successful")
    except Exception as e:
        logging.error(f"OpenAI API key test failed: {str(e)}")
        raise ValueError(f"OpenAI API key validation failed: {str(e)}")
    
    # Create embedding function
    embedding_function = ef.OpenAIEmbeddingFunction(
        api_key=api_key,
        model_name=config["openai"]["embedding_model"]
    )
    
    # Create or get the collection
    collection = client.get_or_create_collection(
        name=config["chromadb"]["collection_name"],
        embedding_function=embedding_function
    )
    
    return collection

def add_documents_to_chromadb(collection, documents: List):
    """
    Adds documents to the ChromaDB collection. 
    Args:
        collection: ChromaDB collection instance.
        documents: List of document objects from chunk_text.
    """
    # Extract text content from documents and ensure it's properly formatted
    texts = []
    for doc in documents:
        text = doc.page_content
        # Ensure text is a string and not empty
        if not isinstance(text, str):
            text = str(text)
        # Remove any problematic characters and ensure proper encoding
        text = text.strip().encode('ascii', 'ignore').decode('ascii')
        texts.append(text)
    
    # Generate IDs for each document
    ids = [f"doc_{i}" for i in range(len(texts))]
    # Create metadata for each document
    metadatas = [{"source": getattr(doc, "metadata", {}).get("source", "unknown")} for doc in documents]
    
    # Log the first document's content for debugging
    if texts:
        logging.info(f"First document content preview: {texts[0][:100]}...")
        logging.info(f"First document length: {len(texts[0])}")
    
    # Add documents to the collection in smaller batches
    batch_size = 100
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        batch_ids = ids[i:i + batch_size]
        batch_metadatas = metadatas[i:i + batch_size]
        
        try:
            collection.add(
                documents=batch_texts,
                ids=batch_ids,
                metadatas=batch_metadatas
            )
            logging.info(f"Successfully added batch {i//batch_size + 1} of {(len(texts) + batch_size - 1)//batch_size}")
        except Exception as e:
            logging.error(f"Error adding batch {i//batch_size + 1} to ChromaDB: {str(e)}")
            logging.error(f"Batch size: {len(batch_texts)}")
            logging.error(f"First document in batch type: {type(batch_texts[0]) if batch_texts else 'None'}")
            raise

def query_chromadb(collection, config: Dict[str, Any], query: str) -> List[Dict[str, Any]]:
    """
    Queries the ChromaDB collection with the specified query.
    
    Args:
        collection: ChromaDB collection instance.
        config: Configuration dictionary containing query settings.
        query: Query string.
        
    Returns:
        List of documents matching the query.
    """
    
    # Query the collection and return results
    results = collection.query(
        query_texts=[query],  # Use query_texts instead of query_embeddings
        n_results=config["query"]["n_results"],
        include=["documents", "metadatas", "distances"]
    )
    
    # Format results into a more usable structure
    formatted_results = []
    for i in range(len(results["documents"][0])):
        formatted_results.append({
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
            "id": results["ids"][0][i],
            "distance": results["distances"][0][i] if "distances" in results else None
        })
    
    return formatted_results

def get_chatgpt_response(
    config: Dict[str, Any], 
    client: OpenAI,
    query: str, 
    context: List[str]
    ) -> str:
    """
    Gets a response from GPT-4o based on the query and context.
    """
    # Combine context documents into a single string
    context_text = "\n\n".join(context)

    # Create a prompt for GPT-4o
    prompt = PROMPT.format(context=context_text, query=query)

    # Call the OpenAI API
    response = client.chat.completions.create(
        model=config["openai"]["completion_model"],
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


def chat_with_knowledge_base(
    config: Dict[str, Any], 
    client: OpenAI, 
    collection: Collection
):
    """
    Interactive chat loop with the knowledge base.
    """
    print("Welcome to the knowledge base chat! Type 'exit' to quit.")

    while True:
        user_query = input("\nYour question: ")

        if user_query.lower() in ["exit", "quit"]:
            print("Thank you for using the knowledge base chat. Goodbye!")
            break

        # Query the collection
        results = query_chromadb(collection, config, user_query)
        
        # Extract the documents from the results
        document_texts = [doc["text"] for doc in results]
      
        # Get response from completion model
        print("Retrieving relevant information...")
        response = get_chatgpt_response(config, client, user_query, document_texts)

        # Print the response
        print("\nAnswer:", response)
        


def main():
    """
    Main function to run the application.
    """
    # Load environment variables
    load_dotenv()

    # Load configuration
    config = load_config("config/config.yaml")

    # Set OpenAI API key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        logging.error("OpenAI API key not found in environment variables")
        raise ValueError("OpenAI API key not found in environment variables")
    
    logging.info("OpenAI API key loaded successfully")

    # Create ChromaDB client
    client = create_chromadb_client(config)

    # Create ChromaDB collection
    collection = create_chromadb_collection(client, config, openai_api_key)

    # Chunk text and add to ChromaDB
    documents = chunk_text(config)
    
    add_documents_to_chromadb(collection, documents)
    chat_with_knowledge_base(config, OpenAI(api_key=openai_api_key), collection)

    # Close the client

if __name__ == "__main__":
    
    # set up logging
    logging.basicConfig(filename="app.log", level=logging.INFO)

    logging.info("Starting IRS Bot...")
    
    # run the main function 
    main()