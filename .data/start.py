import datetime

# using now() to get current time
participant_name = input("\nEnter your name (or the alias you used when signing up): ")
current_time = datetime.datetime.now()
print(f"\n{participant_name} Started the assignment: {current_time}\n")
with open("./.data/logs/time.txt", "a") as f:
    f.write(f"{participant_name} Started the assignment: {current_time}\n")