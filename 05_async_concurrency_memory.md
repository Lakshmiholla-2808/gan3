# 05 --- Async, Concurrency, Parallelism and the GIL

# Threading

Threads allow multiple threads of execution within a process.

Conceptually useful for I/O-bound workloads.

Example:

``` python
from concurrent.futures import ThreadPoolExecutor
import time

def download(item):
    time.sleep(1)
    return f"Downloaded {item}"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(download, ["A", "B", "C"]))

print(results)
```

The example simulates waiting.

------------------------------------------------------------------------

# Multiprocessing

Processes are separate operating-system processes.

Useful when CPU-bound work can benefit from multiple CPU cores, subject
to the application and environment.

``` python
from concurrent.futures import ProcessPoolExecutor

def square(x):
    return x * x

with ProcessPoolExecutor() as executor:
    results = list(executor.map(square, range(10)))

print(results)
```

Trainer point:

Multiprocessing has different memory/process overhead from threads.

------------------------------------------------------------------------

# AsyncIO

Async programming allows cooperative execution of tasks, especially
useful for I/O-bound workloads.

``` python
import asyncio

async def work(name):
    print(f"Start {name}")
    await asyncio.sleep(1)
    print(f"Finish {name}")

async def main():
    await asyncio.gather(
        work("A"),
        work("B"),
        work("C")
    )

asyncio.run(main())
```

The `await` gives the event loop an opportunity to run other tasks while
the coroutine is waiting.

------------------------------------------------------------------------

# Does async make Python faster?

Not automatically.

The better answer is:

> Async can improve throughput and responsiveness for suitable I/O-bound
> workloads by allowing other work to run while one task is waiting. It
> does not automatically make CPU-heavy computation faster.

For CPU-heavy work, investigate:

-   algorithmic improvements
-   multiprocessing
-   native extensions
-   specialized libraries
-   distributed processing when appropriate

------------------------------------------------------------------------

# Threading vs multiprocessing vs asyncio

  Approach          Typical strength          Key idea
  ----------------- ------------------------- -------------------------------
  Threading         I/O-bound work            multiple threads in a process
  Multiprocessing   CPU-bound parallel work   separate processes
  asyncio           high-concurrency I/O      cooperative event loop

This is a simplification, not a rule that applies to every workload.

------------------------------------------------------------------------

# GIL interview answer

A strong answer:

> In standard CPython, the GIL is a mechanism that prevents multiple
> threads from executing Python bytecode simultaneously within the same
> interpreter. This limits CPU-bound parallelism using ordinary Python
> threads. Threads can still be useful for I/O-bound tasks, and
> multiprocessing can provide process-level parallelism.

Then add:

> I would avoid saying "Python has no multithreading" because that is
> incorrect.

------------------------------------------------------------------------

# Event loop mental model

Think:

``` text
Task A starts
   ↓
waits for I/O
   ↓
event loop runs Task B
   ↓
Task B waits
   ↓
event loop runs Task C
   ↓
Task A becomes ready
   ↓
continue Task A
```

The goal is efficient use of waiting time.

------------------------------------------------------------------------

# Trainer exercise

Explain the following scenario:

A web service receives 1,000 requests. Most requests spend time waiting
for external APIs.

Ask:

1.  Why might asyncio be useful?
2.  Would asyncio make CPU calculations faster?
3.  When could threads be reasonable?
4.  When might processes be considered?
5.  What role does the GIL play?

Then ask the learner to draw the flow.
