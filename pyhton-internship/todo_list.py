tasks = []

def view_tasks():
    if not tasks:
        print("No tasks saved.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add  2. View  3. Remove  4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter task: ").strip()
        if task:
            tasks.append(task)
            print("Task added.")
        else:
            print("Task cannot be empty.")
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        if tasks:
            try:
                number = int(input("Task number to remove: "))
                if 1 <= number <= len(tasks):
                    print("Removed:", tasks.pop(number - 1))
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a whole number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
