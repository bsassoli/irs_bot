#!/usr/bin/env python
import os
import json
import logging
import time
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
import pandas as pd

# Import app components
from src.irs_bot.app import (
    load_config, 
    create_chromadb_client, 
    create_chromadb_collection,
    chunk_text, 
    add_documents_to_chromadb,
    query_chromadb,
    get_chatgpt_response
)

from openai import OpenAI
from tests.test_questions import TEST_QUESTIONS, TEST_ANSWERS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('rag_evaluation.log')
    ]
)

# Constants for evaluation
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

SYSTEM_PROMPT_TEMPLATE = """
You are a philosophy professor who teaches the philosophy of science.
{style_instructions}
Context: {context}
Question: {query}
"""

EVALUATION_PROMPT = """
You are an expert evaluator for RAG systems. Evaluate the following response based on the reference answer provided.

Question: {question}

Reference Answer: {reference}

System Response: {response}

Evaluate the system response on three dimensions:
1. Relevance (0-10): How relevant is the response to the question? Score 0 if completely irrelevant, 10 if perfectly relevant.
2. Completeness (0-10): How complete is the response compared to the reference? Score 0 if it misses all key points, 10 if it covers all key points.
3. Accuracy (0-10): How accurate is the response compared to the reference? Score 0 if it contains major errors, 10 if it's perfectly accurate.

Provide your evaluation as a JSON object with the following format:
{{"relevance": score, "completeness": score, "accuracy": score, "explanation": "your reasoning"}}
"""

def setup_evaluation_environment(config_path: str, openai_key: str) -> Tuple[Dict[str, Any], OpenAI]:
    """Setup environment for evaluation."""
    logging.info("Setting up evaluation environment")
    
    # Load configuration
    config = load_config(config_path)
    
    # Initialize OpenAI client
    openai_client = OpenAI(api_key=openai_key)
    
    return config, openai_client

def modify_config_for_chunking(config: Dict[str, Any], chunking_strategy: Dict[str, Any]) -> Dict[str, Any]:
    """Modify config with specific chunking strategy."""
    modified_config = config.copy()
    modified_config["document_processing"]["chunk_size"] = chunking_strategy["chunk_size"]
    modified_config["document_processing"]["chunk_overlap"] = chunking_strategy["chunk_overlap"]
    modified_config["chromadb"]["persist_directory"] = f"chromadb_{chunking_strategy['name']}"
    modified_config["chromadb"]["collection_name"] = f"collection_{chunking_strategy['name']}"
    
    return modified_config

def apply_chunking_strategy(config: Dict[str, Any], api_key: str) -> Tuple[Dict[str, Any], int]:
    """Apply chunking strategy and return updated config and number of chunks."""
    logging.info(f"Applying chunking strategy: size={config['document_processing']['chunk_size']}, overlap={config['document_processing']['chunk_overlap']}")
    
    # Create ChromaDB client
    client = create_chromadb_client(config)
    
    # Create ChromaDB collection
    collection = create_chromadb_collection(client, config, api_key)
    
    # Process document and add to collection
    documents = chunk_text(config)
    
    # Check if collection is empty
    if collection.count() == 0:
        add_documents_to_chromadb(collection, documents)
    
    # Update config with collection info
    config["_collection"] = collection
    config["_client"] = client
    
    return config, len(documents)

def evaluate_rag_system(
    config: Dict[str, Any],
    openai_client: OpenAI,
    test_questions: List[str],
    test_answers: List[str],
    prompt_style: str,
) -> List[Dict[str, Any]]:
    """Evaluate RAG system with given config and test questions."""
    logging.info(f"Evaluating with prompt style: {prompt_style}")
    
    # Get collection from config
    collection = config["_collection"]
    
    # Set test prompt
    import src.irs_bot.prompt
    original_prompt = src.irs_bot.prompt.PROMPT
    style_instructions = PROMPT_STYLES[prompt_style]
    test_prompt = SYSTEM_PROMPT_TEMPLATE.format(style_instructions=style_instructions, context="{context}", query="{query}")
    src.irs_bot.prompt.PROMPT = test_prompt
    
    results = []
    
    for i, question in enumerate(test_questions):
        # Skip malformed questions
        if not question.strip():
            continue
            
        logging.info(f"Processing question {i+1}/{len(test_questions)}: {question[:50]}...")
        
        try:
            # Query ChromaDB
            query_results = query_chromadb(collection, config, question)
            
            # Extract document texts
            document_texts = [doc["text"] for doc in query_results]
            
            # Get response from GPT
            start_time = time.time()
            response = get_chatgpt_response(config, openai_client, question, document_texts)
            response_time = time.time() - start_time
            
            # Evaluate response against reference answer
            eval_result = evaluate_response(openai_client, question, test_answers[i], response)
            
            # Save result
            result = {
                "question": question,
                "context": document_texts,
                "response": response,
                "reference": test_answers[i],
                "evaluation": eval_result,
                "prompt_style": prompt_style,
                "chunk_size": config["document_processing"]["chunk_size"],
                "chunk_overlap": config["document_processing"]["chunk_overlap"],
                "chunk_strategy": config["chromadb"]["collection_name"],
                "response_time": response_time
            }
            
            results.append(result)
            
        except Exception as e:
            logging.error(f"Error processing question: {str(e)}")
    
    # Restore original prompt
    src.irs_bot.prompt.PROMPT = original_prompt
    
    return results

