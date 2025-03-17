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
    print("Task added successfully!")