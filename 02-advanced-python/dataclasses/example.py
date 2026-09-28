from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Ticket:
    id: int
    title: str
    priority: str = "P4"
    tags: list[str] = field(default_factory=list)
    created: datetime = field(default_factory=datetime.now)

t = Ticket(1, "VPN down", "P1", ["network"])
print(t)