def evaluate_response(
    openai_client: OpenAI, 
    question: str, 
    reference: str, 
    response: str
) -> Dict[str, Any]:
    """Evaluate response against reference using GPT."""
    try:
        eval_prompt = EVALUATION_PROMPT.format(
            question=question,
            reference=reference,
            response=response
        )
        
        eval_response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert evaluator for RAG systems."},
                {"role": "user", "content": eval_prompt}
            ],
            temperature=0.2
        )
        
        # Parse the evaluation response
        eval_text = eval_response.choices[0].message.content
        
        # Extract JSON from the response
        try:
            # Find JSON object in the text
            start_idx = eval_text.find('{')
            end_idx = eval_text.rfind('}') + 1
            
            if start_idx >= 0 and end_idx > start_idx:
                json_str = eval_text[start_idx:end_idx]
                eval_result = json.loads(json_str)
            else:
                # Fallback to default scoring
                eval_result = {
                    "relevance": 5,
                    "completeness": 5,
                    "accuracy": 5,
                    "explanation": "Failed to parse evaluation result"
                }
        except json.JSONDecodeError:
            # Another fallback
            eval_result = {
                "relevance": 5,
                "completeness": 5,
                "accuracy": 5,
                "explanation": "Failed to parse JSON from evaluation"
            }
            
        return eval_result
        
    except Exception as e:
        logging.error(f"Error in evaluation: {str(e)}")
        return {
            "relevance": 0,
            "completeness": 0,
            "accuracy": 0,
            "explanation": f"Evaluation failed: {str(e)}"
        }

def save_evaluation_results(results: List[Dict[str, Any]]) -> None:
    """Save evaluation results to file."""
    results_dir = Path("evaluation_results")
    results_dir.mkdir(exist_ok=True)
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = results_dir / f"eval_results_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    logging.info(f"Results saved to {filename}")
    return filename

def generate_evaluation_report(results_path: str) -> str:
    """Generate evaluation report from results."""
    logging.info("Generating evaluation report")
    
    # Load results
    with open(results_path, 'r') as f:
        results = json.load(f)
    
    # Convert to DataFrame for analysis
    df = pd.DataFrame([{
        'question': r['question'],
        'prompt_style': r['prompt_style'],
        'chunk_strategy': r['chunk_strategy'],
        'chunk_size': r['chunk_size'],
        'chunk_overlap': r['chunk_overlap'],
        'relevance': r['evaluation']['relevance'],
        'completeness': r['evaluation']['completeness'],
        'accuracy': r['evaluation']['accuracy'],
        'response_time': r.get('response_time', 0),
        'overall_score': (r['evaluation']['relevance'] + r['evaluation']['completeness'] + r['evaluation']['accuracy']) / 3
    } for r in results])
    
    # Create report directory
    report_dir = Path("evaluation_reports")
    report_dir.mkdir(exist_ok=True)
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    report_path = report_dir / f"evaluation_report_{timestamp}.html"
    
    # Group by prompt style and chunking strategy
    grouped_by_strategy = df.groupby(['prompt_style', 'chunk_strategy']).mean()
    grouped_by_strategy = grouped_by_strategy.reset_index()
    
    # Plot results
    generate_evaluation_charts(df, report_dir, timestamp)
    
    # Generate HTML report
    html_content = f"""
    <html>
    <head>
        <title>RAG Evaluation Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1, h2 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
            th, td {{ padding: 8px; text-align: left; border: 1px solid #ddd; }}
            th {{ background-color: #f2f2f2; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
            .chart-container {{ margin: 20px 0; }}
            .highlight {{ background-color: #ffffcc; }}
        </style>
    </head>
    <body>
        <h1>RAG Evaluation Report</h1>
        <p>Generated on {time.strftime("%Y-%m-%d %H:%M:%S")}</p>
        
        <h2>Overall Results</h2>
        <p>Average overall score: {df['overall_score'].mean():.2f}/10</p>
        
        <h2>Best Performing Configurations</h2>
        <table>
            <tr>
                <th>Prompt Style</th>
                <th>Chunk Strategy</th>
                <th>Relevance</th>
                <th>Completeness</th>
                <th>Accuracy</th>
                <th>Overall Score</th>
                <th>Response Time (s)</th>
            </tr>
    """
    
    # Sort by overall score
    sorted_results = grouped_by_strategy.sort_values('overall_score', ascending=False)
    
    for _, row in sorted_results.iterrows():
        html_content += f"""
            <tr>
                <td>{row['prompt_style']}</td>
                <td>{row['chunk_strategy']}</td>
                <td>{row['relevance']:.2f}</td>
                <td>{row['completeness']:.2f}</td>
                <td>{row['accuracy']:.2f}</td>
                <td>{row['overall_score']:.2f}</td>
                <td>{row['response_time']:.2f}</td>
            </tr>
        """
    
    html_content += """
        </table>
        
        <h2>Evaluation Charts</h2>
        <div class="chart-container">
            <img src="prompt_style_comparison.png" alt="Prompt Style Comparison" width="80%">
        </div>
        <div class="chart-container">
            <img src="chunking_strategy_comparison.png" alt="Chunking Strategy Comparison" width="80%">
        </div>
        <div class="chart-container">
            <img src="combined_metrics.png" alt="Combined Metrics" width="80%">
        </div>
        
        <h2>Question-Level Results</h2>
        <table>
            <tr>
                <th>Question</th>
                <th>Prompt Style</th>
                <th>Chunk Strategy</th>
                <th>Relevance</th>
                <th>Completeness</th>
                <th>Accuracy</th>
                <th>Overall Score</th>
            </tr>
    """
    
    for _, row in df.iterrows():
        html_content += f"""
            <tr>
                <td>{row['question'][:50]}...</td>
                <td>{row['prompt_style']}</td>
                <td>{row['chunk_strategy']}</td>
                <td>{row['relevance']:.2f}</td>
                <td>{row['completeness']:.2f}</td>
                <td>{row['accuracy']:.2f}</td>
                <td>{row['overall_score']:.2f}</td>
            </tr>
        """
    
    html_content += """
        </table>
    </body>
    </html>
    """
    
    with open(report_path, 'w') as f:
        f.write(html_content)
    
    logging.info(f"Report generated at {report_path}")
    
    return str(report_path)

