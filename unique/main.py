
# Task 1 (Write Program): Write a function unique_task that takes a list of integers and 
# returns the index of the second largest UNIQUE value in the list. 

# INSTRUCTIONS:
# Implement a function name unique_task using basic control structures.
# return the index of the second largest UNIQUE value in the list. 
# Be careful about duplicate values and UNIQUENESS checks.
# You may loop through the list multiple times, but you must implement UNIQUENESS tracking and indexing manually, using basic loops and conditionals.

# Example of uniqueness: [3, 3, 5, 1]
# The number 3 is not unique because it appears more than once.
# Unique values here are [5, 1]

# RESTRICTIONS:
# You are NOT allowed to use:
# - set()
# - list.count()  
# - list.index()
# - collections.Counter
# - sorted() or list.sort()
# - Dictionary comprehensions
# - You have 10 minutes

# Assumptions:
# - All elements are non-negative integers (no floats or negative numbers).
# - If there is no second largest unique value, return -1.

# Test using the provided examples.
example_list_1 = [9, 1, 4, 9, 5]
example_list_2 = [4, 1, 7, 7, 2, 3]
example_list_3 = [4]

def unique_task(arr):  # type: (list) -> int
    pass
    #
    # Write your code...
    #


if __name__ == "__main__":
    print(unique_task(example_list_1))