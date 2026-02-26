"""Equinox EduDashboard"""

# MODULES
import random

from data_quotes import quotes
from utilities import (
    edudash_menu,
    empty_grades,
    empty_task,
    grademan_menu,
    separator,
    taskman_menu,
)


# TASK MANAGER FUNCTIONALITY
def task_manager(task_list):
    while True:
        try:
            choice_tasks = int(input(taskman_menu).strip())
        except ValueError:
            print(separator)
            print("ERROR: Write a Number!!!!\n")
            print(separator)
            continue
        print("\n")

        # User's Decision on Menu
        if choice_tasks == 1:
            task_statistics(task_list)
        elif choice_tasks == 2:
            display_tasks(task_list)
        elif choice_tasks == 3:
            add_tasks(task_list)
        elif choice_tasks == 4:
            break
        else:
            print("ERROR: Select 1, 2, 3, or 4!!!")


# FUNCTION 1 (TASK STATISTICS)
def task_statistics(task_list):
    if not task_list:
        print(empty_task)
    else:
        hig_priority = 0
        med_priority = 0
        low_priority = 0
        for task in task_list:
            match task["priority"]:
                case 1:
                    hig_priority += 1
                case 2:
                    med_priority += 1
                case 3:
                    low_priority += 1
                case _:
                    pass

        print("\n+--------------------------------------------------+")
        print("|                                                  |")
        print("|               TASK STATISTICS                    |")
        print("|                                                  |")
        print("+==================================================+")
        print(f"|  Total Tasks: {len(task_list):<34} |")
        print("+--------------------------------------------------+")
        print(f"|  [1] High Priority:   {hig_priority:<26} |")
        print(f"|  [2] Medium Priority: {med_priority:<26} |")
        print(f"|  [3] Low Priority:    {low_priority:<26} |")
        print("+--------------------------------------------------+\n")


# FUNCTION 2 (DISPLAY TASKS)
def display_tasks(task_list):
    if not task_list:
        print(empty_task)
    else:
        task_list.sort(key=lambda x: x["priority"])
        print("\n+--------------------------------------------------+")
        print("|                                                  |")
        print("|               YOUR CURRENT TASKS                 |")
        print("|                                                  |")
        print("+==================================================+\n")
        for task in task_list:
            priority_label = {1: "HIGH", 2: "MED", 3: "LOW"}[task["priority"]]
            print(f"  [{task['priority']}] {priority_label:4} | {task['task']}")
        print("\n+--------------------------------------------------+\n")


# FUNCTION 3 (ADD TASKS)
def add_tasks(task_list):
    new_task = input("Write your new task ->>> ").strip()
    print("\n")
    while True:
        try:
            priority = int(
                input(
                    "Write the Priority for the Task (1 = High, 2 = Medium, 3 = Low) ->>> "
                ).strip()
            )
            if priority < 1 or priority > 3:
                print("\nERROR: Invalid Option. Select 1, 2, or 3!!!\n")
                continue
            task_list.append({"priority": priority, "task": new_task})
            print("\n")
            break
        except ValueError:
            print("\nERROR: Invalid Option. Select 1, 2, or 3!!!\n")
            continue


# GRADE TRACKER FUNCTIONALITY
def grade_tracker(grade_list):
    while True:
        try:
            choice_grades = int(input(grademan_menu).strip())
        except ValueError:
            print(separator)
            print("ERROR: Write a Number!!!!\n")
            print(separator)
            continue
        print("\n")

        # User's Decision on Menu
        if choice_grades == 1:
            display_grades(grade_list)
        elif choice_grades == 2:
            add_grades(grade_list)
        elif choice_grades == 3:
            break


# FUNCTION 1 (DISPLAY GRADES)
def display_grades(grade_list):
    while True:
        try:
            grades_display = int(
                input("""
+--------------------------------------------------+
|                                                  |
|    [1] Full View                                 |
|    [2] Brief View                                |
|    [3] Grades Menu                               |
|                                                  |
+--------------------------------------------------+

->  """).strip()
            )
        except ValueError:
            print(separator)
            print("ERROR: Write a Number!!!!\n")
            print(separator)
            continue

        # Full View Menu for Grades and their Classes
        if grades_display == 1:
            full_view_grades(grade_list)

        # Brief View for Quick Glances to Statistics
        elif grades_display == 2:
            brief_view_menu(grade_list)

        # Return to Grades Menu
        elif grades_display == 3:
            break
        else:
            print("ERROR: Select 1, 2, or 3!!!")


# FUNCTION 1.1 (FULL VIEW GRADES MENU)
def full_view_grades(grade_list):
    if not grade_list:
        print(empty_grades)
    else:
        grade_list.sort(key=lambda x: x["grade"], reverse=True)
        print("\n+--------------------------------------------------+")
        print("|                                                  |")
        print("|              YOUR CURRENT GRADES                 |")
        print("|                                                  |")
        print("+==================================================+\n")
        for grade in grade_list:
            print(f"  [{grade['grade']:>6.2f}] {grade['class']}")
        print("\n+--------------------------------------------------+\n")


# FUNCTION 1.2 (BRIEF VIEW MENU)
def brief_view_menu(grade_list):
    if not grade_list:
        print(empty_grades)
    else:
        only_numbers = [grade["grade"] for grade in grade_list]

        total_grades = sum(only_numbers)
        average = total_grades / len(grade_list)
        max_value = max(only_numbers)
        min_value = min(only_numbers)

        print("\n+--------------------------------------------------+")
        print("|                                                  |")
        print("|              GRADE STATISTICS                    |")
        print("|                                                  |")
        print("+==================================================+")
        print(f"  Average Grade:  {average:>6.2f}                  ")
        print(f"  Highest Grade:  {max_value:>6.2f}                ")
        print(f"  Lowest Grade:   {min_value:>6.2f}                ")
        print("+--------------------------------------------------+\n")


# FUNCTION 2 (ADD GRADES)
def add_grades(grade_list):
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
        grade_list.append({"grade": new_grade, "class": grade_class})
        print("\n")
        break


# WELCOME MENU
def main():
    tasks = []
    grades = []

    while True:
        try:
            choice = int(input(edudash_menu).strip())

            # Submenus
            if choice == 1:
                task_manager(tasks)
            elif choice == 2:
                grade_tracker(grades)
            # Quotes Functionality on Exit using random module
            elif choice == 3:
                quote = random.choice(quotes)
                print("\n        ===== QUOTE OF THE SESSION =====         ")
                print(f"\n{quote}\n")
                print("\n+==================================================+")
                print("|                                                  |")
                print("|         Goodbye and Have a Nice Day! ;)          |")
                print("|                                                  |")
                print("+==================================================+\n")
                break
            else:
                print("ERROR: Select a Valid Option!!!")
        except ValueError:
            print("\nERROR: Write a Number!!!\n")
            continue


main()
