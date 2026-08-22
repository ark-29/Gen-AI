# Stage 4 - RAG Application

A simple Retrieval-Augmented Generation (RAG) application built using Python and the Gemini API.

This project allows users to ask questions about the content of a PDF. The application retrieves relevant sections from the document using embeddings and cosine similarity, reranks the retrieved chunks using Gemini, and generates an answer using the most relevant context.

## Features

- PDF text extraction using PyPDF
- Text chunking with overlap
- Vector embeddings using Gemini Embedding
- Local JSON-based vector store
- Semantic search using cosine similarity
- Top-K document retrieval
- LLM-based reranking
- Context-based answer generation
- Chat history for follow-up questions
- Interactive command-line interface

## RAG Pipeline

The application follows this pipeline:

```text
PDF
 │
 ▼
Extract Text
 │
 ▼
Chunking
 │
 ▼
Gemini Embeddings
 │
 ▼
Vector Store
 │
 ▼
User Question
 │
 ▼
Question Embedding
 │
 ▼
Cosine Similarity
 │
 ▼
Top 10 Candidates
 │
 ▼
Gemini Reranking
 │
 ▼
Top 3 Relevant Chunks
 │
 ▼
Context + Chat History
 │
 ▼
Gemini
 │
 ▼
Final Answer
