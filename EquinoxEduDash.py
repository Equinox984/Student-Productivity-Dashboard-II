"""Equinox Edu DashBoard"""

# Lists and Modules
import random

# We Make the Quotes List Module to Avoid Bloat on the Main Program
from data_quotes import quotes

separator = "==================================\n"
tasks = []
grades = []


# Create Display Tasks function that also allows the user to add tasks if he wants to
def display_tasks():
    while True:
        try:
            choice_tasks = int(
                input("""
========================================
===== Welcome to the Task Manager! =====

1 - Task Statistics
2 - Display Tasks
3 - Add Tasks
4 - Main Menu\n
->  """).strip()
            )
        except ValueError:
            print(separator)
            print("ERROR: Write a Number!!!!\n")
            print(separator)
            continue
        print("\n")
        # Task Statistics Menu
        if choice_tasks == 1:
            if not tasks:
                print("You don't have any tasks.\n")
                print(separator)
            else:
                hig_priority = 0
                med_priority = 0
                low_priority = 0
                print(f"You have [{len(tasks)}] task(s).")
                for priority, new_task in tasks:
                    match priority:
                        case 1:
                            hig_priority += 1
                        case 2:
                            med_priority += 1
                        case 3:
                            low_priority += 1
                        case _:
                            pass
                print(f"""
You have [{hig_priority}] high priority task(s).

You have [{med_priority}] medium priority task(s).

You have [{low_priority}] low priority task(s).\n""")
                print(separator)

        # Display Tasks Menu
        elif choice_tasks == 2:
            if not tasks:
                print("You don't have any tasks.\n")
            else:
                tasks.sort()
                print("This are your current tasks:")
                for priority, new_task in tasks:
                    print(f"[{priority}] - {new_task}\n")
                print("\n")
                print(separator)

        # Add Tasks Menu With Priority
        elif choice_tasks == 3:
            new_task = input("Write your new task ->>> ").strip()
            print("\n")
            while True:
                try:
                    priority = int(
                        input(
                            "Write the Priority for the Task (1 = High, 2 = Medium, 3 = Low) ->>> "
                        ).strip()
                    )
                    if priority <= 0 or priority > 3:
                        print("\nERROR: Invalid Option. Select 1, 2, or 3!!!\n")
                        continue
                    tasks.append([priority, new_task])
                    print("\n")
                    break
                except ValueError:
                    print("\nERROR: Invalid Option. Select 1, 2, or 3!!!\n")
                    continue

        # Return to Main Menu
        elif choice_tasks == 4:
            break
        else:
            print("ERROR: Select 1, 2, 3, or 4!!!")


# Create a grade_tracker function to let the user add his grades and display them
def grade_tracker():
    while True:
        try:
            choice_grades = int(
                input("""\n
=========================================
===== Welcome to the Grade Tracker! =====

1 - Display Grades
2 - Add Grades
3 - Main Menu\n
->  """).strip()
            )
        except ValueError:
            print(separator)
            print("ERROR: Write a Number!!!!\n")
            print(separator)
            continue
        print("\n")

        # Display Grades Menu
        if choice_grades == 1:
            while True:
                try:
                    grades_display = int(
                        input("""\n
1 - Full View
2 - Brief View
3 - Grades Menu\n
->  """).strip()
                    )
                except ValueError:
                    print(separator)
                    print("ERROR: Write a Number!!!!\n")
                    print(separator)
                    continue

                # Full View Menu for Grades and their Classes
                if grades_display == 1:
                    if not grades:
                        print(separator)
                        print("You don't have any grades.\n")
                        print(separator)
                    else:
                        grades.sort(reverse=True)
                        print("\nThis are your current grades:")
                        for new_grade, grade_class in grades:
                            print(f"[{new_grade}] - {grade_class}\n")
                        print("\n")
                        print(separator)

                # Brief View for Quick Glances to Statistics
                elif grades_display == 2:
                    if not grades:
                        print(separator)
                        print("You don't have any grades.\n")
                        print(separator)
                    else:
                        only_numbers = []
                        for new_grade, grade_class in grades:
                            only_numbers.append(new_grade)

                        total_grades = sum(only_numbers)
                        average = total_grades / len(grades)
                        max_value = max(only_numbers)
                        min_value = min(only_numbers)

                        print(separator)
                        print(f"Average Grades: {average}")
                        print(f"Highest Grade: {max_value}")
                        print(f"Lowest Grade: {min_value}\n")
                        print(separator)

                # Return to Grades Menu
                elif grades_display == 3:
                    break
                else:
                    print("ERROR: Select 1, 2, or 3!!!")

        # Add Grades
        elif choice_grades == 2:
            while True:
                try:
                    new_grade = float(input("\nWrite your new grades ->>> ").strip())
                except ValueError:
                    print("\nERROR: Invalid Option. You must add a Number!!!\n")
                    continue
                if new_grade < 0 or new_grade > 100:
                    print("\nERROR: Invalid Option. Insert from 0 to 100!!!\n")
                    continue
                grade_class = input("Write the Name of your Class ->>> ").strip()
                grades.append([new_grade, grade_class])
                print("\n")
                break

        # Return to Main Menu
        elif choice_grades == 3:
            break
        else:
            print("ERROR: Select 1, 2, or 3!!!")


# Create Loop with Main Menu that Handles Invalid Values
while True:
    try:
        print(separator)
        choice = int(
            input("""====== Equinox EduDashboard ======

1 - Task Manager
2 - Grade Tracker
3 - Exit\n
->  """).strip()
        )

        # Adding the functions that we created earlier
        if choice == 1:
            display_tasks()
        elif choice == 2:
            grade_tracker()
        # Quotes Functionality on Exit using random module
        elif choice == 3:
            print(f"\n{random.choice(quotes)}")
            print("\n Goodbye and Have a Nice Day! ;)\n")
            break
        else:
            print("ERROR: Select a Valid Option!!!")
    except ValueError:
        print("\nERROR: Write a Number!!!\n")
        continue
