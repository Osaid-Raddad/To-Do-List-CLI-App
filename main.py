import os
import json

FILE_PATH= "tasks.json"

def add_task(tasks):
    """Add a new task to the list."""
    print("\nAdd New Task\n")
    title = input("Enter task title: ").strip()
    if not title:
        print("Title can't be empty")
        return

    description = input("Enter task description: ").strip()

    while True:
        priority = int(input("Enter priority (0-5 note that 0 is the highest):"))
        if 0 <= priority and priority <= 5:
            break
        else:
            print("Priority must be between 0 and 5")

    task = {
        "title": title,
        "description": description,
        "priority": priority,
        "done": False,
    }

    tasks.append(task)
    print(f"Task {title} added successfully")


def load_tasks():
    """Load tasks from the json file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            tasks = json.load(file)
        file.close()
        return tasks
    else:
        print("file not found.")
        return []


def display_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("\nNo tasks available\n")
        return

    print("\nTask List:\n")
    for index, task in enumerate(tasks, start=1):  
        status = "Done" if task["done"] else "Not Done"
        print(f"\n{index}. {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Status: {status}")

def sort_tasks_by_priority(tasks):
    """Display tasks sorted by priority."""
    if not tasks:
        print("\nNo tasks available\n")
        return

    sorted_tasks = sorted(tasks, key=lambda x: x['priority'])

    print("\nTasks Sorted by Priority\n")
    for index, task in enumerate(sorted_tasks, 1):
        status = "Done" if task["done"] else "Not Done"
        print(f"\n{index}. {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Status: {status}")

def mark_task_done(tasks):
    """Mark a task as Done."""
    if not tasks:
        print("\nNo tasks available")
        return
    
    display_tasks(tasks)
    task_num = int(input("\nEnter task number to mark as done: "))
    if 1 <= task_num and task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print(f"Task {tasks[task_num - 1]['title']} marked as done")
    else:
        print("Invalid task number")

def change_task_priority(tasks):
    """Change the priority level of a task."""
    if not tasks:
        print("\nNo tasks available")
        return
    
    display_tasks(tasks)
    task_num = int(input("\nEnter task number to change priority: "))
    if 1 <= task_num and task_num <= len(tasks):
        while True:
            new_priority = int(input("Enter new priority (0-5 where 0 is the highest): "))
            if 0 <= new_priority and new_priority <= 5:
                tasks[task_num - 1]["priority"] = new_priority
                print(f"Priority updated for task {tasks[task_num - 1]['title']}")
                break
            else:
                print("Priority must be between 0 and 5")                
    else:
        print("Invalid task number")

def delete_task(tasks):
    """Delete a task from the list."""
    if not tasks:
        print("\nNo tasks available\n")
        return
    
    display_tasks(tasks)  
    task_num = int(input("\nEnter task number to delete: "))
    if 1 <= task_num and task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        print(f"Task {deleted_task['title']} deleted successfully!")
    else:
        print("Invalid task number")  

def save_changes(tasks):
    """Save tasks to the json file."""
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)
    file.close()
    print("Tasks saved successfully")

def print_operations():
    "Display the available operations to the user."
    print(
        "\n\n-----------------------Available Operations-----------------------\n"
        "1. Add a Task\n"
        "2. View Tasks\n"
        "3. Sort Tasks by Priority\n"
        "4. Mark Task as Done\n"
        "5. Change Task Priority\n"
        "6. Delete Task\n"
        "7. Save\n"
        "8. Exit Program\n"
    )

def main():
    """Main function to run the program."""
    tasks = load_tasks()
    while True:
        print_operations()
        operation = int(input("Enter operation number (from 1 to 8):"))
        if operation < 1 or operation > 8:
            print("Invalid operation number, Please enter a number between 1 and 8.")
            continue
        match operation:
            case 1:
                add_task(tasks)
            case 2:
                display_tasks(tasks)
            case 3:
                sort_tasks_by_priority(tasks)
            case 4:
                mark_task_done(tasks)
            case 5:
                change_task_priority(tasks)
            case 6:
                delete_task(tasks)
            case 7:
                save_changes(tasks)
            case 8:
                print("Exiting program :)")
                break
            case _:
                print("Error Please try again")

if __name__ == "__main__":
    main()
