# # Source Code from codingdidi:

# # Initialize an empty list to store tasks
# tasks = []
# # Function to add a task
# def add_task():
#     title = input("Enter task title: ")
#     description = input("Enter task description: ")
#     tasks.append({"title": title, "description": description})
#     print("Task added successfully!")
# # Function to view all tasks
# def view_tasks():
#     if tasks:
#         print("Tasks:")
#         for idx, task in enumerate(tasks, start=1):
#             print(f"{idx}. Title: {task['title']}, Description: {task['description']}")
#     else:
#         print("No tasks available.")
# # Function to update a task
# def update_task():
#     view_tasks()
#     if tasks:
#         task_index = int(input("Enter the index of the task to update: ")) - 1
#         if 0 <= task_index < len(tasks):
#             new_title = input("Enter new title (Press Enter to skip): ")
#             new_description = input("Enter new description (Press Enter to skip): ")
#             if new_title:
#                 tasks[task_index]['title'] = new_title
#             if new_description:
#                 tasks[task_index]['description'] = new_description
#             print("Task updated successfully!")
#         else:
#             print("Invalid task index.")
#     else:
#         print("No tasks available.")
# # Function to delete a task
# def delete_task():
#     view_tasks()
#     if tasks:
#         task_index = int(input("Enter the index of the task to delete: ")) - 1
#         if 0 <= task_index < len(tasks):
#             deleted_task = tasks.pop(task_index)
#             print(f"Task '{deleted_task['title']}' deleted successfully!")
#         else:
#             print("Invalid task index.")
#     else:
#         print("No tasks available.")
# # Main loop
# while True:
#     print("\nInteractive Task Manager")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Update Task")
#     print("4. Delete Task")
#     print("5. Exit")
    
#     choice = input("Select an option (1-5): ")
    
#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         update_task()
#     elif choice == "4":
#         delete_task()
#     elif choice == "5":
#         print("Exiting the Task Manager. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please select a valid option (1-5).")

import json
from datetime import datetime

# List to store tasks
tasks = []

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    priority = input("Enter task priority (Low, Medium, High): ").capitalize()
    while priority not in ['Low', 'Medium', 'High']:
        print("Invalid priority. Please choose from Low, Medium, or High.")
        priority = input("Enter task priority (Low, Medium, High): ").capitalize()
    
    due_date_str = input("Enter task due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Task not added.")
        return

    task = {
            "title": title,
            "description": description,
            "priority": priority,
            "due_date": due_date.strftime("%Y-%m-%d")  # Store the date as string
        }
        
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

def view_tasks():
    if tasks:
        print("\nTasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. Title: {task['title']}, Description: {task['description']}, "
                  f"Priority: {task['priority']}, Due Date: {task['due_date']}")
    else:
        print("No tasks available.")

def update_task():
    view_tasks()
    if tasks:
        try:
            task_index = int(input("Enter the index of the task to update: ")) - 1
            if 0 <= task_index < len(tasks):
                task = tasks[task_index]
                new_title = input(f"Enter new title (current: {task['title']}) (Press Enter to skip): ")
                new_description = input(f"Enter new description (current: {task['description']}) (Press Enter to skip): ")
                new_priority = input(f"Enter new priority (current: {task['priority']}) (Low, Medium, High) (Press Enter to skip): ").capitalize()
                new_due_date_str = input(f"Enter new due date (current: {task['due_date']}) (YYYY-MM-DD) (Press Enter to skip): ")
                
                if new_title:
                    task['title'] = new_title
                if new_description:
                    task['description'] = new_description
                if new_priority in ['Low', 'Medium', 'High']:
                    task['priority'] = new_priority
                if new_due_date_str:
                    try:
                        new_due_date = datetime.strptime(new_due_date_str, "%Y-%m-%d")
                        task['due_date'] = new_due_date.strftime("%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format. Skipping date update.")
                
                save_tasks()
                print("Task updated successfully!")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a valid number for task index.")
    else:
        print("No tasks available.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_index = int(input("Enter the index of the task to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                save_tasks()
                print(f"Task '{deleted_task['title']}' deleted successfully!")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a valid number for task index.")
    else:
        print("No tasks available.")

def main():
    global tasks
    tasks = load_tasks()
    
    while True:
        print("\nInteractive Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()