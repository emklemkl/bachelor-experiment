#!/usr/bin/env python3

"""
Task 2 (Write Program):
Write a function `task2` that takes one string argument and counts the number of words 
that have exactly four characters and end with an 'e'.

def task2(s: str) -> int:
    ...

Assumptions:
- You may assume that all words end in either ' ' (space) or '.' (dot).

Example:
If called with the string argument:
    task2("Once upon a time.")
The function should return 2, because "Once" and "time." (ignoring punctuation) 
have exactly four characters and end in 'e'.

RESTRICTIONS:
You are only allowed to use the following string methods:
- s[i]    # Select character at index
- len(s)  # Get the length of a string
- You have 10 minutes

You are NOT allowed to use:
- s.split()  
- s.join()  
- Regular expressions (re module)
- Any kind of AI

INSTRUCTIONS:
- Implement the `task2` function following the restrictions above.
- Test your function using the example provided.
- Submit your `main.py` file as per the given instructions.
"""

example_test_string = "Once upon a time. I had a baseball."

def task2(str: str) -> int:
    print(str)
    #
    # Write your code...
    #

if __name__ == "__main__":
    task2(example_test_string)
