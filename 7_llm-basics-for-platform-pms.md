# OpenAI API Basics

## What is an LLM

Large Language Models (LLMs) predict the next token based on previous tokens. They are not databases and they do not "know" facts in the traditional sense. Because of this, the same prompt can sometimes generate slightly different responses.

## Tokens

Models process text as tokens rather than words. Cost is usually based on input and output tokens. More text means more tokens and therefore higher cost.

## Structured Outputs

Instead of free text, models can return structured data such as JSON. This is useful when building applications because the output becomes predictable and easier to process.

## Context Window and Cost

Models can only process a limited amount of text at once. The prompt, conversation history and response all count towards this limit. Cost depends mainly on model choice and input/output size. Larger models and longer prompts usually cost more.

## Model Parameters

Some common parameters are Temperature & Max output tokens. 

Temperature controls how creative or deterministic the response is. Lower values are usually better for business applications.

Max output tokens limits the size of AI response. 

## Example API Call

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY_HERE" \
  -d '{
    "model": "gpt-5",
    "input": "Analyze this API error log and provide root cause, severity and recommendation: HTTP 429 Too Many Requests"
  }'
```
