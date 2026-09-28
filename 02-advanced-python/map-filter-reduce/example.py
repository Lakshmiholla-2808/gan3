from functools import reduce
invoices = [{"amt": 100, "paid": True}, {"amt": 250, "paid": False}, {"amt": 75, "paid": True}]
paid = filter(lambda i: i["paid"], invoices)
amounts = map(lambda i: i["amt"], paid)
print(reduce(lambda a, b: a + b, amounts, 0))
