#!/usr/bin/python
"""a module that carries a to do list """

tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        if tasks:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        else:
            print("No tasks yet.")
    elif choice == "3":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        num = int(input("Task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task completed!")
        else:
            print("Invalid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

