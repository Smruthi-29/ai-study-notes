import streamlit as st

# Set the title of the web app
st.title("Welcome to My Streamlit App")

# Add a text input box
user_input = st.text_input("Enter something:")

# Add a button
if st.button("Submit"):
    st.write(f"You entered: {user_input}")

# Display an image (optional, if you have an image file)
# st.image("example.jpg", caption="Example Image")

# Add a sidebar
st.sidebar.header("Sidebar")
st.sidebar.write("This is a simple sidebar!")

# Add a checkbox
tagline = st.checkbox("Show tagline")
if tagline:
    st.write("Streamlit makes app development easy!")

import streamlit as st
import openai
import pdfplumber

# Load OpenAI API Key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit UI
st.title("📖 AI-Powered Study Notes Generator")

# File Upload
uploaded_file = st.file_uploader("Upload your study material (PDF)", type=["pdf"])

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    
    # Display extracted text (optional)
    st.subheader("Extracted Text")
    st.text_area("Text Preview", text[:1000], height=250)

    # Generate Study Notes
    if st.button("Generate Notes"):
        with st.spinner("Generating AI-powered study notes..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": f"Summarize this text into key study notes:\n\n{text}"}]
            )
            notes = response["choices"][0]["message"]["content"]
            st.subheader("📌 AI-Generated Study Notes")
            st.write(notes)

