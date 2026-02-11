import os
import json

class Task:
    """Represent a single task."""

    def __init__(self, title, description, priority, done=False):
        """Initialize a task with its properties."""
        self.title = title
        self.description = description
        self.priority = priority
        self.done = done
    
    def to_dict(self):
        """Convert task to dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "done": self.done
        }
    
    @staticmethod
    def create_from_dict(data):
        """Create a Task obj from a dictionary."""
        return Task(
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            done=data["done"]
        )


class TaskManager:
    """Manages all task operations."""
    
    def __init__(self, file_path="tasks.json"):
        """Initialize TaskManager with file path."""
        self.file_path = file_path
        self.tasks = self.load_tasks()
    
    def add_task(self):
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

        task = Task(title, description, priority, False)
        self.tasks.append(task)
        print(f"Task {title} added successfully")

    def load_tasks(self):
        """Load tasks from the json file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                tasks_data = json.load(file)
            file.close()
            return [Task.create_from_dict(task_data) for task_data in tasks_data]
        else:
            print("file not found.")
            return []

    def display_tasks(self):
        """Display all tasks with their status."""
        if not self.tasks:
            print("\nNo tasks available\n")
            return

        print("\nTask List:\n")
        for index, task in enumerate(self.tasks, start=1):  
            status = "Done" if task.done else "Not Done"
            print(f"\n{index}. {task.title}")
            print(f"   Description: {task.description}")
            print(f"   Priority: {task.priority}")
            print(f"   Status: {status}")

    def sort_tasks_by_priority(self):
        """Display tasks sorted by priority."""
        if not self.tasks:
            print("\nNo tasks available\n")
            return

        sorted_tasks = sorted(self.tasks, key=lambda x: x.priority)

        print("\nTasks Sorted by Priority\n")
        for index, task in enumerate(sorted_tasks, 1):
            status = "Done" if task.done else "Not Done"
            print(f"\n{index}. {task.title}")
            print(f"   Description: {task.description}")
            print(f"   Priority: {task.priority}")
            print(f"   Status: {status}")

    def mark_task_done(self):
        """Mark a task as Done."""
        if not self.tasks:
            print("\nNo tasks available")
            return
        
        self.display_tasks()
        task_num = int(input("\nEnter task number to mark as done: "))
        if 1 <= task_num and task_num <= len(self.tasks):
            self.tasks[task_num - 1].done = True
            print(f"Task {self.tasks[task_num - 1].title} marked as done")
        else:
            print("Invalid task number")

    def change_task_priority(self):
        """Change the priority level of a task."""
        if not self.tasks:
            print("\nNo tasks available")
            return
        
        self.display_tasks()
        task_num = int(input("\nEnter task number to change priority: "))
        if 1 <= task_num and task_num <= len(self.tasks):
            while True:
                new_priority = int(input("Enter new priority (0-5 where 0 is the highest): "))
                if 0 <= new_priority and new_priority <= 5:
                    self.tasks[task_num - 1].priority = new_priority
                    print(f"Priority updated for task {self.tasks[task_num - 1].title}")
                    break
                else:
                    print("Priority must be between 0 and 5")                
        else:
            print("Invalid task number")

    def delete_task(self):
        """Delete a task from the list."""
        if not self.tasks:
            print("\nNo tasks available\n")
            return
        
        self.display_tasks()  
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num and task_num <= len(self.tasks):
            deleted_task = self.tasks.pop(task_num - 1)
            print(f"Task {deleted_task.title} deleted successfully!")
        else:
            print("Invalid task number")  

    def save_changes(self):
        """Save tasks to the json file."""
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        file.close()
        print("Tasks saved successfully")

    def print_operations(self):
        """Display the available operations to the user."""
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

    def run(self):
        """A loop to run the program."""
        while True:
            self.print_operations()
            operation = int(input("Enter operation number (from 1 to 8):"))
            if operation < 1 or operation > 8:
                print("Invalid operation number, Please enter a number between 1 and 8.")
                continue
            match operation:
                case 1:
                    self.add_task()
                case 2:
                    self.display_tasks()
                case 3:
                    self.sort_tasks_by_priority()
                case 4:
                    self.mark_task_done()
                case 5:
                    self.change_task_priority()
                case 6:
                    self.delete_task()
                case 7:
                    self.save_changes()
                case 8:
                    print("Exiting program :)")
                    break
                case _:
                    print("Error Please try again")


def main():
    """Main to run the program."""
    task_manager = TaskManager()
    task_manager.run()

if __name__ == "__main__":
    main()
