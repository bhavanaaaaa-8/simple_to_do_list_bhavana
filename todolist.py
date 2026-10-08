tasks = []
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n===== YOUR TASKS =====")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def update_task():
    view_tasks()
    if tasks:
        try:
            number = int(input("Enter task number to update: "))
            if 1 <= number <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[number - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def remove_task():
    view_tasks()
    if tasks:
        try:
            number = int(input("Enter task number to remove: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        remove_task()

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid menu choice. Please enter a number from 1 to 5.")
