# Prompt user for task detail 
task = input("Enter the task discription: ")
priority = input("Enter task's priority (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority"
    case "medium":
        reminder = f"'{task}' is a medium priority"
    case "low":
        reminder = f"'{task}' is a low priority."

# Add a reminder if the task is time sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention."
    print(f"Reminder: {reminder}") # Provide a customized reminder
else:
    reminder += " Consider completing it when you have free time."
    print(f"Note: {reminder}") # Provide a customized reminder

