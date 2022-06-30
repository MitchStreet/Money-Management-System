# Money Management System - Main Menu
# Designed and programmed by Mitchell Street

# Import Python modules
from colorama import Fore, Style, Back

# Reusable prints
spacer_print = (Fore.YELLOW + "-"*50 + Fore.RESET)

# Main menu page gui
def main_menu():
    print(spacer_print)
    print("Money Management System")
    print("""
[1] Make a new entry
[2] Add a new user
[3] View user history
[4] View existing users and status
[5] Reset users
[6] Exit
    """)
