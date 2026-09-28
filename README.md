# Python Full-Stack Trainer

Corporate training curriculum: Python fundamentals to AI-powered full-stack applications.
16 weeks, 80 sessions of about 3 hours. One running case study: **Acme Support Desk**.

## Curriculum
| # | Module | Days | Folder |
|---|---|---|---|
| 01 | Python Fundamentals | 10 | [01-python-fundamentals](01-python-fundamentals) |
| 02 | Advanced Python | 10 | [02-advanced-python](02-advanced-python) |
| 03 | Software Engineering | 5 | [03-software-engineering](03-software-engineering) |
| 04 | SQL | 5 | [04-sql](04-sql) |
| 05 | FastAPI | 7 | [05-fastapi](05-fastapi) |
| 06 | PostgreSQL | 5 | [06-postgresql](06-postgresql) |
| 07 | HTML, CSS, JavaScript | 8 | [07-html-css-javascript](07-html-css-javascript) |
| 08 | React | 8 | [08-react](08-react) |
| 09 | Full-Stack Projects | 8 | [09-fullstack-projects](09-fullstack-projects) |
| 10 | AI-Assisted Development | 4 | [10-ai-assisted-development](10-ai-assisted-development) |
| 11 | AI Full-Stack Projects | 10 | [11-ai-fullstack-projects](11-ai-fullstack-projects) |

Recommended teaching order: 04 SQL, 06 PostgreSQL, then 05 FastAPI, so the API uses a real database from day one.

## Topic folder layout (modules 01 to 03)
```
topic/
  README.md     objectives, real-time example, lab
  example.py    runnable trainer demo
  exercise.py   starter file for learners
```

## Setup
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python 01-python-fundamentals/01-variables/example.py
```

More: [docs/training-flow.md](docs/training-flow.md), [docs/assessment.md](docs/assessment.md)
