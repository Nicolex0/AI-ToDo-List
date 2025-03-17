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
    tasks = pd.concat([tasks, pd.DataFrame([{"Task": task, "Deadline": deadline, "Priority": priority}])], ignore_index=True)
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

    print("\n Your To-Do List (Sorted by Urgency):")
    print(tasks[["Task", "Deadline", "Priority", "Days Left"]])
    print("\n")

def prioritize_tasks(tasks):
    if tasks.empty:
        print("\nNo tasks to prioritize")
        return tasks
    
    tasks["Deadline"] = pd.to_datetime(tasks["Deadline"])
    tasks = tasks.sort_values(by=["Deadline", "Priority"], ascending=[True, False])

    return tasks

def main():
    while True:
        print("\n To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice =="3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
        main()