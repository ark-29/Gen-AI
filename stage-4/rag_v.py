from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader
import numpy as np
import os
import json

load_dotenv()

path = "Problem Solving- UNIT I- PART II.pdf"

gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

reader = PdfReader(path)

vector_store_file = "vector_store.json"

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"


def embedding(text):

    embed = gemini.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return embed.embeddings[0].values


def chunking(text, chunk_size=1000, overlap=300):

    start = 0
    chunks = []

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if os.path.exists(vector_store_file):

    print("Loading existing vector store...")

    with open(
        vector_store_file,
        "r",
        encoding="utf-8"
    ) as file:

        vector_db = json.load(file)

    print("Vector store loaded!")

else:

    print("Vector store not found.")
    print("Creating embeddings...")

    chunks = chunking(text)

    vector_db = []

    for i, chunk in enumerate(chunks):

        print(
            f"Embedding chunk "
            f"{i + 1}/{len(chunks)}"
        )

        vector = embedding(chunk)

        vector_db.append(
            {
                "text": chunk,
                "embedding": vector
            }
        )

    with open(
        vector_store_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            vector_db,
            file
        )

    print("Vector store created and saved!")


print(
    "Number of chunks:",
    len(vector_db)
)


def calc_cosine_similarity(vector1, vector2):

    vector1 = np.array(
        vector1,
        dtype=float
    )

    vector2 = np.array(
        vector2,
        dtype=float
    )

    similarity_score = np.dot(
        vector1,
        vector2
    ) / (
        np.linalg.norm(vector1)
        *
        np.linalg.norm(vector2)
    )

    return similarity_score


def reranking(question, candidates):

    candidate_text = ""

    for number, (similarity_score, index) in enumerate(candidates):

        chunk = vector_db[index]["text"]

        candidate_text += f"""
CANDIDATE{number}

{chunk}

"""

    prompt = f"""
You are a relevance evaluator.

Your task is to determine how relevant each candidate chunk is to the question.

Question:
{question}

Candidate Chunks:

{candidate_text}

Give a relevance score from 0 to 10.

10 = directly answers the question
8-9 = highly relevant
5-7 = somewhat relevant
1-4 = weakly relevant
0 = completely irrelevant

Return ONLY a JSON array like this:

[
    {{"candidate": 0, "score": 9}},
    {{"candidate": 1, "score": 4}},
    {{"candidate": 2, "score": 8}}
]

Include all candidates exactly once.
"""

    response = gemini.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    try:

        clean_response = response.text.strip()

        if clean_response.startswith("```"):

            clean_response = clean_response.replace(
                "```json",
                ""
            )

            clean_response = clean_response.replace(
                "```",
                ""
            )

            clean_response = clean_response.strip()

        results = json.loads(
            clean_response
        )

    except:

        print(
            "Could not parse reranking response."
        )

        print(response.text)

        return []

    reranked = []

    for item in results:

        candidate_number = item["candidate"]

        if isinstance(
            candidate_number,
            str
        ):

            candidate_number = candidate_number.replace(
                "CANDIDATE",
                ""
            )

            candidate_number = int(
                candidate_number
            )

        relevance_score = item["score"]

        original_index = candidates[
            candidate_number
        ][1]

        reranked.append(
            (
                relevance_score,
                original_index
            )
        )

    reranked.sort(
        reverse=True
    )

    return reranked


chat_history = []

while True:

    question = input(
        "\nEnter Your Query: "
    )

    if question.lower() == "exit":

        print("GoodBye!!")

        break

    question_embed = embedding(
        question
    )

    scores = []

    for index, item in enumerate(vector_db):

        score = calc_cosine_similarity(
            question_embed,
            item["embedding"]
        )

        scores.append(
            (score, index)
        )

    scores.sort(
        reverse=True
    )

    retrieve_k = 10

    candidates = scores[:retrieve_k]

    reranked_result = reranking(
        question,
        candidates
    )

    top_k = 3

    top_results = reranked_result[:top_k]

    context = ""

    for score, index in top_results:

        context += (
            vector_db[index]["text"]
            +
            "\n\n"
        )

    chat_history.append(
        {
            "role": "user",
            "parts": [
                f"""
Context:
{context}

Question:
{question}
"""
            ]
        }
    )

    model_prompt = f"""
You are a document-based AI assistant.

Answer the user's question using the provided context.

If the answer is not available in the context,
say that the information is not available in the provided document.

Use the previous conversation to understand follow-up questions.

Conversation:
{chat_history}
"""

    response = gemini.models.generate_content(
        model="gemini-3.5-flash",
        contents=model_prompt
    )

    print(
        "\n================================"
    )

    print(
        "        MODEL RESPONSE"
    )

    print(
        "================================"
    )

    print(
        response.text
    )

    chat_history.append(
        {
            "role": "model",
            "parts": [
                response.text
            ]
        }
    )