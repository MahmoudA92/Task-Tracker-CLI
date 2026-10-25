"""
Task Tracker CLI
Stage 1: menu skeleton
"""

import json
from pathlib import Path

FILE = "tasks.json"

# Helper functions 
def print_menu() -> None:
    print("\n Task Tracker Menu: \n")
    menu : list[str] = ["add task", "list tasks", "complete task", "exit"]
    for index, item in enumerate(menu, start=1):
        print(f"   {index}) {item}")

# File Handling functions
def load_tasks() -> list[dict]:
    """
    Load tasks from a JSON file.
    Returns a list of task dicts.
    """
    if not Path(FILE).exists():
        return[]
    with open(FILE, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def save_tasks(tasks: list[dict]) -> None:
    """
    Save tasks to a JSON file.
    """
    with open(FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)

# Features functions 
def add_task(tasks: list[dict]) -> list[dict]:
    """
    Create a new task dict and append to tasks list.
    
    Task shape: {"name": str, "priority": str, "done": bool}
    Returns the new task.
    """
    name = input("\n Enter task name: ").strip()
    priority = input("\n Enter task priority (low, medium, high): ").strip().lower()
    done = False

    if not name or priority not in ["low", "medium", "high"]:
        print("\n Invalid task name or priority. Task not added.")
        return tasks

    new_task = {"name": name, "priority": priority, "done": done}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"\n Task '{name}' added successfully!")
    return tasks

def list_tasks(tasks: list[dict]) -> None:
    """
    Print all tasks in a formatted way.
    """
    if not tasks:
        print("\n No tasks found.")
        return

    print("\n Task List:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"   {index}) {task['name']} - Priority: {task['priority'].capitalize()} - Status: {status}")

def complete_task(tasks: list[dict]) -> list[dict]:
    """
    Mark a task as done based on user input.
    Returns the updated tasks list.
    """
    if not tasks:
        print("\n No tasks to complete.")
        return tasks

    list_tasks(tasks)
    print("\n Enter the number of the task to mark as done: ")
    index_str = int(input().strip()) - 1
    if 0 <= index_str < len(tasks):
        tasks[index_str]["done"] = True
        save_tasks(tasks)
        print(f"\n Task '{tasks[index_str]['name']}' marked as done!")
    else:
        print("\n Invalid task number.")
    return tasks

def main():
    print("\n Welcome to the Task Tracker!")

    tasks : list[dict] = load_tasks()

    while True:
        print_menu()

        choice : str = input("\n Choose: ").strip()
        
        match choice:
            case "1":
                tasks = add_task(tasks)
            case "2":
                list_tasks(tasks)
            case "3":
                tasks = complete_task(tasks)
            case "4":
                print("\n Goodbye!, my Friend 👋\n")
                break
            case _:
                print(f"\n please choose between 1-4 as a valid option \n")

if __name__ == "__main__":
    main()