# Bachelor-experiment

## BEFORE YOU START

**You should read everything on this page before the title "TASK 2 - Write Program".**

Start the experiment by running the python3 start script. Finish by running the finished script (more info below).
If you run a start or finish command twice, or enter the wrong ID/acronym, it’s fine—just rerun the script with the correct info.

Let us know before leaving the experiment.
Once you've stopped the assignment timer, do not change your code, even if you find bugs.
You won’t be judged—just do your best and submit when you're satisfied.
After submission, we’ll anonymize the data.

**Before you start reading under "TASK 2 - Write Program" or open main.py make sure to start the timer.**


**EXACTLY THE SAME INSTRUCTIONS YOU SEE BELOW CAN BE FOUND IN THE main.py**
# Start and Stop assignment
👉 Open the project in your preferred text editor.
Stand in bachelor-experiment/synthesis/ 
## Start Timer in terminal:
**Start:** ```python3 ./.data/start.py```
- Enter your student acronym: eg. (emkl21)
- Enter your provided ID: eg. (1) **!!Don't press Enter yet!!**
- Let us know you have come this far

## When you are finished:
**Stop:** ```python3 ./.data/finished.py```

## Execute code:
**Test code:** ```python3 main.py```



## TASK 2 - Write Program

Write a function named `task2` that takes one string argument and counts the number of words 
that have exactly four characters and end with an 'e'.
```
def task2(s: str) -> int: ...
```

### Assumptions:
- You may assume that all words end in either ' ' (space) or '.' (dot).

### Example
If called with the string argument:


    `task2("Once upon a time.")`


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
- Any kind of AI, such as ChatGPT or CoPilot (IntelliSense is ok as it not an AI)

INSTRUCTIONS:
- Implement the `task2` function following the restrictions above.
- Test your function using the example provided.
- Submit your `main.py` file as per the given instructions.
"""
