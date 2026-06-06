import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Smart API Assistant")

uploaded_file = st.file_uploader(
    "Upload log file",
    type=["txt", "log"]
)

if uploaded_file:
    log_content = uploaded_file.read().decode("utf-8")

    st.subheader("Uploaded Log")
    st.text_area("", log_content, height=200)

    if st.button("Analyze"):

        prompt = f"""
        You are an API operations assistant.

        Analyze the following logs and provide:

        1. Severity
        2. Likely Root Cause
        3. Affected Services or Endpoints
        4. Recommended Actions

        Logs:

        {log_content}
        """

        response = client.responses.create(
            model="gpt-4.1",
            input=prompt
        )

        st.subheader("Analysis")
        st.write(response.output_text)
