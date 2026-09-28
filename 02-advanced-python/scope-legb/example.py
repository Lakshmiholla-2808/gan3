def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

hits = make_counter()
print(hits(), hits(), hits())
