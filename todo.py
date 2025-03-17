import pandas as pd
from datetime import datetime

TASKS_FILE = "tasks.csv" 

def load_tasks():
    try:
        return pd.read_csv(TASKS_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Task", "Deadline", "Priority"])
    
def save_tasks(tasks):
    tasks.to_csv(TASKS_FILE, index=False)
    
def add_task():
    task = input("Enter task description:")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    priority = int(input("Enter priority (1-5, where 5 is highest): "))

    tasks = load_tasks()
    tasks = tasks.append({"Task": task, "Deadline": deadline, "Priority": priority}, ignore_index=True)
    save_tasks(tasks)
    print("Task added successfully!\n\n")

def view_tasks():
    tasks = load_tasks()
    if tasks.empty:
        print("No tasks found. Add a task to get started!\n")
        return
    
    tasks["Deadline"] = pd.to_datetime(tasks["Deadline"])
    tasks["Days Left"] = (tasks["Deadline"] - datetime.now()).dt.days

    tasks["Urgency"] = tasks["Priority"] / (tasks["Days Left"] + 1)
    tasks = tasks.sort_values(by="Urgency", ascending=False)

    print("\n Yout To-Do List (Sorted by Urgency):")
    print(tasks[["Task", "Deadline", "Priority", "Days Left"]])
    print("\n")