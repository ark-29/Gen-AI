🤖 AI Resume Assistant

An AI-powered resume application built with Streamlit and Google Gemini. It provides two main features: ATS Resume Scoring and AI Resume Analysis.

🚀 Features
🎯 1. ATS Score

Upload your resume as a PDF and optionally provide a Job Description.

With Job Description

The application analyzes how well your resume matches the job and provides:

📊 Job Match Score
✅ Matched Skills
❌ Missing Skills
🔑 Matched Keywords
⚠️ Missing Keywords
💪 Strengths
⚠️ Weaknesses
🚀 Improvement Suggestions
Without Job Description

The application performs a general ATS compatibility analysis without assuming a specific job.

📄 2. Resume Analyzer

Upload your resume and get a detailed AI-powered analysis:

📊 Resume Score
📝 Resume Summary
💻 Technical Skills
🤝 Soft Skills
🎓 Education
🚀 Projects
💼 Experience
💪 Strengths
⚠️ Weaknesses
🚀 Suggestions
🛠️ Tech Stack
Python
Streamlit — User interface
Google Gemini API — AI analysis
PyPDF — PDF text extraction
python-dotenv — Environment variable management
📁 Project Structure
Resume/
│
├── interface.py
├── ATS.py
├── analyzer.py
├── text.py
├── requirements.txt
├── .gitignore
│
└── sample/
    └── sample_resume.pdf
File Description
File	Purpose
interface.py	Main Streamlit application
ATS.py	ATS scoring and job matching using Gemini
analyzer.py	General resume analysis using Gemini
text.py	Extracts text from PDF resumes
requirements.txt	Python dependencies
sample/	Sample resume for testing
⚙️ Setup
1. Clone the repository
git clone <your-repository-url>
cd Resume
2. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Create .env

Create a .env file in the project directory:

GEMINI_API_KEY=your_gemini_api_key

Do not upload .env to GitHub.

Make sure your .gitignore contains:

.env
venv/
__pycache__/
5. Run the application
streamlit run interface.py

The application will open in your browser.

🔐 API Key

This project uses the Google Gemini API for AI-powered resume analysis.

Store your API key in .env:

GEMINI_API_KEY=your_api_key

Never commit your API key to GitHub.

🧪 Testing

A sample resume is included in:

sample/sample_resume.pdf

You can use it to test both:

ATS Score
Resume Analyzer
☁️ Deployment

The application can be deployed using Streamlit Community Cloud.

After pushing the project to GitHub:

Connect your GitHub repository.
Select interface.py as the main file.
Add GEMINI_API_KEY under the deployment's secrets.
Deploy the application.
⚠️ Notes
Resume files are processed for analysis and are not permanently stored by this application.
The Job Description is optional for ATS analysis.
Resume Analyzer does not require a Job Description.
Gemini API usage may be subject to Google's API limits and quotas.
🎯 Project Goal

The goal of this project is to build a practical Generative AI application that helps job seekers understand their resume quality, ATS compatibility, and areas for improvement.

📌 Future Improvements

Potential future features:

Resume improvement/rewrite
Resume-to-job compatibility percentage
Multiple resume formats
Downloadable analysis report
User authentication
Resume version tracking
Deployment with a production backend

Built with Python, Streamlit, and Google Gemini 🤖
