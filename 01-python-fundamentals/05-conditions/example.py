def priority(text):
    text = text.lower()
    if "down" in text or "outage" in text:
        return "P1"
    elif "password" in text:
        return "P3"
    return "P4"

for t in ["Server is down", "Password reset", "New mouse"]:
    print(t, "->", priority(t))

status = 404
match status:
    case 200: print("ok")
    case 404: print("not found")
    case _: print("other")
