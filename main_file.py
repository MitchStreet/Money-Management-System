# Money Management System - Main file
# Designed and programmed by Mitchell Street

# Import other pages and files
import main_menu_page

# Import Python modules
from os.path import exists  # Used to validate file(s) existence
import pickle  # For dictionary database
from colorama import Fore

# Database for user data
# Checks if database file exists
database_exists = exists("user_data_file.pkl")

# If the database doesn't exist...
if database_exists is False:
    # Creates an empty database called "user_data" with value Temp = 0
    user_data = {}

    # Creates a .pkl file in write mode
    file = open("user_data_file.pkl", "wb")

    # Dumps the dictionary to the .pkl file
    pickle.dump(user_data, file)

    # closes
    file.close()
    print(Fore.YELLOW + "Dictionary created." + Fore.RESET)

# Open main menu
main_menu_page.main_menu()
