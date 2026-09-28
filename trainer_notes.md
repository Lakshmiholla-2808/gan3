# Trainer Notes --- How to Teach Python

## The same topic at three levels

### Level 1 --- Fresher

Use:

-   simple language
-   one small example
-   visual analogy
-   one exercise

Example:

> A list is like a changeable collection of items.

``` python
skills = ["Python", "SQL"]
skills.append("Git")
```

### Level 2 --- Developer

Add:

-   behavior
-   implementation considerations
-   edge cases
-   debugging

### Level 3 --- Corporate/Experienced

Add:

-   trade-offs
-   architecture
-   performance considerations
-   maintainability
-   testing
-   production failure modes
-   alternatives

------------------------------------------------------------------------

# Micro-teaching structure

Use:

``` text
Hook
↓
Problem
↓
Concept
↓
Example
↓
Live coding
↓
Common mistake
↓
Exercise
↓
Interview question
↓
Real-world application
```

## Example: Generators

### Hook

"What happens if your application has to process a 20 GB log file?"

### Problem

Loading everything into memory may be undesirable.

### Concept

A generator can produce records lazily.

### Live coding

``` python
def read_lines(path):
    with open(path, encoding="utf-8") as file:
        for line in file:
            yield line
```

### Common mistake

Treating a generator as a list.

### Exercise

Count ERROR lines without loading the entire file into a list.

### Interview

"Generator vs list?"

### Corporate application

Large-file processing and streaming-style workflows.

------------------------------------------------------------------------

# GitHub practice rule

For each topic, create:

``` text
topic/
├── README.md
├── examples/
├── exercises/
├── broken_code/
├── solutions/
└── interview_questions.md
```

Initially keep solutions in a separate location so learners do not
immediately see them.

------------------------------------------------------------------------

# Daily trainer drill

For every topic:

### Round 1

Explain it in 30 seconds.

### Round 2

Explain it in 3 minutes.

### Round 3

Teach it for 10 minutes with code.

### Round 4

Answer five follow-up questions.

### Round 5

Debug a broken example.

### Round 6

Give a real-world use case.

This is how you move from "I know Python" to "I can train people in
Python."

------------------------------------------------------------------------

# Portfolio checklist

By the end of Phase 1, your GitHub should show:

-   Python fundamentals
-   advanced Python
-   exercises
-   real-world labs
-   debugging exercises
-   unit-test examples
-   interview questions
-   trainer notes
-   README
-   project architecture
-   screenshots/output where useful

Do not fill the repository with copied tutorial code. Add your own
explanations and exercises.
