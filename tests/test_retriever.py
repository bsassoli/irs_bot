import os
import chromadb
import chromadb.utils.embedding_functions as ef
from llama_index.core.evaluation import generate_question_context_pairs
from typing import List, Tuple, Dict, Any
from chromadb.errors import NotFoundError
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from irs_bot.app import load_config
from llama_index.core.schema import TextNode


def test_generate_qa_pairs(num_docs: int = 5):
    """
    Test generation of question-context pairs from the dataset.
    """
    load_dotenv()
    config = load_config("config/config.yaml")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
        
    openai_ef = ef.OpenAIEmbeddingFunction(
                api_key=openai_api_key,
                model_name=config["openai"]["embedding_model"]
            )

    client = chromadb.PersistentClient(path="./chromadb")
    try:
        collection = client.get_collection(
            name="recipes_for_science",
            embedding_function=openai_ef
        )

    except NotFoundError:
        raise NotFoundError("Collection not found.")
    print("Collection found.")
    
    # 2. Get all documents from the collection
    results = collection.get(
    include=["documents", "metadatas", "embeddings"],
    limit=num_docs  # Adjust based on your collection size
    )
    nodes = []
    for i, doc_text in enumerate(results["documents"]):
    # If you have metadata that includes original document IDs, use that
        doc_id = results["metadatas"][i].get("doc_id", f"doc_{i}") if results["metadatas"] else f"doc_{i}"
        nodes.append(TextNode(text=doc_text, id_=doc_id))

    # Create an LLM instance
    
    llm = OpenAI(
        model=config["openai"]["completion_model"],
        temperature=config["openai"]["temperature"],
    )
    
    qa_pairs = generate_question_context_pairs(
        llm=llm,
        nodes=nodes,  # Use all documents in your index
        num_questions_per_chunk=2,  # Adjust based on your needs
)
    # 5. Save the dataset
    qa_pairs.save_json("qa_eval_dataset.json")
    
    return qa_pairs

if __name__=="__main__":
    
    qa_pairs = test_generate_qa_pairs()
    print(qa_pairs)

