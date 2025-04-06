# Bachelor-experiment

## Instructions for the unique-task 

## BEFORE YOU START

**You should read everything on this page before the title "TASK unique - Write Program".**

Start the experiment by running the python3 start script. Finish by running the finished script (more info below).
If you run a start or finish command twice, or enter the wrong ID/acronym, it’s fine—just rerun the script with the correct info.

Let us know before leaving the experiment.
Once you've stopped the assignment timer, do not change your code, even if you find bugs.
You won’t be judged—just do your best and submit when you're satisfied.
After submission, we’ll anonymize the data.

**Before you start reading under "TASK unique - Write Program" or open main.py make sure to start the timer.**


**EXACTLY THE SAME INSTRUCTIONS YOU SEE BELOW CAN BE FOUND IN THE main.py**
# Start and Stop assignment
👉 Open the project in your preferred text editor.  
👉 Stand in **bachelor-experiment/unique/** 
## Start Timer in terminal:
**Start:** ```python3 ./.data/start.py```
- Enter your student acronym: eg. (emkl21)
- Enter your provided ID: eg. (1) **!!Don't press Enter yet!!**
- Let us know you have come this far

## When you are finished:
**Stop:** ```python3 ./.data/finished.py```

## Execute code:
Stand in "unique/"
**Test code:** ```python3 main.py```



## TASK unique - Write Program

- You have 10 minutes

Write a function called `unique_task` that takes a list of integers and 
returns the index of the second largest UNIQUE value in the list. 
```
def unique_task(li: list) -> int: ...
```

### Assumptions:
- All elements are non-negative integers (no floats or negative numbers).
- If there is no second largest unique value, return -1.

### Example
- Example of uniqueness: [3, 3, 5, 1]
- The number 3 is not unique because it appears more than once.
- Unique values here are [5, 1]
- Second largest unique value in this example is 1.

### RESTRICTIONS
You are NOT allowed to use:
- set()
- list.count()  
- list.index()
- collections.Counter
- sorted() or list.sort()
- Dictionary comprehensions
- Any kind of AI, such as ChatGPT or CoPilot (IntelliSense is ok as it not an AI)


## INSTRUCTIONS:
- Implement a function named unique_task using basic control structures.
- Be careful about duplicate values and UNIQUENESS checks.
- You may loop through the list multiple times, but you must implement UNIQUENESS tracking and indexing manually, using basic loops and conditionals.
