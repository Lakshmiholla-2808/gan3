from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg://app:secret@localhost:5432/acme")

with engine.connect() as conn:
    rows = conn.execute(text("SELECT id, title FROM tickets WHERE status = :s"),
                        {"s": "open"})
    for row in rows:
        print(row)
