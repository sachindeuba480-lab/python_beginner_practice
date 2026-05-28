while True:

    print("\n==== EXPENSE TRACKER ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Expense name: ")
        amount = input("Amount: ")

        with open("expenses.txt", "a") as file:
            file.write(f"{name} - Rs.{amount}\n")

        print("Expense added!")

    elif choice == "2":

        print("\n==== ALL EXPENSES ====")

        try:
            with open("expenses.txt", "r") as file:
                print(file.read())

        except FileNotFoundError:
            print("No expenses found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")