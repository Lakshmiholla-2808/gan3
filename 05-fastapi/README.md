# FastAPI (7 days)

| Day | Topics |
|---|---|
| 1 | REST basics, first endpoint, Swagger UI |
| 2 | Path/query params, Pydantic validation |
| 3 | SQLAlchemy CRUD, dependency injection |
| 4 | Auth: password hashing, JWT, roles |
| 5 | Errors, middleware, CORS, pagination |
| 6 | Testing with TestClient, Alembic |
| 7 | Docker, deployment, docs |

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://localhost:8000/docs

## Test
```bash
pytest
```
`app/main.py` uses in-memory storage so learners can start instantly. In Day 3 they replace it with PostgreSQL (see Module 06).
