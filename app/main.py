import streamlit as st
from app.utils import load_resume, generate_interview_questions

# Set up Streamlit UI
st.title("AI-Based Interview Bot")
st.write("Upload your resume to generate interview questions.")

# File uploader widget for resume upload
uploaded_file = st.file_uploader("Choose a file", type="pdf")
if uploaded_file is not None:
    # Load and display resume content (showing a snippet here for brevity)
    resume_text = load_resume(uploaded_file)
    st.subheader("Resume Text:")
    st.write(resume_text[:500])  # Display first 500 characters for quick preview

    # Button to generate interview questions
    if st.button("Generate Interview Questions"):
        with st.spinner('Generating interview questions...'):
            interview_questions = generate_interview_questions(resume_text)
            st.subheader("Generated Interview Questions:")
            st.write(interview_questions)
