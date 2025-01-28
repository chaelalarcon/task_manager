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