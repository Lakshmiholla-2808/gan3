# 03 --- Python Internals for Developer and Trainer Interviews

# Mutable vs immutable

Mutable objects can be changed after creation.

Examples include lists and dictionaries.

``` python
items = [1, 2, 3]
items.append(4)
```

Immutable objects cannot be changed in place.

Examples include integers, strings and tuples.

``` python
name = "Python"
# name[0] = "J"  # TypeError
```

Important nuance: a variable can be rebound even when the object itself
is immutable.

``` python
x = 10
x = 20
```

The integer object was not changed; the name `x` was rebound.

------------------------------------------------------------------------

# is vs ==

`==` compares values for equality.

`is` tests object identity.

``` python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

Use `is` for identity checks.

A classic example:

``` python
value = None

if value is None:
    print("No value")
```

------------------------------------------------------------------------

# References

Python names refer to objects.

``` python
a = [1, 2]
b = a

b.append(3)

print(a)
print(b)
```

Both names refer to the same list.

Trainer question:

Why did changing `b` also affect `a`?

Because `a` and `b` refer to the same mutable object.

------------------------------------------------------------------------

# Shallow copy vs deep copy

Shallow copy creates a new outer object but nested objects may still be
shared.

``` python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0].append(99)

print(original)
```

Deep copy recursively copies nested objects.

``` python
deep = copy.deepcopy(original)
```

### Real-world example

Consider an application configuration containing nested dictionaries and
lists. A shallow copy may accidentally share nested mutable data.

------------------------------------------------------------------------

# Scope

A variable's scope describes where it can be accessed.

``` python
x = "global"

def demo():
    x = "local"
    print(x)

demo()
print(x)
```

------------------------------------------------------------------------

# LEGB

Python resolves names using:

``` text
L — Local
E — Enclosing
G — Global
B — Built-in
```

Example:

``` python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()
```

Trainer challenge:

Explain what changes when `global` or `nonlocal` is used.

------------------------------------------------------------------------

# Function arguments

Python passes object references through function calls. A useful
trainer-level explanation is:

> The function receives a reference to an object; whether the caller
> appears to be affected depends on whether the object is mutated or the
> local name is rebound.

Example:

``` python
def add_item(items):
    items.append("Python")

values = []
add_item(values)

print(values)
```

The list was mutated.

Compare:

``` python
def replace(items):
    items = ["new"]

values = ["old"]
replace(values)

print(values)
```

The local name was rebound; the caller's list was not replaced.

------------------------------------------------------------------------

# Garbage collection and memory management

At trainer level, distinguish:

1.  Python object model
2.  Reference counting in CPython
3.  Cyclic garbage collection
4.  Memory allocation/deallocation

Do not teach "Python immediately deletes every object when its reference
count becomes zero" as a universal statement. That is too simplistic.

In CPython, reference counting is an important mechanism, and cyclic
garbage collection handles reference cycles that reference counting
alone cannot resolve.

------------------------------------------------------------------------

# GIL

The Global Interpreter Lock is a CPython implementation mechanism that
affects execution of Python bytecode by threads.

Trainer-level explanation:

> Threads can still be useful for I/O-bound work, but CPU-bound Python
> code does not generally gain parallel execution of Python bytecode
> from ordinary threads in a standard CPython process because of the
> GIL.

Do not say "Python cannot do multithreading." It can.

Also avoid treating the GIL as a universal property of every Python
implementation.

------------------------------------------------------------------------

# Interview drill

Explain each in three levels:

### Fresher

"What is `is` versus `==`?"

### Developer

"Why can two lists be equal but not identical?"

### Experienced developer

"Where can identity checks matter, and why is `is None` preferred to
`== None`?"

Repeat the same three-level approach for:

-   mutability
-   references
-   shallow/deep copy
-   LEGB
-   memory management
-   GIL
