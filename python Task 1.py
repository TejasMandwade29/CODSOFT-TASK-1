import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    """Load tasks from a file."""
    if not os.path.isfile(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        tasks = file.read().splitlines()
    return tasks

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def update_task(tasks):
    """Update a task in the list."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_num - 1] = new_task
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task from the list."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Delete a task")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()