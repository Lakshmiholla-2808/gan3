ticket = {"id": 7, "title": "VPN down", "user": {"name": "Asha"}}
print(ticket["user"]["name"], ticket.get("priority", "P4"))

counts = {}
for word in "vpn down vpn slow vpn".split():
    counts[word] = counts.get(word, 0) + 1
print(counts)
for k, v in counts.items():
    print(k, v)
