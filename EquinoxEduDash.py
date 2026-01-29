"""Equinox EduDashboard"""

# MODULES
import random

from data_quotes import quotes

# UTILITIES
separator = "==================================\n"
tasks = []
grades = []

empty_task = """
=========================================
====== You don't have any tasks!!! ======
-----------------------------------------\n"""

empty_grades = """
=========================================
====== You don't have any grades!!! =====
-----------------------------------------\n"""


# TASK MANAGER FUNCTIONALITY
def task_manager():
    while True:
        try:
            choice_tasks = int(
                input("""
========================================
===== Welcome to the Task Manager! =====
----------------------------------------

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

        # User's Decision on Menu
        if choice_tasks == 1:
            task_statistics()
        elif choice_tasks == 2:
            display_tasks()
        elif choice_tasks == 3:
            add_tasks()
        elif choice_tasks == 4:
            break
        else:
            print("ERROR: Select 1, 2, 3, or 4!!!")


# FUNCTION 1 (TASK STATISTICS)
def task_statistics():
    if not tasks:
        print(empty_task)
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


# FUNCTION 2 (DISPLAY TASKS)
def display_tasks():
    if not tasks:
        print(empty_task)
    else:
        tasks.sort()
        print("This are your current tasks:")
        for priority, new_task in tasks:
            print(f"[{priority}] - {new_task}\n")
        print("\n")
        print(separator)


# FUNCTION 3 (ADD TASKS)
def add_tasks():
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


# GRADE TRACKER FUNCTIONALITY
def grade_tracker():
    while True:
        try:
            choice_grades = int(
                input("""\n
=========================================
===== Welcome to the Grade Tracker! =====
-----------------------------------------

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

        # User's Decision on Menu
        if choice_grades == 1:
            display_grades()
        elif choice_grades == 2:
            add_grades()
        elif choice_grades == 3:
            break


# FUNCTION 1 (DISPLAY GRADES)
def display_grades():
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
            full_view_grades()

        # Brief View for Quick Glances to Statistics
        elif grades_display == 2:
            brief_view_menu()

        # Return to Grades Menu
        elif grades_display == 3:
            break
        else:
            print("ERROR: Select 1, 2, or 3!!!")


# FUNCTION 1.1 (FULL VIEW GRADES MENU)
def full_view_grades():
    if not grades:
        print(empty_grades)
    else:
        grades.sort(reverse=True)
        print("\nThis are your current grades:")
        for new_grade, grade_class in grades:
            print(f"[{new_grade}] - {grade_class}\n")
        print("\n")
        print(separator)


# FUNCTION 1.2 (BRIEF VIEW MENU)
def brief_view_menu():
    if not grades:
        print(empty_grades)
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


# FUNCTION 2 (ADD GRADES)
def add_grades():
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


# WELCOME MENU
while True:
    try:
        choice = int(
            input("""
==================================
====== Equinox EduDashboard ======
----------------------------------

1 - Task Manager
2 - Grade Tracker
3 - Exit\n
->  """).strip()
        )

        # Submenus
        if choice == 1:
            task_manager()
        elif choice == 2:
            grade_tracker()
        # Quotes Functionality on Exit using random module
        elif choice == 3:
            print("\n")
            print(f"\n{random.choice(quotes)}")
            print("\n====== Goodbye and Have a Nice Day! ;) ======\n")
            break
        else:
            print("ERROR: Select a Valid Option!!!")
    except ValueError:
        print("\nERROR: Write a Number!!!\n")
        continue
