# RAG flow

```
Upload document -> split into chunks -> create embeddings -> store in pgvector
User question   -> embed question -> top-k similar chunks
                -> send chunks + question to the LLM -> answer with sources
```

## Safety checklist
- Treat retrieved text as data, not instructions (prompt injection)
- Mask PII before sending to a third-party model
- Log token usage and cost per request
- Keep a fixed evaluation set of 20 questions and re-run after every prompt change
