# toDoApp.py
# Simple To-Do Application

tasks = []

def show_menu():
    print("\n==== TO-DO APP ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def showTasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("Tasks List:")
        for i, task in enumerate(tasks, 1):  # Using enumerate for cleaner indexing
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("\nEnter the number of the task to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            t = input("Enter task: ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            n = int(input("Enter task number to remove: "))
            removetask(n)   
        elif ch == "4":
            print("Exiting...")
            break
        else:
            print("Wrong choice!")


if __name__ == "__main__":
    main()
