# Money Management System - Main Menu
# Designed and programmed by Mitchell Street

# Import Python modules
from colorama import Fore
import time

# Import other pages
import entry_page

# Reusable prints
spacer_print = (Fore.YELLOW + "-" * 50 + Fore.RESET)


# Main menu page gui
def main_menu():
    # Main menu text
    print(spacer_print)  # To separate menus
    print(Fore.GREEN + "Money Management System" + Fore.RESET)
    # Display all the different options
    print(Fore.BLUE + "[1]" + Fore.RESET + " Make a new entry")
    print(Fore.BLUE + "[2]" + Fore.RESET + " Add a new user")
    print(Fore.BLUE + "[3]" + Fore.RESET + " View user history")
    print(Fore.BLUE + "[4]" + Fore.RESET + " View existing users and status")
    print(Fore.BLUE + "[5]" + Fore.RESET + " Reset user")
    print(Fore.BLUE + "[6]" + Fore.RESET + " Exit")

    # User input and data validation for their input
    possible_menus = ["1", "2", "3", "4", "5", "6"]
    while True:  # Data validation
        choice = str(input("Selected menu: "))
        if choice in possible_menus:
            break
        else:
            print(Fore.RED + "Invalid input, please enter a number from " + Fore.BLUE +
                  "1-6" + Fore.RED + "." + Fore.RESET)

    # Route user to the appropriate menu
    if choice == "1":  # Make a new entry
        print(Fore.BLUE + "'Make a new entry' selected" + Fore.RESET)
        entry_page.new_entry()

    elif choice == "2":  # Add a new user
        print(Fore.BLUE + "'Add a new user' selected" + Fore.RESET)

    elif choice == "3":  # View user history
        print(Fore.BLUE + "'View user history' selected" + Fore.RESET)

    elif choice == "4":  # View existing users and status
        print(Fore.BLUE + "'View existing users and status' selected" + Fore.RESET)

    elif choice == "5":  # Reset user
        print(Fore.BLUE + "'Reset user' selected" + Fore.RESET)

    elif choice == "6":  # Exit the program
        print(Fore.RED + "Exiting the program..." + Fore.RESET)
        time.sleep(1)
        exit("User exit")

    else:
        print(Fore.RED + "System error, returning to main menu..." + Fore.RESET)
