cart = ["book"]
alias = cart
alias.append("pen")
print(cart, cart is alias)
copy = cart[:]
print(copy == cart, copy is cart)
