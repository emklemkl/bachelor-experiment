import datetime

# using now() to get current time
current_time = datetime.datetime.now()
print(f"\nFinished the assignment: {current_time}\n")
with open("./.data/logs/unique_time.txt", "a") as f:
    f.write(f"Ended (unique): {current_time}\n")