# bachelor-experiment


## BEFORE YOU START

**You should read everything on this page before the title "TASK 2 - Write Program". Before you start reading under "TASK 2 - Write Program" you should start the timer.**

1. Before you start reading "TASK 2 - Write a program" assignment below you are required to run: 
    `python3 ./.data/start.py`

## WHEN YOU ARE FINISHED

1. When you are ready to turn in your assignment, run:
    ```
    python3 ./.data/finished.py
    ``` 

2. After stopping the time, zip your program.(Replace < YOUR-ASSIGNED-ID > with your id, etc: task2-2.zip).   
   If you are using WSL2: Stand in the root of the project and run:
    ```
    zip -r task2-<YOUR-ASSIGNED-ID>.zip . 
    ```
    To move the zip file to Windows desktop you have two choices:
    ```
    mv task2-<YOUR-ASSIGNED-ID>.zip /mnt/c/Users/<YOUR-WINDOWS-USERNAME>/Desktop/

    or by opening and using the windows explorer:

    explorer.exe .
    
    ```
If you accidentally run the same start/finished command two times, no worries, its basically just a log entry. Just let us know before you leave the experiment. When you have stopped the assignment timer, please do not change ANYTHING in your code, even if you see a bug. Changes after triggering the stop timer would skew the result. You will not be personally judged in any way for mistakes. In fact, you can treat this task as any other school assignments, when you think it's good enough and you have solved the task to the best of your abilities, just turn it in.
As soon as we gather up the results we will start the anonymization process of the data.

## TASK 2 - Write Program

**EXACTLY THE SAME INSTRUCTIONS YOU SEE BELOW CAN BE FOUND IN THE main.py**

Write a function named `task2` that takes one string argument and counts the number of words 
that have exactly four characters and end with an 'e'.
```
def task2(s: str) -> int: ...
```

### Assumptions:
- You may assume that all words end in either ' ' (space) or '.' (dot).

### Example
If called with the string argument:
    `task2("Once upon a time. I had a baseball.")`
The function should return 2, because "Once" and "time." (ignoring punctuation) 
have exactly four characters and end in 'e'.

### RESTRICTIONS
You are only allowed to use the following string methods:
- s[i]
- len(s)

You are NOT allowed to use:
- s.split() 
- s.join() 
- Regular expressions (re module)

INSTRUCTIONS:
- Implement the `task2` function following the restrictions above.
- Test your function using the example provided.
- Submit your `main.py` file as per the given instructions.
"""
