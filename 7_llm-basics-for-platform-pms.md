# OpenAI API Basics

## What is an LLM

Large Language Models predict the next token based on previous tokens. They are not databases and can generate different responses for the same prompt.

## Tokens

Models process text as tokens, not words.

Cost is usually based on:

* Input tokens
* Output tokens

## Prompts

Prompts are instructions given to the model.

Good prompts usually provide:

* Context
* Task
* Expected output format

## Structured Outputs

Instead of free text, models can return structured responses such as JSON.

This is useful for applications that need predictable outputs.

## Cost Considerations

Cost depends on:

* Model choice
* Input size
* Output size
* Number of requests

## Example Use Case

Analyze API logs and return:

* Root Cause
* Severity
* Recommended Fix
