tasks = []

while True:
    print("\n==== TO-DO APP ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "3":
        remove = int(input("Enter task number to remove: "))
        if 0 < remove <= len(tasks):
            tasks.pop(remove - 1)
            print("Task removed!")
        else:
            print("Invalid task number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")