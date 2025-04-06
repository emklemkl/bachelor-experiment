import datetime
log_file_path = "./.data/logs/unique_time.txt"

# using now() to get current time
participant_name = input("\nEnter your student acronym (ex: emkl21): ")
participant_id = input("\nEnter your provided ID: ")
current_time = datetime.datetime.now()
print(f"\n{participant_name}(ID: {participant_id})Started the assignment: {current_time}\n")
with open(log_file_path, "a") as f:
    f.write(f"{participant_name}\nID {participant_id}\nStarted (unique): {current_time}\n")
