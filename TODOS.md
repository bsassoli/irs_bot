# TODOS FOR IRS_BOT

- [ ] Add chapter and section to chunks in metadata
- [x] Develop evals to test chunking strategy
- [ ] Find optimal chunking strategy using evaluate_chunking.py
- [ ] Test other open source embeddings
- [ ] Test other models for the chatbot
- [x] Implement different chunking strategies
- [x] Develop evals for retrieval
- [ ] Develop evals for completeness
- [ ] Finalize textbook markdown for ingestion
- [ ] Coverage

## Implemented Features

### Chunking Evaluation
- Created chunking evaluation module in `src/irs_bot/chunking_eval.py`
- Added test file in `tests/test_chunking.py`
- Created evaluation script `evaluate_chunking.py`
- Supports multiple chunking strategies:
  - Markdown header-based chunking
  - Character-based chunking with various sizes
  - Token-based chunking with various sizes
  - Sentence-based chunking with various sizes
- Evaluation metrics include:
  - Mean Reciprocal Rank (MRR)
  - Hit Rate
  - Context Relevancy 
  - Document statistics (count and length)


