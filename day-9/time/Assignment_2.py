# Create a program that:
# Schedules reminders for a list of tasks with specific deadlines.
# Checks which tasks are overdue based on the current date and time.
from datetime import datetime, timedelta
from collections import defaultdict
tasks = defaultdict(list)

def add_task(task_name, deadline_str):
    deadline = datetime.strptime(deadline_str, "%d/%m/%Y %H:%M:%S")
    tasks[deadline].append(task_name)

# Check overdue tasks
def check_overdue_tasks(current_time):
    overdue_tasks = []
    for deadline in tasks:
        if deadline < current_time:
            overdue_tasks.extend(tasks[deadline])
    return overdue_tasks

# Display all tasks
def display_tasks():
    for deadline, task_list in sorted(tasks.items()):
        for task in task_list:
            print(f"Task: {task}, Deadline: {deadline.strftime('%d/%m/%Y %H:%M:%S')}")

# Main program
if __name__ == "__main__":
    current_time = datetime.now()
    print(f"Current Date and Time: {current_time.strftime('%d/%m/%Y %H:%M:%S')}")

    # Example tasks
    add_task("Complete project report", "20/01/2025 15:00:00")
    add_task("Team meeting", "21/01/2025 10:00:00")
    add_task("Submit expense report", "19/01/2025 17:00:00")

    print("\nAll tasks:")
    display_tasks()

    overdue_tasks = check_overdue_tasks(current_time)
    if overdue_tasks:
        print("\nOverdue tasks:")
        for task in overdue_tasks:
            print(f"- {task}")
    else:
        print("\nNo overdue tasks.")
