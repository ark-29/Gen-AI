from google import genai
from dotenv import load_dotenv
import os
import json

gemini=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def resume_analyzer(resume_text):
    prompt=f"""
You are an expert resume reviewer.

Analyze the following resume carefully.

RESUME:
{resume_text}

Provide a detailed analysis covering:

1. Overall resume score out of 100
2. Professional summary
3. Technical skills
4. Soft skills
5. Education
6. Projects
7. Work experience
8. Strengths
9. Weaknesses
10. Suggestions for improvement

Do not invent information that is not present in the resume.

Return ONLY valid JSON in this format:
{{
    "resume_score": 0,
    "summary": "",
    "technical_skills": [],
    "soft_skills": [],
    "education": [],
    "projects": [],
    "experience": [],
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}"""
    try:
            response = gemini.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )
    
            result = response.text.strip()
    
            if result.startswith("```"):
    
                result = result.replace(
                    "```json",
                    ""
                )
    
                result = result.replace(
                    "```",
                    ""
                )
    
                result = result.strip()
    
            return json.loads(result)
    except Exception as e:
        return {
            "error":str(e)
        }