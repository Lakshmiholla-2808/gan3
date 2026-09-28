# 06 --- Real-World Labs

These labs are designed to turn knowledge into trainer-ready skills.

# Lab 1 --- Employee Salary Processor

Build:

``` text
Employee ID
Name
Department
Salary
Experience
```

Requirements:

1.  Store employees in a list of dictionaries.
2.  Display all employees.
3.  Filter employees by department.
4.  Find employees above a salary threshold.
5.  Calculate average salary.
6.  Sort employees by salary.
7.  Convert records into a dictionary keyed by employee ID.

Concepts:

-   list
-   dictionary
-   loops
-   functions
-   comprehensions
-   lambda
-   sorted

------------------------------------------------------------------------

# Lab 2 --- Employee Service

Create functions:

``` python
add_employee()
get_employee()
update_employee()
delete_employee()
list_employees()
```

Add:

-   validation
-   custom exceptions
-   logging

This introduces CRUD thinking before FastAPI.

------------------------------------------------------------------------

# Lab 3 --- Log File Analyzer

Input: a text log file.

Build functions to:

-   count ERROR lines
-   count WARNING lines
-   find the most common error
-   produce a summary dictionary

Trainer concepts:

-   file handling
-   functions
-   dictionaries
-   generators
-   exceptions

------------------------------------------------------------------------

# Lab 4 --- Large File Processor

Create a generator:

``` python
def read_large_file(path):
    ...
    yield line
```

Then process records without constructing a huge list.

Explain why this is useful.

------------------------------------------------------------------------

# Lab 5 --- Decorator for Timing

Create a decorator:

``` python
@timer
def calculate():
    ...
```

It should report execution time.

Then discuss:

-   decorators
-   `*args`
-   `**kwargs`
-   return values
-   logging

------------------------------------------------------------------------

# Lab 6 --- Context Manager

Create a context manager that logs:

``` text
Resource acquired
Work performed
Resource released
```

Then explain why cleanup belongs in a context manager.

------------------------------------------------------------------------

# Lab 7 --- Async API Simulation

Create three async tasks that each wait for a different amount of time.

Compare:

1.  sequential execution
2.  `asyncio.gather()`

Measure elapsed time.

Trainer goal:

Explain that the benefit comes from overlapping waiting, not from making
CPU instructions magically faster.

------------------------------------------------------------------------

# Lab 8 --- Mini Project

Build:

## Employee Management CLI

Features:

-   add employee
-   update employee
-   delete employee
-   search employee
-   list employees
-   save to JSON
-   load from JSON
-   logging
-   validation
-   exceptions

Then create:

``` text
README
architecture diagram
test cases
interview questions
trainer explanation
```

This becomes your first portfolio artifact.