def generate_evaluation_charts(df: pd.DataFrame, report_dir: Path, timestamp: str) -> None:
    """Generate charts for evaluation results."""
    # Chart 1: Prompt Style Comparison
    plt.figure(figsize=(12, 6))
    prompt_comparison = df.groupby('prompt_style').mean()
    metrics = ['relevance', 'completeness', 'accuracy', 'overall_score']
    
    prompt_comparison[metrics].plot(kind='bar', ax=plt.gca())
    plt.title('Performance by Prompt Style')
    plt.ylabel('Score (0-10)')
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(report_dir / 'prompt_style_comparison.png')
    
    # Chart 2: Chunking Strategy Comparison
    plt.figure(figsize=(12, 6))
    chunk_comparison = df.groupby('chunk_strategy').mean()
    chunk_comparison[metrics].plot(kind='bar', ax=plt.gca())
    plt.title('Performance by Chunking Strategy')
    plt.ylabel('Score (0-10)')
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(report_dir / 'chunking_strategy_comparison.png')
    
    # Chart 3: Combined metrics heatmap
    plt.figure(figsize=(12, 8))
    combined_data = df.pivot_table(
        values='overall_score', 
        index='prompt_style', 
        columns='chunk_strategy'
    )
    
    plt.imshow(combined_data, cmap='YlGn', aspect='auto', vmin=0, vmax=10)
    plt.colorbar(label='Overall Score')
    plt.title('Performance Matrix (Prompt Style × Chunking Strategy)')
    plt.xticks(range(len(combined_data.columns)), combined_data.columns, rotation=45)
    plt.yticks(range(len(combined_data.index)), combined_data.index)
    
    # Add text annotations
    for i in range(len(combined_data.index)):
        for j in range(len(combined_data.columns)):
            value = combined_data.iloc[i, j]
            plt.text(j, i, f'{value:.2f}', ha='center', va='center', 
                     color='black' if value > 5 else 'white')
    
    plt.tight_layout()
    plt.savefig(report_dir / 'combined_metrics.png')

def run_evaluation() -> None:
    """Run full evaluation of RAG system."""
    # Load environment variables
    load_dotenv()
    
    # Get OpenAI API key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API key not found in environment variables")
    
    # Setup evaluation environment
    base_config, openai_client = setup_evaluation_environment("config/config.yaml", openai_api_key)
    
    all_results = []
    
    # Test different combinations of chunking strategies and prompt styles
    for chunking_strategy in CHUNKING_STRATEGIES:
        # Modify config for chunking strategy
        config = modify_config_for_chunking(base_config, chunking_strategy)
        
        # Apply chunking strategy
        config, num_chunks = apply_chunking_strategy(config, openai_api_key)
        logging.info(f"Chunking strategy {chunking_strategy['name']} resulted in {num_chunks} chunks")
        
        # Test different prompt styles
        for prompt_style in PROMPT_STYLES:
            # Evaluate RAG system
            results = evaluate_rag_system(
                config, 
                openai_client, 
                TEST_QUESTIONS, 
                TEST_ANSWERS,
                prompt_style
            )
            
            all_results.extend(results)
    
    # Save results
    results_path = save_evaluation_results(all_results)
    
    # Generate report
    report_path = generate_evaluation_report(results_path)
    
    print(f"Evaluation complete. Report generated at {report_path}")

if __name__ == "__main__":
    run_evaluation()