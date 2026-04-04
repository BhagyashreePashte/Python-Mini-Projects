def task():
    tasks = []  # Initialize an empty list
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    try:
        total_task = int(input("Enter how many tasks you want to add = "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Adding initial tasks
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
        

    print("\nToday's tasks are:")
    for t in tasks:
        print("-", t)

    # Menu loop
    while True:
        try:
            operation = int(input("\nEnter:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\nChoose option = "))

            if operation == 1:
                add = input("Enter task you want to add = ")
                tasks.append(add)
                print(f"Task '{add}' added successfully.")

            elif operation == 2:
                updated_val = input("Enter the task name you want to update = ")
                if updated_val in tasks:
                    up = input("Enter new task = ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Task updated successfully.")
                else:
                    print("Task not found.")

            elif operation == 3:
                del_val = input("Enter task you want to delete = ")
                if del_val in tasks:
                    tasks.remove(del_val)
                    print(f"Task '{del_val}' deleted successfully.")
                else:
                    print("Task not found.")

            elif operation == 4:
                if tasks:
                    print("\nYour Tasks:")
                    for t in tasks:
                        print("-", t)
                else:
                    print("No tasks available.")

            elif operation == 5:
                print("Closing the program...")
                break

            else:
                print("Invalid choice. Enter number between 1 to 5.")

        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the program
task()