import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# ==========================================
# GEMINI CONFIGURATION
# ==========================================

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)


model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================================
# PDF TEXT EXTRACTION
# ==========================================

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

# ==========================================
# GENERATE INTERVIEW QUESTIONS + ANSWERS
# ==========================================

def generate_questions(resume_text, role):

    prompt = f"""
    You are an expert interviewer.

    Analyze the resume and generate interview preparation content.

    Target Role:
    {role}

    Resume:
    {resume_text}

    Generate:

    ==================================
    HR QUESTIONS
    ==================================

    5 HR Questions.

    After each question leave 2 blank lines.

    Then provide:

    Sample Answer:

    ==================================
    TECHNICAL QUESTIONS
    ==================================

    5 Technical Questions.

    After each question leave 2 blank lines.

    Then provide:

    Sample Answer:

    ==================================
    PROJECT QUESTIONS
    ==================================

    5 Project-Based Questions.

    Questions must be based on projects mentioned in the resume.

    After each question leave 2 blank lines.

    Then provide:

    Sample Answer:

    Keep answers simple and suitable for a fresher.
    """

    response = model.generate_content(prompt)

    return response.text

# ==========================================
# GENERATE MOCK INTERVIEW QUESTIONS
# ==========================================

def generate_mock_questions(resume_text, role):

    prompt = f"""
    Based on the resume and target role,
    generate exactly 3 interview questions.

    The questions should be:
    - Resume based
    - Personalized
    - Suitable for a real interview

    Target Role:
    {role}

    Resume:
    {resume_text}

    Return only questions.

    One question per line.
    """

    response = model.generate_content(prompt)

    questions = []

    for line in response.text.split("\n"):

        line = line.strip()

        if line and "?" in line:
            questions.append(line)

    return questions[:3]

# ==========================================
# EVALUATE ANSWERS
# ==========================================

def evaluate_answer(question, answer):

    prompt = f"""
    You are an expert interview evaluator.

    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer.

    Give output in this format:

    Score: X/10

    Strengths:
    - Point 1
    - Point 2

    Improvements:
    - Point 1
    - Point 2

    Suggested Better Answer:
    Provide a concise improved answer.
    """

    response = model.generate_content(prompt)

    return response.text

# ==========================================
# STREAMLIT PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Interview Prep Assistant",
    layout="wide"
)

# ==========================================
# TITLE
# ==========================================

st.title("🎯 AI Interview Prep Assistant")

st.write(
    "Upload your resume and prepare for interviews using AI."
)

# ==========================================
# ROLE INPUT
# ==========================================

role = st.text_input(
    "Target Role",
    placeholder="Example: Data Analyst"
)

# ==========================================
# FILE UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ==========================================
# MAIN PROCESS
# ==========================================

if uploaded_file and role:

    with st.spinner("Analyzing Resume..."):

        resume_text = extract_text(uploaded_file)

    st.success("Resume Uploaded Successfully!")

    # ======================================
    # INTERVIEW QUESTIONS SECTION
    # ======================================

    st.header("📋 Interview Questions & Sample Answers")

    with st.spinner("Generating Questions..."):

        interview_content = generate_questions(
            resume_text,
            role
        )

    st.markdown(interview_content)

    st.divider()

    # ======================================
    # MOCK INTERVIEW SECTION
    # ======================================

    st.header("🎤 Mock Interview")

    st.write(
        "Answer the following questions and get instant AI feedback."
    )

    mock_questions = generate_mock_questions(
        resume_text,
        role
    )

    answers = {}

    for i, question in enumerate(mock_questions):

        st.subheader(f"Question {i+1}")

        st.write(question)

        answers[question] = st.text_area(
            "Your Answer",
            height=120,
            key=f"answer_{i}"
        )

    # ======================================
    # EVALUATION BUTTON
    # ======================================

    if st.button("Evaluate My Interview"):

        st.header("📊 Interview Evaluation")

        for question, answer in answers.items():

            if answer.strip():

                with st.spinner("Evaluating Answer..."):

                    feedback = evaluate_answer(
                        question,
                        answer
                    )

                st.markdown("---")

                st.subheader("Question")

                st.write(question)

                st.subheader("Feedback")

                st.markdown(feedback)

            else:

                st.warning(
                    f"Please answer the question:\n\n{question}"
                )

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Built using Streamlit + Gemini API"
)