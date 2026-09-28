from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Acme Support Desk")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

TICKETS: dict[int, dict] = {}


class TicketIn(BaseModel):
    title: str
    priority: str = "P4"


@app.post("/tickets", status_code=201)
def create_ticket(data: TicketIn):
    tid = len(TICKETS) + 1
    TICKETS[tid] = {"id": tid, **data.model_dump(), "status": "open"}
    return TICKETS[tid]


@app.get("/tickets")
def list_tickets(status: str | None = None):
    items = list(TICKETS.values())
    return [t for t in items if status is None or t["status"] == status]


@app.get("/tickets/{ticket_id}")
def read_ticket(ticket_id: int):
    if ticket_id not in TICKETS:
        raise HTTPException(404, "Ticket not found")
    return TICKETS[ticket_id]


@app.patch("/tickets/{ticket_id}/close")
def close_ticket(ticket_id: int):
    ticket = read_ticket(ticket_id)
    ticket["status"] = "closed"
    return ticket
