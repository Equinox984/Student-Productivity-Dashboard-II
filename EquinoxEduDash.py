"""Soccer Manager Engine

The purpose of this project is to create a tool that allows soccer enthusiasts to
have all the information from soccer teams, to soccer leagues from Honduras.
"""

from module import soccer_teams

############################################################################################
# Create a function that shows the Soccer Manager Menu
# - Submenu 1: If the user selects 1, we will have a Menu with all the Soccer Leagues
# and their teams.
# It will also have a Finder, where we will have information from every team. A mini
# Wikipedia basically.
# - Submenu 2: If the user selects 2, we will show with this function every match
# available with their dates and stadiums.
# - Submenu 3: If the user selects 3, we will have a Trivia Minigame, where you need
# to select the correct option from fun facts of
# every honduran team. Then we will show the results in the display.
############################################################################################


# === MENUS ===
# Menu 1: Soccer Leagues -> Matches, Teams. Finder.
def soccer_league():
    while True:
        try:
            league_choice = int(
                input("""
--- Soccer Leagues Menu ---

[1] Honduran Leagues
[2] Honduran Teams
[3] Finder
[4] Exit

-> """).strip()
            )
            if league_choice == 1:
                honduran_leagues()
            elif league_choice == 2:
                print("\n--- Honduran Teams ---")
            elif league_choice == 3:
                print("\n--- Finder ---")
            elif league_choice == 4:
                print("Exiting...")
                break
            else:
                print(
                    "\nERROR: Invalid choice. Please select a valid option (1,2,3).\n"
                )
                continue
        except ValueError:
            print("\nERROR: Invalid input. Please enter a number.\n")
            continue


# Subfunction 1 (Belongs to Menu 1): Honduran Leagues
def honduran_leagues():
    while True:
        try:
            choice_leagues = int(
                input("""
--- Honduran Leagues ---
[1] Honduran National Professional Football League (First Division)
[2] Honduran Second Division (Ascenso League)
[3] Exit

-> """)
            )
            if choice_leagues == 1:
                print("\nShow teams from first league.")
            elif choice_leagues == 2:
                print("\nShow teams from second league.")
            elif choice_leagues == 3:
                break
            else:
                print(
                    "\nERROR: Invalid choice. Please select a valid option (1,2,3).\n"
                )
        except ValueError:
            print("\nERROR: Invalid input. Please enter a number.\n")


# Subfunction 2 (Belongs to Menu 1): Honduran Teams
# Subfunction 3 (Belongs to Menu 1): Finder


# Menu 2: Matches with Dates & Stadium Names Menu
# Menu 3: Trivia Minigame


# Main Menu: User selects one of the following options.
def main_menu():
    while True:
        try:
            main_choice = int(
                input("""
===== Welcome to the Soccer Manager =====

[1] Soccer Leagues
[2] Matches
[3] Trivia Minigame
[4] Exit

-> """).strip()
            )
        except ValueError:
            print("\nERROR: Invalid input. Please enter a valid option.\n")
            continue

        if main_choice == 1:
            soccer_league()
        elif main_choice == 2:
            print("\n--- Matches Menu ---")
        elif main_choice == 3:
            print("\n--- Trivia Minigame ---")
        elif main_choice == 4:
            break
        else:
            print("\nERROR: Invalid option. Select 1, 2, 3, or 4!!!\n")
            continue


main_menu()
