import json

def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def view_tasks():
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        print("-" * 30)
        print(f"ID        : {task['id']}")
        print(f"Title     : {task['title']}")
        print(f"Completed : {task['completed']}")
        print(f"Deadline  : {task['deadline']}")
        print(f"Priority  : {task['priority']}")

    print("-" * 30)

def add_task():
    title = input("Enter task title: ").strip()

    while title == "":
        print("Task title cannot be empty!")
        title = input("Enter task title: ").strip()

    deadline = None
    priority = None

    more = input("Add deadline & priority? (y/n): ").strip().lower()

    while more not in ["y", "n"]:
        print("Please enter y or n.")
        more = input("Add deadline & priority? (y/n): ").strip().lower()

    if more == "y":
        deadline = input("Enter deadline: ").strip()

        while True:
            p = input("Priority (H/M/L): ").strip().upper()

            if p == "H":
                priority = "High"
                break
            elif p == "M":
                priority = "Medium"
                break
            elif p == "L":
                priority = "Low"
                break
            else:
                print("Invalid priority!")

    task = {
        "title": title,
        "completed": False,
        "deadline": deadline,
        "priority": priority
    }

    tasks = load_tasks()

    if len(tasks) == 0:
        task["id"] = 1
    else:
        task["id"] = max(task["id"] for task in tasks) + 1

    tasks.append(task)

    save_tasks(tasks)

    print("✅ Task added successfully!")

def edit_task():
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks found.")
        return

    view_tasks()

    task_id = int(input("Enter Task ID to edit: "))

    for task in tasks:
        if task["id"] == task_id:

            print("""
1. Edit Title
2. Edit Deadline
3. Edit Priority
4. Toggle Completed
5. Cancel
""")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                task["title"] = input("New title: ").strip()

            elif choice == "2":
                task["deadline"] = input("New deadline: ").strip()

            elif choice == "3":
                while True:
                    p = input("Priority (H/M/L): ").strip().upper()

                    if p == "H":
                        task["priority"] = "High"
                        break
                    elif p == "M":
                        task["priority"] = "Medium"
                        break
                    elif p == "L":
                        task["priority"] = "Low"
                        break
                    else:
                        print("Invalid priority!")

            elif choice == "4":
                task["completed"] = not task["completed"]

            elif choice == "5":
                return

            else:
                print("Invalid choice.")
                return

            save_tasks(tasks)

            print("✅ Task updated.")
            return

    print("❌ Task ID not found.")

def delete_task():
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    view_tasks()

    task_id = int(input("Enter Task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id:

            confirm = input(f"Delete '{task['title']}'? (y/n): ").strip().lower()

            if confirm == "y":
                tasks.remove(task)

                save_tasks(tasks)

                print("✅ Task deleted.")
            else:
                print("Deletion cancelled.")

            return

    print("❌ Task ID not found.")


while True:
    print("""
========== TODO ==========
1. View Tasks
2. Add Task
3. Edit Task
4. Delete Task
5. Exit
==========================
""")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        edit_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
