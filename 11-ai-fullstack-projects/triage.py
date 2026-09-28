"""Ticket triage with structured, validated LLM output."""
import json
from dataclasses import dataclass

CATEGORIES = {"billing", "bug", "access", "other"}


@dataclass
class Triage:
    category: str
    priority: str
    summary: str


def fake_llm(prompt: str) -> str:
    """Stand-in for a real LLM call. Replace with your provider's API client."""
    text = prompt.lower()
    category = "access" if "password" in text else "bug" if "error" in text else "other"
    priority = "P1" if "down" in text else "P3"
    return json.dumps({"category": category, "priority": priority,
                       "summary": prompt.split("Ticket:")[-1].strip()[:60]})


def triage(ticket_text: str, llm=fake_llm) -> Triage:
    prompt = ("Classify this support ticket. Return JSON with category "
              "(billing|bug|access|other), priority (P1-P4), summary.\n"
              f"Ticket: {ticket_text}")
    data = json.loads(llm(prompt))
    if data["category"] not in CATEGORIES:        # never trust model output blindly
        data["category"] = "other"
    return Triage(**data)


if __name__ == "__main__":
    for t in ["Production site is down with error 500", "I forgot my password"]:
        print(triage(t))
