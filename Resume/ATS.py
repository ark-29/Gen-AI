from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

gemini=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_ats(resume_text,job_description=None):
    if job_description:

        prompt = f"""
You are an Expert ATS Resume Analyzer.

Analyze the resume against the provided job description.

Resume:
{resume_text}

Job Description:
{job_description}

Evaluate:

1. Overall match score out of 100
2. Skills matched between resume and job description
3. Skills missing from the resume
4. Important keywords found in the resume
5. Important keywords missing from the resume
6. Relevant experience
7. Relevant projects
8. Strengths of the resume for this job
9. Weaknesses of the resume for this job
10. Specific suggestions to improve the resume for this job

Return ONLY valid JSON in this format:

{{
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "matched_keywords": [],
    "missing_keywords": [],
    "relevant_experience": [],
    "relevant_projects": [],
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}

Add a small amount of humor while describing the resume analysis.
"""

    else:

        prompt = f"""
You are an Expert ATS Resume Analyzer.

Analyze the following resume for general ATS compatibility.

Resume:
{resume_text}

Evaluate:

1. Overall ATS score out of 100
2. Technical skills detected
3. Important keywords found in the resume
4. Potential keywords that could improve ATS compatibility
5. Relevant experience
6. Relevant projects
7. Strengths of the resume
8. Weaknesses of the resume
9. Specific suggestions to improve ATS compatibility

Since no job description was provided, do NOT invent a target job
or claim that a skill is missing from a specific job description.

Return ONLY valid JSON in this format:

{{
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "matched_keywords": [],
    "missing_keywords": [],
    "relevant_experience": [],
    "relevant_projects": [],
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}

Add a small amount of humor while describing the resume analysis.
"""
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