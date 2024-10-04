import json
import os

# Task Manager class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def load_tasks(self, filename='tasks.json'):
        """Load tasks from a file."""
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self, filename='tasks.json'):
        """Save tasks to a file."""
        with open(filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        """Add a new task to the list."""
        task = {'description': description, 'done': False}
        self.tasks.append(task)
        print(f"Task added: {description}")

    def edit_task(self, task_id, new_description):
        """Edit an existing task."""
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]['description'] = new_description
            print(f"Task {task_id} updated to: {new_description}")
        else:
            print(f"Task ID {task_id} not found.")

    def remove_task(self, task_id):
        """Remove a task from the list."""
        if 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            print(f"Task removed: {removed_task['description']}")
        else:
            print(f"Task ID {task_id} not found.")

    def mark_done(self, task_id):
        """Mark a task as done."""
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]['done'] = True
            print(f"Task {task_id} marked as done.")
        else:
            print(f"Task ID {task_id} not found.")

    def show_tasks(self):
        """Display all tasks with their status."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(self.tasks):
                status = "Done" if task['done'] else "Pending"
                print(f"{i}. [{status}] {task['description']}")
        print()

# Command-line interface for the task manager
def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("\nTask Manager:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Mark Task as Done")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            manager.show_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            manager.add_task(description)
            manager.save_tasks()
        elif choice == '3':
            manager.show_tasks()
            try:
                task_id = int(input("Enter the task ID to edit: "))
                new_description = input("Enter new task description: ")
                manager.edit_task(task_id, new_description)
                manager.save_tasks()
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '4':
            manager.show_tasks()
            try:
                task_id = int(input("Enter the task ID to remove: "))
                manager.remove_task(task_id)
                manager.save_tasks()
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '5':
            manager.show_tasks()
            try:
                task_id = int(input("Enter the task ID to mark as done: "))
                manager.mark_done(task_id)
                manager.save_tasks()
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '6':
            print("Exiting Task Manager...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
