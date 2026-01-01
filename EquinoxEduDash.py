"""Equinox Edu DashBoard"""

separator = "==================================\n"
tasks = []
grades = []


# Create Display Tasks function that also allows the user to add tasks if he wants to
def display_tasks():
    while True:
        try:
            choice_tasks = int(
                input("""\n
1 - Display Tasks
2 - Add Tasks
3 - Main Menu
->  """).strip()
            )
        except ValueError:
            print(separator)
            print("ERROR: Write a Number!!!!\n")
            print(separator)
            continue
        print(separator)
        if choice_tasks == 1:
            if not tasks:
                print("You don't have any tasks.\n")
            else:
                tasks.sort()
                print("This are your current tasks:")
                for priority, new_task in tasks:
                    print(f"[{priority}] - {new_task}\n")
                print("\n")
                print(separator)
        elif choice_tasks == 2:
            new_task = input("Write your new task -> ").strip()
            print("\n")
            while True:
                try:
                    priority = int(
                        input(
                            "Write the Priority for the Task (1 = High, 2 = Medium, 3 = Low) -> "
                        ).strip()
                    )
                    if priority == 0 or priority > 3:
                        print("\nERROR: Invalid Option. Select 1, 2, or 3!!!\n")
                        continue
                    tasks.append([priority, new_task])
                    print("\n")
                    break
                except ValueError:
                    print("\nERROR: Invalid Option. Select 1, 2, or 3!!!\n")
                    continue

        elif choice_tasks == 3:
            break
        else:
            print("ERROR: Select 1, 2, or 3!!!")


# Create a grade_tracker function to let the user add his grades and display them
def grade_tracker():
    while True:
        try:
            choice_grades = int(
                input("""\n
1 - Display Grades
2 - Add Grades
3 - Main Menu
->  """).strip()
            )
        except ValueError:
            print(separator)
            print("ERROR: Write a Number!!!!\n")
            print(separator)
            continue

        if choice_grades == 1:
            while True:
                try:
                    grades_display = int(
                        input("""\n
1 - Full View
2 - Brief View
3 - Grades Menu
->  """).strip()
                    )
                except ValueError:
                    print(separator)
                    print("ERROR: Write a Number!!!!\n")
                    print(separator)
                    continue
                if grades_display == 1:
                    if not grades:
                        print(separator)
                        print("You don't have any grades.\n")
                        print(separator)
                    else:
                        grades.sort(reverse=True)
                        print("This are your current grades:")
                        for new_grade, grade_class in grades:
                            print(f"[{new_grade}] - {grade_class}\n")
                        print("\n")
                        print(separator)
                elif grades_display == 2:
                    print("\nWork on Progress")
                elif grades_display == 3:
                    break
                else:
                    print("ERROR: Select 1, 2, or 3!!!")

        elif choice_grades == 2:
            while True:
                try:
                    new_grade = float(input("Write your new grades -> ").strip())
                except ValueError:
                    print("\nERROR: Invalid Option. You must add a Number!!!\n")
                    continue
                if new_grade < 0 or new_grade > 100:
                    print("\nERROR: Invalid Option. Insert from 0 to 100!!!\n")
                    continue
                grade_class = input("Write the Name of your Class -> ").strip()
                grades.append([new_grade, grade_class])
                print("\n")
                break

        elif choice_grades == 3:
            break
        else:
            print("ERROR: Select 1, 2, or 3!!!")


# Create Loop with Menu that handles invalid Values
while True:
    try:
        print(separator)
        choice = int(
            input("""\n====== Equinox EduDashboard ======

1 - Task Manager
2 - Grade Tracker
3 - Exit\n
->  """).strip()
        )
        if choice == 1:
            display_tasks()  # Here will be a function to display tasks
        elif choice == 2:
            grade_tracker()
        elif choice == 3:
            print("\nGoodbye and Have a Nice Day! ;)\n")
            break
        else:
            print("ERROR: Select a Valid Option!!!")
    except ValueError:
        print("\nERROR: Write a Number!!!\n")
        continue
