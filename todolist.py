
choice = int(input("1 for adding/updating tasks\n2 for reading tasks: "))

with open("todo.txt", "a+") as fobj:
    if choice == 1:
        x = input("Enter what you want to add: ")
        fobj.writelines(x+"\n")
        print(f"{x} added successfully")
    elif choice == 2:
        print("Your added tasks are:\n")
        fobj.seek(0)
        tasks = fobj.read()
        print(tasks)
    else:
        print("Invalid choice")
