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

Analyze API logs and return root cause, severity & recommended fix.

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY_HERE" \
  -d '{
    "model": "gpt-5",
    "input": "Analyze this API error log and provide root cause, severity and recommendation: HTTP 429 Too Many Requests"
  }'
```
