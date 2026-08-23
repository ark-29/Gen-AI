import streamlit as st
from text import extract_text
from ATS import analyze_ats
from analyzer import resume_analyzer


st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("AI Resume Assistant")
st.write("Analyze your resume or Check ATS Score.")

st.divider()

option = st.radio(
    "Choose",
    [
        "Check ATS Score",
        "Resume Analyzer"
    ],
    horizontal=True
)

st.divider()


if option == "Check ATS Score":

    st.header("Check ATS")

    st.write(
        "Upload your resume [PDF] and optionally provide a job description."
    )

    resume = st.file_uploader(
        "Upload your resume",
        type=["pdf"]
    )

    job_description = st.text_area(
        "Job Description (Optional)",
        height=250,
        placeholder="Paste the job description here..."
    )

    if st.button(
        "Check ATS",
        use_container_width=True
    ):

        if resume is None:

            st.warning(
                "Please upload your Resume."
            )

        else:

            with st.spinner(
                "Analyzing Your Resume..."
            ):

                resume_text = extract_text(resume)

                if not resume_text.strip():

                    st.warning(
                        "Could not Extract text from PDF."
                    )

                else:

                    if job_description.strip():

                        result = analyze_ats(
                            resume_text,
                            job_description
                        )

                    else:

                        result = analyze_ats(
                            resume_text
                        )

            if "error" in result:

                st.error(
                    f"Analysis failed: {result['error']}"
                )

            else:

                if job_description.strip():

                    st.success(
                        "Job specific analysis completed!"
                    )

                    st.subheader(
                        "🎯 Job Match Score"
                    )

                else:

                    st.success(
                        "General ATS analysis completed!"
                    )

                    st.subheader(
                        "📊 ATS Compatibility Score"
                    )

                st.metric(
                    "Match Score",
                    f"{result['match_score']}/100"
                )

                st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader(
                        "✅ Matched Skills"
                    )

                    for item in result["matched_skills"]:

                        st.write(
                            f"• {item}"
                        )

                with col2:

                    st.subheader(
                        "❌ Missing Skills"
                    )

                    for item in result["missing_skills"]:

                        st.write(
                            f"• {item}"
                        )

                st.subheader(
                    "🔑 Matched Keywords"
                )

                for item in result["matched_keywords"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "⚠️ Missing Keywords"
                )

                for item in result["missing_keywords"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "💼 Relevant Experience"
                )

                for item in result["relevant_experience"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "🚀 Relevant Projects"
                )

                for item in result["relevant_projects"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "💪 Strengths"
                )

                for item in result["strengths"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "⚠️ Weaknesses"
                )

                for item in result["weaknesses"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "🚀 Suggestions"
                )

                for item in result["suggestions"]:

                    st.write(
                        f"• {item}"
                    )


else:

    st.header(
        "Resume Analyzer"
    )

    st.write(
        "Upload your resume and get a detailed AI analysis."
    )

    resume = st.file_uploader(
        "Upload your resume",
        type=["pdf"]
    )

    if st.button(
        "Analyze",
        use_container_width=True
    ):

        if resume is None:

            st.warning(
                "Please Upload your Resume."
            )

        else:

            with st.spinner(
                "Analyzing Your Resume..."
            ):

                resume_text = extract_text(resume)

                if not resume_text.strip():

                    st.warning(
                        "Could not Extract text from PDF."
                    )

                else:

                    result = resume_analyzer(
                        resume_text
                    )

            if "error" in result:

                st.error(
                    f"Analysis failed: {result['error']}"
                )

            else:

                st.success(
                    "Resume analysis completed!"
                )

                st.divider()

                st.subheader(
                    "📊 Resume Score"
                )

                st.metric(
                    "Resume Score",
                    f"{result['resume_score']}/100"
                )

                st.subheader(
                    "📝 Summary"
                )

                st.write(
                    result["summary"]
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader(
                        "💻 Technical Skills"
                    )

                    for item in result["technical_skills"]:

                        st.write(
                            f"• {item}"
                        )

                with col2:

                    st.subheader(
                        "🤝 Soft Skills"
                    )

                    for item in result["soft_skills"]:

                        st.write(
                            f"• {item}"
                        )

                st.subheader(
                    "🎓 Education"
                )

                for item in result["education"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "🚀 Projects"
                )

                for item in result["projects"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "💼 Experience"
                )

                for item in result["experience"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "💪 Strengths"
                )

                for item in result["strengths"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "⚠️ Weaknesses"
                )

                for item in result["weaknesses"]:

                    st.write(
                        f"• {item}"
                    )

                st.subheader(
                    "🚀 Suggestions"
                )

                for item in result["suggestions"]:

                    st.write(
                        f"• {item}"
                    )
