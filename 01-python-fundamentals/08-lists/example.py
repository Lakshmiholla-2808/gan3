queue = [("P3", "Password reset"), ("P1", "Server down")]
queue.append(("P2", "VPN slow"))
queue.sort()
print(queue)
print(queue.pop(0))
print(queue[-1], len(queue))
