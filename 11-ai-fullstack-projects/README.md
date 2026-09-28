# AI Full-Stack Projects (10 days)

| Topic | Days |
|---|---|
| LLM API basics: messages, system prompts, tokens, cost | 1 |
| Structured output with Pydantic validation | 1 |
| Prompt design in code: templates, few-shot, guardrails | 1 |
| Embeddings and RAG with pgvector | 2 |
| Streaming responses (SSE) to React | 1 |
| Evaluation and safety: test sets, prompt injection, PII | 1 |
| Capstone | 3 |

## Capstone options
| Project | AI feature |
|---|---|
| A. Smart Support Desk | Auto-categorize tickets, suggest replies, summarize threads |
| B. Company Knowledge Chatbot | RAG over policy PDFs with sources |
| C. Resume Screener | Extract skills to JSON and rank against a job description |
| D. Meeting Notes Assistant | Transcript to summary and action items |

## Rubric (100)
Working AI feature 25, full-stack integration 20, prompt and output validation 15, evaluation and safety 15, code quality and tests 15, demo 10.

## Run the starter
`triage.py` uses a fake LLM so it runs with no API key. Replace `fake_llm` with your provider's client.
```bash
python triage.py
```
