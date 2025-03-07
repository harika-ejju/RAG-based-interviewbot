import requests
import json

# Gemini API configurations
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
GEMINI_API_KEY = "AIzaSyDPFOSdoAXf6FFkFQag9xywTwtYu2apImM"  # Replace with your actual Gemini API key

import fitz  # PyaMuPDF for extracting text from PDFs

def load_resume(uploaded_file):
    """
    Loads and extracts text from a PDF resume.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    resume_text = ""
    for page in doc:
        resume_text += page.get_text()
    return resume_text


def generate_interview_questions(resume_text):
    """
    Generates interview questions based on the provided resume text using Gemini's API.
    """
    template = """
    Based on the following resume, generate 5 relevant interview questions:
    
    Resume: {resume_text}
    """

    # Prepare the payload for the API request with a simplified text
    simplified_text = "John Doe is an experienced software engineer with 5 years of experience in full-stack development. He has expertise in Python, JavaScript, and React."

    payload = {
        "contents": [{
            "parts": [{"text": template.format(resume_text=simplified_text)}]
        }]
    }

    headers = {
        "Content-Type": "application/json"
    }

    # Send the POST request to Gemini API
    try:
        # Log the payload for debugging
        print("Payload:", json.dumps(payload, indent=4))

        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            data=json.dumps(payload)
        )

        # Log the response status code and the full response text
        print("Response Status Code:", response.status_code)
        print("Response Text:", response.text)  # Log the full response

        if response.status_code == 200:
            # Parse the response and return the generated content
            data = response.json()

            # Check if content exists in the response
            if 'content' in data:
                return data['content']
            else:
                return "No content generated in the response."

        else:
            # Handle errors if the response is not successful
            return f"Error {response.status_code}: {response.text}"

    except Exception as e:
        # Handle any exceptions during the request
        return f"An error occurred: {str(e)}"
