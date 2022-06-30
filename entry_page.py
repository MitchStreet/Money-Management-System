# Money Management System - Make new entry
# Designed and programmed by Mitchell Street

# Import Python modules
from colorama import Fore
import time


# Reusable prints
spacer_print = (Fore.YELLOW + "-" * 50 + Fore.RESET)



# New entry page
def new_entry():
    time.sleep(0.5)
    print(spacer_print)
    print(Fore.GREEN + "Make a new entry" + Fore.RESET)
    while True:
        name_entry = str(input(Fore.BLUE + "Enter user's name: " + Fore.RESET)).lower()
