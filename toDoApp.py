# toDoApp.py

tasks = []

def show_menu():
    print("\n==== TO-DO APP ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
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
