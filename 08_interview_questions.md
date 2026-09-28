# 08 --- Python Technical Interview Bank

Use these questions for daily oral practice.

## Basic

### 1. What are Python's built-in data types?

Mention common built-ins such as numbers, strings, lists, tuples, sets,
dictionaries, booleans and `None`.

Follow-up: Which are mutable?

------------------------------------------------------------------------

### 2. List vs tuple?

Discuss:

-   mutability
-   intended semantics
-   common use cases

------------------------------------------------------------------------

### 3. Set vs list?

Discuss:

-   uniqueness
-   ordering/sequence semantics
-   membership operations

------------------------------------------------------------------------

### 4. Dictionary vs list?

Discuss:

-   key-value lookup
-   sequence vs mapping

------------------------------------------------------------------------

### 5. What is mutable vs immutable?

Give examples:

Mutable: - list - dict - set

Common immutable examples: - int - float - bool - str - tuple

------------------------------------------------------------------------

### 6. What is dynamic typing?

Python names can refer to objects of different types at different times.

------------------------------------------------------------------------

### 7. What is variable scope?

Explain where a name can be accessed.

------------------------------------------------------------------------

### 8. Explain LEGB.

Local → Enclosing → Global → Built-in.

------------------------------------------------------------------------

### 9. `is` vs `==`?

`==` tests equality of values.

`is` tests object identity.

------------------------------------------------------------------------

### 10. What is slicing?

Explain:

``` python
sequence[start:stop:step]
```

------------------------------------------------------------------------

## Intermediate

### 11. What are list comprehensions?

Concise syntax for constructing lists from iterables, often with
transformation and filtering.

------------------------------------------------------------------------

### 12. Dictionary comprehensions?

Example:

``` python
{x: x*x for x in range(5)}
```

------------------------------------------------------------------------

### 13. What are \*args and \*\*kwargs?

`*args` collects extra positional arguments.

`**kwargs` collects extra keyword arguments.

------------------------------------------------------------------------

### 14. What is lambda?

A small anonymous function expression.

------------------------------------------------------------------------

### 15. map vs filter?

`map` transforms elements.

`filter` selects elements satisfying a condition.

------------------------------------------------------------------------

### 16. What does zip do?

Combines values from iterables into tuples, stopping when the shortest
iterable is exhausted under normal `zip()` behavior.

------------------------------------------------------------------------

### 17. enumerate?

Produces index-value pairs while iterating.

------------------------------------------------------------------------

### 18. Generator?

A lazy iterator-producing construct commonly created with `yield`.

------------------------------------------------------------------------

### 19. Generator vs list?

A list materializes the collection.

A generator produces values lazily.

Discuss memory and one-pass behavior.

------------------------------------------------------------------------

### 20. What is an iterator?

An object that provides successive values through the iterator protocol.

------------------------------------------------------------------------

## Advanced

### 21. What is a decorator?

A callable that accepts another callable and returns a callable with
modified/enhanced behavior.

------------------------------------------------------------------------

### 22. How do decorators work?

Explain function objects, wrapper functions and `@decorator` syntax.

------------------------------------------------------------------------

### 23. Context manager?

An abstraction for managing setup/cleanup around a block.

------------------------------------------------------------------------

### 24. How does `with` work?

Explain context manager protocol conceptually and mention `__enter__` /
`__exit__` for class-based context managers.

------------------------------------------------------------------------

### 25. Shallow vs deep copy?

Shallow copies the outer container while nested references may remain
shared.

Deep copy recursively copies nested objects subject to the objects' copy
behavior.

------------------------------------------------------------------------

### 26. How does Python manage memory?

Discuss objects, references, CPython reference counting, cyclic garbage
collection and memory allocation.

Avoid oversimplification.

------------------------------------------------------------------------

### 27. Garbage collection?

Discuss automatic management of unreachable objects and cyclic garbage
collection in CPython.

------------------------------------------------------------------------

### 28. Reference counting?

In CPython, objects maintain reference counts; when the count reaches
zero, the object's memory can generally be reclaimed promptly. Cycles
require cyclic GC.

------------------------------------------------------------------------

### 29. What is the GIL?

A CPython mechanism affecting simultaneous execution of Python bytecode
by threads within an interpreter.

------------------------------------------------------------------------

### 30. Threading vs multiprocessing?

Threads share a process's memory space and are often useful for
I/O-bound work.

Processes have separate process memory and can provide process-level
parallelism for suitable CPU-bound workloads.

------------------------------------------------------------------------

### 31. Multiprocessing vs asyncio?

Multiprocessing uses separate processes.

Asyncio uses cooperative scheduling of coroutines in an event loop,
especially useful for I/O concurrency.

------------------------------------------------------------------------

### 32. Does async make Python faster?

Not inherently.

It can improve throughput for suitable I/O-bound workloads by
overlapping waiting.

------------------------------------------------------------------------

### 33. When should asynchronous programming be used?

When the workload involves substantial asynchronous I/O and the
surrounding libraries/frameworks support it appropriately.

Do not use async merely because it sounds faster.

------------------------------------------------------------------------

# Trainer follow-up questions

After each answer, ask:

1.  Can you give a simple example?
2.  Where would you use this in a real application?
3.  What is the limitation?
4.  What is the alternative?
5.  What common mistake do beginners make?
6.  How would you explain this to a manager?
7.  How would you explain it to a fresher?
8.  What would an experienced developer challenge?

------------------------------------------------------------------------

# 3-minute explanation template

For any Python topic:

``` text
1. Problem
2. Concept
3. Tiny example
4. Real-world example
5. Common mistake
6. Interview question
7. Trade-off / limitation
```

Example: Generator

``` text
Problem:
A huge dataset should not always be materialized at once.

Concept:
Generators produce values lazily.

Example:
yield

Real-world:
Process a large file line by line.

Mistake:
Assuming a generator can be indexed like a list.

Interview:
Generator vs list?

Trade-off:
Generators are often memory-efficient, but they are typically consumed progressively and are not a random-access collection.
```
