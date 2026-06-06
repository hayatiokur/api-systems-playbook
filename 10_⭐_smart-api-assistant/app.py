import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Smart API Assistant")

log_type = st.selectbox(
    "Log Format",
    [
        "Auto Detect",
        "Apache",
        "Nginx",
        "Kong",
        "AWS API Gateway"
    ]
)

log_file = st.file_uploader(
    "Upload Logs",
    type=["txt", "log"]
)

metrics_file = st.file_uploader(
    "Upload Metrics",
    type=["csv", "txt"]
)

trace_file = st.file_uploader(
    "Upload Traces",
    type=["json", "txt"]
)

if st.button("Analyze"):

    logs = ""
    metrics = ""
    traces = ""

    if log_file:
        logs = log_file.read().decode("utf-8")

    if metrics_file:
        metrics = metrics_file.read().decode("utf-8")

    if trace_file:
        traces = trace_file.read().decode("utf-8")

    prompt = f"""
You are a senior API platform engineer and observability expert.

Supported log platforms:
- Apache
- Nginx
- Kong
- AWS API Gateway

Selected Log Source:
{log_type}

Analyze all available data sources.

=== LOGS ===
{logs}

=== METRICS ===
{metrics}

=== TRACES ===
{traces}

Generate a complete Incident Report.

Structure:

# Executive Summary

Short summary of the incident.

# Severity

Low / Medium / High / Critical

# Root Cause

Most likely root cause.

# Impact Assessment

What users or systems were affected?

# Affected Services or Endpoints

List affected services.

# Evidence

Correlate logs, metrics and traces.

Explain why you reached the conclusion.

# Recommended Actions

Immediate actions.

# Next Steps

Longer term improvements.

# Platform Detection

If Auto Detect is selected, determine the most likely platform from log patterns.

Be concise and practical.
"""

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    report = response.output_text

    st.subheader("Incident Report")
    st.markdown(report)

    st.download_button(
        label="Download Incident Report",
        data=report,
        file_name="incident_report.md",
        mime="text/markdown"
    )
