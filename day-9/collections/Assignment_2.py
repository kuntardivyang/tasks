# Create a program that:
# Uses OrderedDict to maintain the order of tasks in a to-do list.
# Allows adding, removing, and displaying tasks in the order they were added.
from datetime import datetime
from collections import defaultdict

tasks = defaultdict(list)

def add_task(task_name, deadline):
    deadline = datetime.strptime(deadline, "%d/%m/%Y")
    tasks[deadline].append(task_name)

def remove_task(task_name):
    for deadline in list(tasks):
        if task_name in tasks[deadline]:
            tasks[deadline].remove(task_name)
            if not tasks[deadline]:
                del tasks[deadline]
            print(f'Task "{task_name}" removed.')
            return
    print(f'Task "{task_name}" not found.')

def display_tasks():
    if not tasks:
        print('No tasks in the to-do list.')
    else:
        for deadline, task_list in sorted(tasks.items()):
            for task in task_list:
                print(f'Task: {task}, Deadline: {deadline.strftime("%d/%m/%Y")}')

def overdue(current_time):
    overdue_tasks = []
    for deadline in tasks:
        if deadline < current_time:
            overdue_tasks.extend(tasks[deadline])
    return overdue_tasks

while True:
    print('''
        Type 1 to Add task
        Type 2 to Remove task
        Type 3 to Display tasks
        Type 4 to Check overdue tasks
        Type 5 to Exit
    ''')
    user_input = int(input())
    if user_input == 1:
        task_name = input('Enter the task name: ')
        deadline = input('Enter the task deadline date in this format (15/01/2025): ')
        add_task(task_name, deadline)
    elif user_input == 2:
        task_name = input('Enter the task name to remove: ')
        remove_task(task_name)
    elif user_input == 3:
        display_tasks()
    elif user_input == 4:
        current_time = datetime.now()
        overdue_tasks = overdue(current_time)
        if overdue_tasks:
            print("Overdue tasks:")
            for task in overdue_tasks:
                print(task)
        else:
            print("No overdue tasks.")
    elif user_input == 5:
        break
    else:
        print('Invalid input, please try again.')
