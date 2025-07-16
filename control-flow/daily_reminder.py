while True:
    print()
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    if time_bound == "yes" or time_bound == "no":
        match priority:
            case "high":
                if time_bound == "yes":
                    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
                else:
                    print(
                        f"Reminder: '{task}' is a high-priority task that requires your attention soon. While it doesn’t have a strict deadline, "
                        "completing it promptly will help keep your workload manageable.")
            case "medium":
                if time_bound == "yes":
                    print(
                        f"Reminder: '{task}' is a medium-priority task with a deadline. Please ensure you complete it on time to stay on track!")
                else:
                    print(
                        f"Reminder: '{task}' is a medium-priority task. While there’s no urgent deadline, Feel free to tackle it whenever it’s convenient for you.")
            case "low":
                if time_bound == "yes":
                    print(
                        f"Reminder: '{task}' is a low-priority task, but it does have a deadline. Work on it when you can to avoid last-minute delays.")
                else:
                    print(
                        f"Reminder: '{task}' is a low-priority task with no strict deadline. Consider completing it when you have free time.")
            case _:
                print("Invalid choice! Please select either high, medium or low.")
    else:
        print("Please select either yes or no.")

    print()
    exit_system = input("Do you want to exit the system (yes/no): ").lower()
    if exit_system == "yes":
        break
