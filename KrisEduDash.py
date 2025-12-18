"""Task Manager Tool"""

taskList = []

separator = "========================="
separator2 = "-------------------------"


def DisplayTask():
    print("\n")
    print(separator + "\nDisplaying Current Tasks\n" + separator)

    if not taskList:
        print("\nNo tasks has been added, my friend UwU.\n")
    else:
        # Python orders the first element of the tuple (Priority)
        taskList.sort()
        print("\nTasks by Priority (1=High):")

        # We use the ordered list to display the tasks
        for priority, task in taskList:
            print(f"[{priority}] - {task}\n")

    # We ask the user if they want to add a new task
    while True:
        choice = input("Do you want to add a task? (y/n): ").lower().strip()
        if choice == "y" or choice == "n":
            return choice
        else:
            print("Invalid input. Type 'y' or 'n'.")


# We ask the user to add a task and priority and saves it on the list
def AddTask():
    print(separator2)
    new_task = input("\nEnter the task description: ")

    # A loop to make sure that the priority is a valid number (1, 2, or 3)
    while True:
        try:
            priority = int(input("Enter Priority Level (1=High, 2=Medium 3=Low): "))
            if 1 <= priority <= 3:
                break
            else:
                print("Priority must be 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Enter a number.")

    # We save the task as a Tuple (Priority, Task)
    taskList.append((priority, new_task))
    print(f"Task '{new_task}' added with priority {priority}!")
    print(separator2)


# Main Program Tool
print(separator2)
print("Welcome to Edu Dashboard")
print(separator2)

while True:
    choice = input(("\n1. Task Manager\n2. Exit\n-> "))
    if choice == "1":
        addTask = DisplayTask()
        if addTask == "y":
            AddTask()
    elif choice == "2":
        break
    else:
        print("\nInvalid option. Please choose 1 or 2.\n")

print("\nExiting Task Manager. Goodbye!")
