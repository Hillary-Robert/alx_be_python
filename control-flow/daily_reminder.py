task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high" | "medium" | "low":
        pr_text = priority
    case _:
        pr_text = "unknown"

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {pr_text} priority task that requires immediate attention today!")
else:

    if pr_text == "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    elif pr_text == "medium":
        print(f"Note: '{task}' is a medium priority task. Plan to schedule it soon.")
    elif pr_text == "high":
        print(f"Note: '{task}' is a high priority task, but it's not time-bound.")
    else:
        print(f"Note: '{task}' has an unknown priority level.")