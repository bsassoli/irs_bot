import datasets
import pandas as pd
import os
import json
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from ragas import evaluate
from tqdm import tqdm
from irs_bot.app import (
    load_config,
    create_chromadb_client,
    add_documents_to_chromadb,
    chunk_text, query_chromadb,
    get_chatgpt_response
)
import chromadb.utils.embedding_functions as ef
from openai import OpenAI
from langchain.docstore.document import Document  # Import if needed for Document objects

def create_test_collection(client, config, api_key, collection_name):
    """
    Creates a ChromaDB collection for testing with the specified name.
    
    Args:
        client: ChromaDB client instance.
        config: Configuration dictionary containing collection settings.
        api_key: OpenAI API key.
        collection_name: Name for the test collection.
        
    Returns:
        ChromaDB collection instance.
    """
    # Create embedding function
    embedding_function = ef.OpenAIEmbeddingFunction(
        api_key=api_key,
        model_name=config["openai"]["embedding_model"]
    )
    
    # Create or get the collection with the specified name
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function
    )
    
    return collection


def evaluate_with_ragas(qa_data, chunk_sizes, chunk_overlaps, config):
    results = []
    
    # Extract the key components from the qa_data
    queries = qa_data.get("queries", {})
    corpus = qa_data.get("corpus", {})
    relevant_docs = qa_data.get("relevant_docs", {})
    
    if not queries or not corpus:
        raise ValueError("Invalid QA data format: missing 'queries' or 'corpus'")
    
    # Process a subset of queries for testing if needed
    query_ids = list(queries.keys())
    # Uncomment to use a subset of queries
    # query_ids = query_ids[:4]  
    
    for chunk_size in chunk_sizes:
        for chunk_overlap in chunk_overlaps:
            if chunk_overlap >= chunk_size:
                continue
                
            print(f"Testing chunk_size={chunk_size}, chunk_overlap={chunk_overlap}")
            
            try:
                # Modify config
                temp_config = config.copy()
                temp_config["document_processing"]["chunk_size"] = chunk_size
                temp_config["document_processing"]["chunk_overlap"] = chunk_overlap
                
                # Process documents with these parameters
                client = create_chromadb_client(temp_config)
                collection_name = f"test_chunks_{chunk_size}_{chunk_overlap}"

                # Create the test collection
                temp_config["chromadb"]["collection_name"] = collection_name
                api_key = os.getenv("OPENAI_API_KEY")
                if not api_key:
                    raise ValueError("OPENAI_API_KEY environment variable not set")
                    
                collection = create_test_collection(client, temp_config, api_key, collection_name)
                
                # Add all corpus documents to the collection
                # Check your add_documents_to_chromadb function to determine correct format
                try:
                    # Option 1: If function expects Document objects
                    documents = []
                    for doc_id, text in corpus.items():
                        # Use the Document class that matches your environment
                        # This could be langchain.docstore.document.Document or similar
                        documents.append(Document(
                            page_content=text,
                            metadata={"source": doc_id}
                        ))
                except (NameError, ImportError):
                    # Option 2: If function expects dictionary-like objects or can't import Document
                    documents = []
                    for doc_id, text in corpus.items():
                        documents.append({
                            "page_content": text,
                            "metadata": {"source": doc_id}
                        })
                
                add_documents_to_chromadb(collection, documents)
                
                # Prepare evaluation data
                eval_data = []
                for query_id in query_ids:
                    question = queries[query_id]
                    
                    # Get the relevant document texts with error handling
                    ground_truth_doc_ids = relevant_docs.get(query_id, [])
                    ground_truth_texts = []
                    for doc_id in ground_truth_doc_ids:
                        if doc_id in corpus:
                            ground_truth_texts.append(corpus[doc_id])
                        else:
                            print(f"Warning: Document ID {doc_id} referenced in relevant_docs but not found in corpus")
                    
                    ground_truth = "\n".join(ground_truth_texts)
                    
                    # Get RAG response
                    retrieved_results = query_chromadb(collection, temp_config, question)
                    
                    # Verify the structure of retrieved_results
                    retrieved_contexts = []
                    for doc in retrieved_results:
                        if isinstance(doc, dict) and "text" in doc:
                            retrieved_contexts.append(doc["text"])
                        else:
                            # Try to extract text based on your actual structure
                            print(f"Warning: Unexpected structure in retrieved document: {type(doc)}")
                            # You might need to adapt this depending on your actual structure
                            if hasattr(doc, "page_content"):
                                retrieved_contexts.append(doc.page_content)
                    
                    # Skip if no contexts were retrieved
                    if not retrieved_contexts:
                        print(f"Warning: No contexts retrieved for question: {question[:50]}...")
                        continue
                    
                    response = get_chatgpt_response(
                        temp_config, 
                        OpenAI(api_key=api_key),
                        question,
                        retrieved_contexts
                    )
                    
                    eval_data.append({
                        "question": question,
                        "contexts": retrieved_contexts,
                        "answer": response,
                        "ground_truth": ground_truth
                    })
                
                # Skip if no evaluation data
                if not eval_data:
                    print(f"Warning: No evaluation data for chunk_size={chunk_size}, chunk_overlap={chunk_overlap}")
                    continue
                
                # Convert to RAGAS format
                dataset = datasets.Dataset.from_pandas(pd.DataFrame(eval_data))
                
                # Run RAGAS evaluation
                evaluation_result = evaluate(
                    dataset=dataset,
                    metrics=[
                        faithfulness,
                        answer_relevancy,
                        context_precision,
                        context_recall,
                    ]
                )

                # Calculate mean scores for each metric (handling the case where metrics are lists)
                faithfulness_score = evaluation_result["faithfulness"]
                answer_relevancy_score = evaluation_result["answer_relevancy"]
                context_precision_score = evaluation_result["context_precision"]
                context_recall_score = evaluation_result["context_recall"]

                # Convert lists to mean values if necessary
                if isinstance(faithfulness_score, list):
                    faithfulness_score = sum(faithfulness_score) / len(faithfulness_score) if faithfulness_score else 0
                if isinstance(answer_relevancy_score, list):
                    answer_relevancy_score = sum(answer_relevancy_score) / len(answer_relevancy_score) if answer_relevancy_score else 0
                if isinstance(context_precision_score, list):
                    context_precision_score = sum(context_precision_score) / len(context_precision_score) if context_precision_score else 0
                if isinstance(context_recall_score, list):
                    context_recall_score = sum(context_recall_score) / len(context_recall_score) if context_recall_score else 0

                # Record results
                result_entry = {
                    "chunk_size": chunk_size,
                    "chunk_overlap": chunk_overlap,
                    "faithfulness": faithfulness_score,
                    "answer_relevancy": answer_relevancy_score,
                    "context_precision": context_precision_score,
                    "context_recall": context_recall_score,
                    "overall_score": (
                        faithfulness_score + 
                        answer_relevancy_score + 
                        context_precision_score + 
                        context_recall_score
                    ) / 4
                }
                results.append(result_entry)
                print(f"Results for chunk_size={chunk_size}, chunk_overlap={chunk_overlap}:")
                for key, value in result_entry.items():
                    if key != "chunk_size" and key != "chunk_overlap":
                        print(f"  {key}: {value:.4f}")
                
            except Exception as e:
                print(f"Error evaluating chunk_size={chunk_size}, chunk_overlap={chunk_overlap}: {str(e)}")
            finally:
                # Clean up collection even if an error occurred
                try:
                    client.delete_collection(collection_name)
                except Exception as e:
                    print(f"Error deleting collection {collection_name}: {str(e)}")
    
    return pd.DataFrame(results) if results else pd.DataFrame()


