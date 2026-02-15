from typing import Dict, Any


class Task:
    """Represent a single task."""

    def __init__(self, title: str, description: str, priority: int, done: bool = False) -> None:
        """Initialize a task with its properties."""
        self.title: str = title
        self.description: str = description
        self.priority: int = priority
        self.done: bool = done
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "done": self.done
        }
    
    @staticmethod
    def create_from_dict(data: Dict[str, Any]) -> 'Task':
        """Create a Task obj from a dictionary."""
        return Task(
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            done=data["done"]
        )
