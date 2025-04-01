import datetime

# using now() to get current time
current_time = datetime.datetime.now()
print(f"\nFinished the assignment: {current_time}\n")
with open("./.data/logs/time.txt", "a") as f:
    f.write(f"Ended the assignment: {current_time}\n")