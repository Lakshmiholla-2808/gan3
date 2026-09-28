attempts = 0
while attempts < 3:
    attempts += 1
    print("attempt", attempts)
    if attempts == 2:
        print("success")
        break

for i, order in enumerate(["A101", "A102", "A103"], start=1):
    print(i, order)
