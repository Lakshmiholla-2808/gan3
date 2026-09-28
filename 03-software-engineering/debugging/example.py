def discount(price, percent):
    # BUG: percent is treated as a fraction; find and fix it
    return price - price * percent / 10

print(discount(200, 10))   # expected 180