if __name__ == "__main__":
    try:
        # Load configuration
        config = load_config("config/config.yaml")
        
        # Load the dataset properly with error handling
        try:
            with open("qa_eval_dataset.json", "r") as f:
                qa_data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading qa_eval_dataset.json: {str(e)}")
            exit(1)
        
        # Print some sample data for verification
        print("Sample queries:")
        for query_id, query_text in list(qa_data.get("queries", {}).items())[:2]:
            print(f"ID: {query_id}, Query: {query_text}")
        
        print("\nSample corpus documents:")
        for doc_id, doc_text in list(qa_data.get("corpus", {}).items())[:2]:
            print(f"ID: {doc_id}, Text: {doc_text[:100]}...")
        
        # Define chunk sizes and overlaps to test
        chunk_sizes = [256, 512, 1024]
        chunk_overlaps = [0, 128, 256]
        
        # Evaluate with RAGAS
        with tqdm(total=len(chunk_sizes) * len(chunk_overlaps), desc="Evaluating chunk sizes and overlaps") as pbar:
            results_df = evaluate_with_ragas(qa_data, chunk_sizes, chunk_overlaps, config)
        
        if results_df.empty:
            print("No results were generated during evaluation.")
            exit(1)
            
        # Save results to CSV
        results_df.to_csv("chunking_evaluation_results.csv", index=False)
        
        # Print best parameters
        best_row = results_df.loc[results_df['overall_score'].idxmax()]
        print(f"\nBest parameters found:")
        print(f"Chunk size: {best_row['chunk_size']}")
        print(f"Chunk overlap: {best_row['chunk_overlap']}")
        print(f"Overall score: {best_row['overall_score']:.4f}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")