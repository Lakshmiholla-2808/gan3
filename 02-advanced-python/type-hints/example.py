def find_user(users: dict[int, str], uid: int) -> str | None:
    return users.get(uid)

def total(prices: list[float], tax: float = 0.18) -> float:
    return round(sum(prices) * (1 + tax), 2)

print(find_user({1: "Asha"}, 2), total([100.0, 50.0]))
