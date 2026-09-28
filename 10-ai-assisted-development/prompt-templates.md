# Prompt templates

## Feature
```
Role: Senior Python developer.
Context: FastAPI app, SQLAlchemy 2.0, PostgreSQL.
Task: Add an endpoint to close a ticket and record who closed it.
Constraints: dependency injection, Pydantic v2, 404 if missing, no raw SQL.
Output: router code + one pytest test. Explain trade-offs briefly.
```

## Debug
```
Here is the traceback and the function. Explain the root cause first,
then propose the smallest fix and a test that fails before the fix.
```

## Refactor
```
Refactor for readability without changing behaviour. Keep public
function names. List every change you made.
```

## Review
```
Review this diff for bugs, security issues and missing tests. Rank by severity.
```
