from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

user=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_input=input("Enter What you want: ")

response=user.models.generate_content(
    model="gemini-3.5-flash",
    contents=user_input
)

print("\n Response: ",response.text)