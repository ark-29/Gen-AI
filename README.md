# Gen-AI
Lets Do something !!!

# Stage 1 — First LLM API Application

## Overview

This project is a simple Python application that sends a user-provided prompt to Google's Gemini API and displays the generated response.

The purpose of this project is to understand the basic interaction between a Python application and an LLM through an API.

## Architecture

```text
User Prompt
     ↓
Python Application
     ↓
Gemini API
     ↓
Gemini LLM
     ↓
Generated Response
     ↓
Python Application
     ↓
Terminal
```

## Technologies Used

* Python
* Google Gemini API
* `google-genai`
* `python-dotenv`
* Git & GitHub

## Project Structure

```text
stage-1/
├── llm_api.py
├── README.md
└── .env
```

The `.env` file contains the API key and is excluded from Git using `.gitignore`.

## How It Works

1. The application loads the Gemini API key from the `.env` file.
2. A Gemini client is created using the API key.
3. The user enters a prompt.
4. The prompt is sent to the Gemini model through the API.
5. Gemini generates a response.
6. The application extracts the response text and displays it in the terminal.

## How to Run

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate it

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -U google-genai python-dotenv
```

### 4. Create `.env`

```text
GEMINI_API_KEY=your_api_key_here
```

### 5. Run

```bash
python llm_api.py
```

## Example

```text
Enter your prompt: Explain machine learning in simple terms

Gemini: Machine learning is a way for computers to learn
patterns from data and use those patterns to make predictions
or decisions.
```

## Security

The Gemini API key is stored in an environment variable and is **not committed to GitHub**.

The `.env` file is included in `.gitignore`.

