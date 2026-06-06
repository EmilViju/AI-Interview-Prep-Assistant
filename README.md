# 🎯 AI Interview Prep Assistant

## Overview

AI Interview Prep Assistant is an AI-powered web application that helps students and job seekers prepare for interviews using their resumes.

The application analyzes a user's resume, generates personalized interview questions, provides sample answers, conducts a mock interview, and evaluates the user's responses using Google's Gemini AI.

---

## Features

✅ Resume Upload (PDF)

✅ Resume-Based Interview Questions

✅ HR Questions with Sample Answers

✅ Technical Questions with Sample Answers

✅ Project-Based Questions with Sample Answers

✅ Personalized Mock Interview

✅ AI-Powered Answer Evaluation

✅ Interview Feedback with Scores, Strengths, and Improvements

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini API

### Libraries

* google-generativeai
* PyPDF2
* Streamlit

---

## Project Workflow

1. User uploads a resume (PDF).
2. Resume text is extracted.
3. Gemini AI analyzes the resume.
4. Interview questions and sample answers are generated.
5. A mock interview is conducted.
6. User submits answers.
7. Gemini AI evaluates responses and provides feedback.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Interview-Prep-Assistant.git
```

Move into the project directory:

```bash
cd AI-Interview-Prep-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a Streamlit secrets file:

```text
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Run the application:

```bash
streamlit run app.py
```

---

## Project Structure

```text
AI-Interview-Prep-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

---

## Future Improvements

* Resume Scoring System
* Skill Gap Analysis
* PDF Interview Report Generation
* Voice-Based Mock Interview
* Interview Performance Dashboard
* Multi-Role Interview Preparation

---

## Author

Emil Viju

Aspiring AI/ML Engineer | Data Analyst Enthusiast

---

## License

This project is developed for educational and portfolio purposes.
