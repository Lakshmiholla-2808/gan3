# 02 --- Collections, Functions and Pythonic Patterns

# List vs Tuple

## Simple explanation

Both are ordered collections.

``` python
items = [10, 20, 30]
coordinates = (10, 20)
```

A list is mutable:

``` python
items[0] = 99
```

A tuple is immutable:

``` python
# coordinates[0] = 99  # TypeError
```

## Interview answer

The choice should depend on whether the collection needs to change and
on the semantic meaning of the data. A tuple can communicate that the
collection is intended to remain fixed.

------------------------------------------------------------------------

# List vs Set

List:

-   ordered sequence
-   allows duplicates
-   indexable

Set:

-   unique elements
-   optimized for membership operations
-   not a sequence you should rely on for positional access

Example:

``` python
emails = ["a@example.com", "a@example.com", "b@example.com"]
unique_emails = set(emails)
```

------------------------------------------------------------------------

# Dictionary vs List

Use a list when position/sequence matters.

Use a dictionary when you need key-value lookup.

``` python
users = ["Asha", "Ravi"]

user = {
    "id": 101,
    "name": "Asha"
}
```

------------------------------------------------------------------------

# \*args

`*args` collects additional positional arguments.

``` python
def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30))
```

The parameter `numbers` is a tuple.

------------------------------------------------------------------------

# \*\*kwargs

`**kwargs` collects additional keyword arguments.

``` python
def show_user(**details):
    print(details)

show_user(name="Asha", role="Developer")
```

`details` is a dictionary.

------------------------------------------------------------------------

# Lambda

A lambda is a small anonymous function.

``` python
square = lambda x: x * x

print(square(5))
```

Use it when a small function is useful locally, especially with
functions such as `sorted`.

``` python
employees = [
    {"name": "A", "salary": 50000},
    {"name": "B", "salary": 70000},
]

result = sorted(employees, key=lambda e: e["salary"])
```

------------------------------------------------------------------------

# map()

Transforms values.

``` python
numbers = [1, 2, 3]

squares = list(map(lambda x: x * x, numbers))
```

Modern Python code may often use a comprehension when it is clearer:

``` python
squares = [x * x for x in numbers]
```

------------------------------------------------------------------------

# filter()

Keeps values satisfying a condition.

``` python
numbers = [1, 2, 3, 4, 5]

even = list(filter(lambda x: x % 2 == 0, numbers))
```

Equivalent readable comprehension:

``` python
even = [x for x in numbers if x % 2 == 0]
```

------------------------------------------------------------------------

# reduce()

`reduce` repeatedly combines values into one result.

``` python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)
```

Trainer point: don't use `reduce` just because you can. Prefer clear
built-ins such as `sum()` when they express the intent better.

------------------------------------------------------------------------

# zip()

Combines elements from iterables.

``` python
names = ["Asha", "Ravi", "John"]
scores = [80, 90, 85]

for name, score in zip(names, scores):
    print(name, score)
```

Real-world use: combining parallel datasets or columns.

------------------------------------------------------------------------

# enumerate()

Adds an index while iterating.

``` python
names = ["Asha", "Ravi"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

------------------------------------------------------------------------

# Iterables and iterators

An iterable is something you can iterate over.

An iterator produces values one at a time using `__next__()` and
remembers its iteration state.

``` python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

Eventually `next()` raises `StopIteration`.

------------------------------------------------------------------------

# Generator

A generator is a convenient way to create an iterator using `yield`.

``` python
def numbers():
    for i in range(5):
        yield i

for number in numbers():
    print(number)
```

## Generator vs list

List:

``` python
values = [x * x for x in range(1000000)]
```

Generator:

``` python
values = (x * x for x in range(1000000))
```

A generator produces values lazily instead of constructing the entire
result collection at once.

### Real-world example

Processing a large file line by line:

``` python
def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line
```

This is useful when you do not want to load the entire file into memory.

------------------------------------------------------------------------

# Practice exercises

1.  Find duplicate values in a list.
2.  Convert two lists into a dictionary.
3.  Count word frequency using a dictionary.
4.  Find employees with salary above a threshold.
5.  Create a generator for batches of records.
6.  Use `enumerate()` to display ranked results.
7.  Use `zip()` to combine employee names and departments.
8.  Rewrite simple `map()` and `filter()` examples using comprehensions.
