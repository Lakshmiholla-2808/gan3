# 07 --- Broken Code and Debugging

A corporate trainer should be able to teach debugging, not only
successful code.

Use this process:

``` text
WHAT happened?
↓
WHERE did it happen?
↓
WHY did it happen?
↓
VERIFY the hypothesis
↓
FIX
↓
PREVENT recurrence
```

# Bug 1 --- Mutable default argument

Broken:

``` python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))
```

Ask the learner:

Why does the second call contain the first item?

Fix:

``` python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

Trainer discussion:

Default argument expressions are evaluated when the function is defined,
not every time the function is called.

------------------------------------------------------------------------

# Bug 2 --- is vs ==

Broken:

``` python
status = "approved"

if status is "approved":
    print("Approved")
```

The correct value comparison is:

``` python
if status == "approved":
    print("Approved")
```

For a singleton such as `None`:

``` python
if value is None:
    ...
```

------------------------------------------------------------------------

# Bug 3 --- Shallow copy surprise

``` python
import copy

data = [[1, 2], [3, 4]]
new_data = copy.copy(data)

new_data[0].append(99)

print(data)
```

Ask:

Why did the original nested list change?

Then demonstrate `copy.deepcopy()`.

------------------------------------------------------------------------

# Bug 4 --- Consuming an iterator

``` python
numbers = iter([1, 2, 3])

print(list(numbers))
print(list(numbers))
```

Why is the second result empty?

The iterator was already consumed.

------------------------------------------------------------------------

# Bug 5 --- Blocking inside async code

Conceptual broken example:

``` python
import time
import asyncio

async def work():
    time.sleep(3)
```

Why is this problematic?

`time.sleep()` blocks the thread/event loop.

For an async waiting example:

``` python
await asyncio.sleep(3)
```

The appropriate solution depends on the actual workload.

------------------------------------------------------------------------

# Bug 6 --- Forgotten await

``` python
async def get_data():
    return "data"

result = get_data()
print(result)
```

Ask:

Why isn't `result` the returned string?

Because calling an async function creates a coroutine object; it must be
awaited in an appropriate async context.

------------------------------------------------------------------------

# Trainer challenge

For every bug:

1.  Ask the learner what they observe.
2.  Ask them to predict the output.
3.  Ask where they think the problem is.
4.  Let them test the hypothesis.
5.  Fix it.
6.  Ask how to prevent it in a real project.
