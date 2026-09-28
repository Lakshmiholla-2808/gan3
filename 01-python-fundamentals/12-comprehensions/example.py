tickets = [
    {"id": 1, "status": "open", "hours": 3},
    {"id": 2, "status": "closed", "hours": 9},
    {"id": 3, "status": "open", "hours": 5},
]
open_ids = [t["id"] for t in tickets if t["status"] == "open"]
by_id = {t["id"]: t["hours"] for t in tickets}
statuses = {t["status"] for t in tickets}
print(open_ids, by_id, statuses)
