def sla_hours(priority: str = "P4") -> int:
    """Return SLA hours for a ticket priority."""
    return {"P1": 4, "P2": 8, "P3": 24}.get(priority, 72)

print(sla_hours("P1"), sla_hours("P3"), sla_hours())
