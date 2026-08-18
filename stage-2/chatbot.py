from google import genai
from dotenv import load_dotenv
import os
import time
import speech_recognition as sr

recognizer=sr.Recognizer()
load_dotenv()

gemini=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

memory=[]
max_tries=3

def audio_text():
    with sr.Microphone() as source:
        print("Listening....")
        audio=recognizer.listen(source)

    try:
        text=recognizer.recognize_google(audio)
        print("User: ",text)
        return text
    except Exception as e:
        print("Error!!  ",e)
        return None

while True:
    print("Choose input mode \n 1.Text \n 2.Audio")
    choice=input("Enter your choice: ")
    if choice=="1":
        user_input=input("Enter What You to know:  ")
    elif choice=="2":
        user_input=audio_text()
        if user_input is None:
            continue
    else:
        print("Enter A valid choice.")
        continue

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
                "role":"model",
                "parts":[{"text":full_answer}]
            })
            break
        except Exception as e:
            if i == max_tries-1:
                print("\n request failed",e)
            else:
                wait_time=2**i
                print(f"\n Request Failed try again in {wait_time}")
                time.sleep(wait_time)