# Money Management System - Main file
# Designed and programmed by Mitchell Street

# Import other pages and files
import main_menu_page

# Import Python modules
import mysql.connector

# Database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

for x in mycursor:
  print(x)

# Open main menu
# main_menu_page.main_menu()
