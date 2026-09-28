# PostgreSQL (5 days)

| Day | Topics |
|---|---|
| 1 | Install, psql, roles, databases |
| 2 | Types (UUID, JSONB, TIMESTAMPTZ), constraints, foreign keys |
| 3 | Indexes, EXPLAIN ANALYZE, tuning |
| 4 | Views, CTEs, window functions, full-text search |
| 5 | SQLAlchemy, Alembic migrations, backups |

## Start a database
```bash
docker compose up -d
psql postgresql://app:secret@localhost:5432/acme -f init.sql
python db.py
```

Always use parameterized queries. Explain SQL injection with a live demo.
