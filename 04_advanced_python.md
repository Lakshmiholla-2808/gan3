# 04 --- Advanced Python

# Decorators

A decorator is a callable that modifies or extends the behavior of
another callable.

Basic example:

``` python
def logger(func):
    def wrapper():
        print("Before function")
        result = func()
        print("After function")
        return result

    return wrapper


@logger
def greet():
    print("Hello")


greet()
```

The decorator syntax:

``` python
@logger
def greet():
    ...
```

is conceptually equivalent to:

``` python
def greet():
    ...

greet = logger(greet)
```

## Real-world uses

Decorators are commonly useful for cross-cutting behavior such as:

-   logging
-   timing
-   authorization checks
-   caching
-   instrumentation

Trainer challenge:

Modify the decorator to accept `*args` and `**kwargs`.

------------------------------------------------------------------------

# Context managers

A context manager controls setup and cleanup around a block of code.

``` python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

The `with` statement helps ensure the resource is properly managed.

## Custom context manager

``` python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Acquire")
    try:
        yield
    finally:
        print("Release")

with managed_resource():
    print("Work")
```

### Real-world examples

-   files
-   locks
-   database transactions
-   temporary resources
-   connections

------------------------------------------------------------------------

# Dataclasses

Dataclasses reduce boilerplate for classes primarily used to hold data.

``` python
from dataclasses import dataclass

@dataclass
class Employee:
    id: int
    name: str
    department: str
```

Use:

``` python
employee = Employee(101, "Asha", "Engineering")
print(employee)
```

Trainer question:

When is a dataclass useful compared with a normal class?

Answer: when the main purpose is representing structured data and you
want generated methods such as an initializer and representation with
minimal boilerplate.

------------------------------------------------------------------------

# Type hints

``` python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

Type hints improve readability, tooling and static analysis.

Important:

> Type hints do not by themselves make ordinary Python function
> arguments runtime-enforced.

For runtime validation in application frameworks, separate validation
mechanisms may be used.

------------------------------------------------------------------------

# Logging

Avoid using `print()` as the application's logging system.

``` python
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("Unexpected input")
```

Typical levels:

``` text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

### Real-world example

If a production API becomes slow, logs can help establish:

-   which endpoint was called
-   which operation failed
-   what happened before the failure
-   correlation/request information when the application provides it

Logging should not expose passwords, tokens or other sensitive
information.

------------------------------------------------------------------------

# Modules, packages and dependencies

A production project should organize code rather than putting everything
into one Python file.

Example:

``` text
app/
├── main.py
├── services/
├── repositories/
├── models/
├── schemas/
└── utils/
```

Trainer question:

Why separate services and repositories?

A common reason is separation of concerns: business logic and
data-access logic can evolve and be tested independently.

------------------------------------------------------------------------

# Production exercise

Build a small employee service with:

-   dataclass
-   type hints
-   logging
-   custom exception
-   service function
-   repository-like function
-   unit tests
