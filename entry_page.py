# Money Management System - Make new entry
# Designed and programmed by Mitchell Street

# Import Python modules
from colorama import Fore
import time
import pickle


# Reusable prints
spacer_print = (Fore.YELLOW + "-" * 50 + Fore.RESET)

# Open database
file = open("user_data_file.pkl", "rb")
user_data = pickle.load(file)


# New entry page
def new_entry():
    time.sleep(0.5)
    print(spacer_print)
    print(Fore.GREEN + "Make a new entry" + Fore.RESET)
    while True:
        name_entry = str(input(Fore.BLUE + "Enter user's name: " + Fore.RESET)).lower()
        if name_entry in user_data[]:
            print(name_entry + "Selected.")
            break
        else:
            print(Fore.RED + "User doesn't exist." + Fore.RESET)

    # Let user select user to edit
    selected_user = str(input("Please select a user: "))

    money_input = int(input("input here: "))

    user_data.update({selected_user: money_input})
    print(user_data)

    file = open("user_data_file.pkl", "wb")
    pickle.dump(user_data, file)
    file.close()
