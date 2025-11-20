"""Task Manager Tool"""

taskList = []  # Creating an empty list to store tasks
# Define a visual separator
separator = "=================================="
separator2 = "-----------------"


def DisplayTask():
    pass


def AddTask():
    pass


# Main Program Tool
# Welcome Message
print(separator2)
print("Welcome to Edu Dash")
print(separator2)

while True:  # run forever
    selection = input(("1. Task Manager\n2. Exit\n-> "))
    if selection != "1" and selection != "2":
        print("\nInvalid option. Please choose 1 or 2.\n")
    elif selection == "1":  # If the user chooses 1 (Task Manager)
        # Display Tasks and return Y o N to addTask variable.
        addTask = DisplayTask()

        if addTask == "y":  # Check the value stored in the variable.
            # if "y" then call the AddTask() function.
            AddTask()
        else:  # if "n" go back to the main selection menu-
            continue
    else:
        break
