raw = ["1200", "35.5", "true"]
qty = int(raw[0])
price = float(raw[1])
flag = raw[2].lower() == "true"
print(type(qty), type(price), type(flag), qty * price)
print(type(None), bool(0), bool("text"))
