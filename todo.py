import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def view_tasks(tasks):
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


def get_priority():
    while True:
        p = input("Priority (H/M/L): ").strip().upper()
        if p == "H":
            return "High"
        elif p == "M":
            return "Medium"
        elif p == "L":
            return "Low"
        else:
            print("Invalid priority! Enter H, M, or L.")


def get_task_id(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def add_task(tasks):
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
        priority = get_priority()

    new_id = max((t["id"] for t in tasks), default=0) + 1

    task = {
        "id": new_id,
        "title": title,
        "completed": False,
        "deadline": deadline,
        "priority": priority
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")


def edit_task(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    view_tasks(tasks)

    task_id = get_task_id("Enter Task ID to edit: ")

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
                task["priority"] = get_priority()
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


def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    view_tasks(tasks)

    task_id = get_task_id("Enter Task ID to delete: ")

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


if __name__ == "__main__":
    tasks = load_tasks()

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
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
