emps = [("Ravi", 50), ("Asha", 50), ("Meena", 40)]
print(sorted(emps, key=lambda e: (-e[1], e[0])))
