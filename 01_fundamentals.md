# 01 --- Python Fundamentals

## 1. Variables and dynamic typing

### Explain to a fresher

A variable is a name that refers to a value.

``` python
name = "Anu"
age = 21
```

Python determines the type of the value at runtime.

``` python
x = 10
print(type(x))

x = "hello"
print(type(x))
```

This is called dynamic typing.

### Real-world example

An employee record can contain different kinds of values:

``` python
employee_name = "Rahul"
employee_id = 101
salary = 45000.50
is_active = True
```

### Trainer point

Do not say that Python variables are boxes that permanently contain a
type. A Python name refers to an object, and the object has a type.

------------------------------------------------------------------------

# 2. Built-in data types

Important built-in types include:

``` text
int
float
complex
bool
str
list
tuple
set
dict
NoneType
```

Example:

``` python
age = 25
price = 99.5
name = "Priya"
skills = ["Python", "SQL"]
coordinates = (12.9, 77.6)
unique_ids = {101, 102, 103}
employee = {"id": 101, "name": "Priya"}
active = True
result = None
```

### Interview explanation

A data type determines the kind of object and the operations supported
by that object.

------------------------------------------------------------------------

# 3. Operators

``` python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Comparison:

``` python
print(a > b)
print(a == b)
print(a != b)
```

Logical:

``` python
age = 25
has_id = True

print(age >= 18 and has_id)
```

------------------------------------------------------------------------

# 4. Strings

``` python
name = "Python"

print(name[0])
print(name[-1])
print(name[0:3])
print(name.upper())
print(name.lower())
print(name.replace("P", "J"))
```

### Real-world example

``` python
first_name = "Anu"
last_name = "Sharma"

full_name = f"{first_name} {last_name}"
```

------------------------------------------------------------------------

# 5. Conditions

``` python
marks = 82

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
else:
    grade = "C"

print(grade)
```

### Corporate example

``` python
amount = 120000

if amount > 100000:
    approval = "Manager approval required"
else:
    approval = "Automatic approval"
```

The point is not the exact business rule; it is learning how application
logic is expressed.

------------------------------------------------------------------------

# 6. Loops

``` python
for i in range(5):
    print(i)
```

``` python
employees = ["Asha", "Ravi", "John"]

for employee in employees:
    print(employee)
```

While loop:

``` python
attempts = 0

while attempts < 3:
    print("Trying...")
    attempts += 1
```

### Trainer question

When would you use `for` instead of `while`?

A useful answer: use `for` when iterating over a known iterable; use
`while` when repetition is controlled by a condition.

------------------------------------------------------------------------

# 7. Lists

Lists are ordered, mutable collections.

``` python
skills = ["Python", "SQL", "Git"]

skills.append("FastAPI")
skills.remove("Git")

print(skills)
```

Indexing:

``` python
print(skills[0])
print(skills[-1])
```

------------------------------------------------------------------------

# 8. Tuples

Tuples are ordered and immutable.

``` python
point = (10, 20)

print(point[0])
```

A common use is representing a fixed collection of values.

------------------------------------------------------------------------

# 9. Sets

Sets contain unique elements.

``` python
skills = {"Python", "SQL", "Python"}

print(skills)
```

Useful for membership tests and removing duplicates.

------------------------------------------------------------------------

# 10. Dictionaries

Dictionaries store key-value mappings.

``` python
employee = {
    "id": 101,
    "name": "Anu",
    "department": "Engineering"
}

print(employee["name"])
```

Safer lookup:

``` python
print(employee.get("email"))
```

### Real-world example

JSON-like API data is commonly represented by dictionaries in Python.

------------------------------------------------------------------------

# 11. Slicing

Syntax:

``` text
sequence[start:stop:step]
```

Example:

``` python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])
print(numbers[::-1])
```

Important: the `stop` position is excluded.

------------------------------------------------------------------------

# 12. Comprehensions

List comprehension:

``` python
squares = [x * x for x in range(5)]
```

With condition:

``` python
even_numbers = [x for x in range(10) if x % 2 == 0]
```

Dictionary comprehension:

``` python
squares = {x: x * x for x in range(5)}
```

### Trainer caution

Comprehensions improve concise transformations, but extremely complex
comprehensions can reduce readability.

------------------------------------------------------------------------

# 13. Functions

``` python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(100, 3)
print(total)
```

Explain:

-   function name
-   parameters
-   arguments
-   return value
-   local variables

------------------------------------------------------------------------

# 14. Exception handling

``` python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid number.")
```

With `else` and `finally`:

``` python
try:
    value = int("10")
except ValueError:
    print("Invalid")
else:
    print("Conversion successful")
finally:
    print("This block runs after the operation")
```

### Corporate example

An API may receive invalid input. The application should handle expected
failures rather than crashing unexpectedly.

------------------------------------------------------------------------

# 15. Modules and packages

A module is a Python file that can contain reusable code.

``` python
# math_utils.py

def add(a, b):
    return a + b
```

Use it:

``` python
from math_utils import add

print(add(2, 3))
```

A package organizes related modules.

------------------------------------------------------------------------

# 16. Virtual environments

Create:

``` bash
python -m venv .venv
```

Activate it according to your operating system.

Then install packages:

``` bash
python -m pip install requests
```

Why?

Different projects may require different dependency versions.

------------------------------------------------------------------------

# 17. pip

Check:

``` bash
python -m pip --version
```

Install:

``` bash
python -m pip install requests
```

Freeze dependencies:

``` bash
python -m pip freeze > requirements.txt
```

Install from requirements:

``` bash
python -m pip install -r requirements.txt
```

### Corporate explanation

A project should not depend on whatever packages happen to be installed
globally on a developer's machine. Isolated environments and explicit
dependencies make projects more reproducible.
