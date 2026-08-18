from google import genai
from dotenv import load_dotenv
import os
import time
load_dotenv()

gemini=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

memory=[]
max_tries=3
while True:

    user_input=input("Enter What You to know:  ")

    if user_input.lower() == "break" or user_input.lower()=="exit":
        print("Thank You!!")
        break

    memory.append({
        "role":"user",
        "parts":[{"text":user_input}]
    })
    for i in range(max_tries):
        try:
            response=gemini.models.generate_content_stream(
                model="gemini-3.5-flash",
                contents=memory
            )

            full_answer=""
            for piece in response:
                print(piece.text,end=" ",flush=True)
                full_answer+=piece.text
            
            print()

            memory.append({
                "role":"Model",
                "parts":[{"text":full_answer}]
            })
        except Exception as e:
            if i == max_tries-1:
                print("\n request failed",e)
            else:
                wait_time=2**max_tries
                print(f"\n Request Failed try again in {wait_time}")
                time.sleep(wait_time)