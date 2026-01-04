"""Equinox Edu DashBoard"""

import random

separator = "==================================\n"
tasks = []
grades = []
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Code is like humor. When you have to explain it, it's bad. - Cory House",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "The best error message is the one that never shows up. - Thomas Fuchs",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
    "Experience is the name everyone gives to their mistakes. - Oscar Wilde",
    "In order to be irreplaceable, one must always be different. - Coco Chanel",
    "Java is to JavaScript what car is to Carpet. - Chris Heilmann",
    "Knowledge is power. - Francis Bacon",
    "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code. - Dan Salomon",
    "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away. - Antoine de Saint-Exupery",
    "Before software can be reusable it first has to be usable. - Ralph Johnson",
    "Make it work, make it right, make it fast. - Kent Beck",
    "Simplicity is the soul of efficiency. - Austin Freeman",
    "Fix the cause, not the symptom. - Steve Maguire",
    "Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck",
    "Walking on water and developing software from a specification are easy if both are frozen. - Edward V Berard",
    "It's not a bug – it's an undocumented feature. - Anonymous",
    "The most important property of a program is whether it accomplishes the intention of its user. - C.A.R. Hoare",
]


# Create Display Tasks function that also allows the user to add tasks if he wants to
def display_tasks():
    while True:
        try:
            choice_tasks = int(
                input("""\n
1 - Task Statistics
2 - Display Tasks
3 - Add Tasks
4 - Main Menu
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
                print(separator)
            else:
                hig_priority = 0
                med_priority = 0
                low_priority = 0
                print(f"You have [{len(tasks)}] task(s).")
                for priority, new_task in tasks:
                    if priority == 1:
                        hig_priority += 1
                    elif priority == 2:
                        med_priority += 1
                    elif priority == 3:
                        low_priority += 1
                print(f"""
You have [{hig_priority}] high priority task(s).

You have [{med_priority}] medium priority task(s).

You have [{low_priority}] low priority task(s).\n""")
                print(separator)

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

        elif choice_tasks == 3:
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
                        print("\nThis are your current grades:")
                        for new_grade, grade_class in grades:
                            print(f"[{new_grade}] - {grade_class}\n")
                        print("\n")
                        print(separator)

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

                elif grades_display == 3:
                    break
                else:
                    print("ERROR: Select 1, 2, or 3!!!")

        elif choice_grades == 2:
            while True:
                try:
                    new_grade = float(input("\nWrite your new grades -> ").strip())
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
            print(f"\n{random.choice(quotes)}")
            print("\nGoodbye and Have a Nice Day! ;)\n")
            break
        else:
            print("ERROR: Select a Valid Option!!!")
    except ValueError:
        print("\nERROR: Write a Number!!!\n")
        continue
