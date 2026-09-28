hours, rate = 52, 300
overtime = max(hours - 40, 0)
pay = min(hours, 40) * rate + overtime * rate * 1.5
print(pay, pay > 15000 and overtime > 0, 7 // 2, 7 % 2, 2 ** 5)
print("P1" in ["P1", "P2"], [] is [])
