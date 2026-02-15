from task_manager import TaskManager


def main() -> None:
    """Main to run the program."""
    task_manager: TaskManager = TaskManager()
    task_manager.run()

if __name__ == "__main__":
    main()
