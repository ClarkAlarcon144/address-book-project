'''----------------------------
Address Book Project
Each function is labeled and commented.
Please intindihin niyo yung mga ginawa para gets niyo rin pag defense na.
----------------------------'''

import json #Ito yung ginagamit para ma-save yung laman ng address book kahit i-close program.
import os
import colorama  #for making the ui colorful
from colorama import Fore, Back, Style
import time
from prettytable import PrettyTable

colorama.init(autoreset=True, convert=True)

def welcome_message():
    
    message = "Hello User, Welcome to our Address Book!"
    
    for char in message:
        
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + char, end='', flush=True)
        time.sleep(0.011)
    print() 

def input_or_cancel(input_text, cancel_text):
    value = input(input_text).strip()

    if value.lower() == "q":
        print(cancel_text)
        return None
    
    return value

# Function to display the main menu of the address book
def display_menu():

    welcome_message()

    menu_options = [
        (Fore.LIGHTBLUE_EX, "What would you like to do?"),
        (Fore.LIGHTMAGENTA_EX, "1. Add Contact"),
        (Fore.LIGHTYELLOW_EX, "2. Edit Contact"),
        (Fore.LIGHTGREEN_EX, "3. Delete Contact"),
        (Fore.LIGHTBLUE_EX, "4. View Contacts"),
        (Fore.LIGHTRED_EX, "5. Search Address Book"),
        (Fore.LIGHTWHITE_EX, "6. Exit")
    ]

    for color, text in menu_options:
        print(color + text)
        time.sleep(0.08)

def save_address_book():
    # Update the data dictionary with the latest lists.
    # Kasi iniba-iba natin laman nung lists diba, 
    # kaya kailangan natin i-update yung data na ibabalik natin sa file ulit
    data = {
        "first names": first_name_list,
        "last names": last_name_list,
        "addresses": address_list,
        "contacts": contact_number_list
    }

    # Save all changes back to the JSON file.
    # I-sasave niya yung laman nung address book dun sa file,
    # para next time, ma-loload nalang ulit laman nung address book
    with open("address_book.json", "w") as file:
        json.dump(data, file, indent=4)

# Function to add a new contact to the lists
def add_contact():
    print("Press (q) at any time to cancel operation.\n")

    # Ask user for contact details
    first_name = input_or_cancel("First Name: ", "Add contact cancelled.")
    if first_name is None:
        return

    last_name = input_or_cancel("Last Name: ", "Add contact cancelled.")
    if last_name is None:
        return

    address = input_or_cancel("Address: ", "Add contact cancelled.")
    if address is None:
        return

    contact_number = input_or_cancel("Contact Number: ", "Add contact cancelled.")
    if contact_number is None:
        return
    
    # Add each piece of information to its respective list
    first_name_list.append(first_name)
    last_name_list.append(last_name)
    address_list.append(address)
    contact_number_list.append(contact_number)
    
    print("\nContact has been added.")

    save_address_book()

def view_contacts():
    print("List of Contacts:")

    # Loop through each contact and display their information
    table = PrettyTable()
    table.field_names = [
        f"{Fore.CYAN}No.{Style.RESET_ALL}",
        f"{Fore.LIGHTBLUE_EX}First Name{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}Last Name{Style.RESET_ALL}",
        f"{Fore.LIGHTYELLOW_EX}Address{Style.RESET_ALL}",
        f"{Fore.LIGHTRED_EX}Contact Number{Style.RESET_ALL}"
        ]

    for i in range(len(first_name_list)):
        table.add_row(
            [
            Fore.CYAN + str(i + 1) + Style.RESET_ALL,
            Fore.LIGHTBLUE_EX + first_name_list[i] + Style.RESET_ALL,
            Fore.LIGHTGREEN_EX + last_name_list[i] + Style.RESET_ALL,
            Fore.YELLOW + address_list[i] + Style.RESET_ALL,
            Fore.LIGHTRED_EX + contact_number_list[i] + Style.RESET_ALL
            ]
        )

    print(table)

# Function to edit an existing contact
def edit_contact():
    view_contacts()

    print("Press (q) at any time to cancel operation.\n")

    while True:
        try:
            index = input_or_cancel("What number do you want to edit? ", "Edit contact cancelled.")
            if index is None:
                return
            
            index = int(index)

            # Check if the index is valid
            if index < 1 or index > len(first_name_list):
                print("Invalid entry number.")
                continue
        
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        break

    # Update the contact information at the selected index
    first_name = input_or_cancel("First Name: ", "Edit contact cancelled.")
    if first_name is None:
        return
    
    last_name = input_or_cancel("Last Name: ", "Edit contact cancelled.")
    if last_name is None:
        return

    address = input_or_cancel("Address: ", "Edit contact cancelled.")
    if address is None:
        return

    contact_number = input_or_cancel("Contact Number: ", "Edit contact cancelled.")
    if contact_number is None:
        return
    
    #Pag tapos na mag-input ng lahat, at hindi nag-cancel yung user, then i-eedit na yung lists.
    first_name_list[index-1] = first_name
    last_name_list[index-1] = last_name
    address_list[index-1] = address
    contact_number_list[index-1] = contact_number

    print("\nContact has been edited.")

    save_address_book()
    
# Function to delete a contact from the lists
def delete_contact():
    view_contacts()

    print("Press (q) at any time to cancel operation.\n")
    
    while True:
        try:
            index = input_or_cancel("What number do you want to edit? ", "Edit contact cancelled.")
            if index is None:
                return
            
            index = int(index)
            
            # Check if the index is valid
            if index < 1 or index > len(first_name_list):
                print("Invalid entry number.")
                continue
        
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        break
    
    # Remove the contact from all lists
    first_name_list.pop(index-1)
    last_name_list.pop(index-1)
    address_list.pop(index-1)
    contact_number_list.pop(index-1)

    print("Contact has been deleted.")

    save_address_book()

# Function to search for a contact in any list
def search(search_term, search_term_list):
    found = False # Flag to check if any match is found

    # Loop through the search list and check for matches
    for i, data in enumerate(search_term_list):

        if search_term.lower() == data.lower(): # Titingnan kung may match sa list yung hinahanap mo
            # Retrieve all contact details
            first_name = first_name_list[i]
            last_name = last_name_list[i]
            address = address_list[i]
            contact_number = contact_number_list[i]
    
            # Print the found contact
            print(f"{i+1}) {first_name} | {last_name} | {address} | {contact_number}")

            found = True #Update flag

    # If no contact matched, show a message
    if not found:
        print("Entry does not exist.")

# Function to search the address book by category
def search_address_book():
    print("Press (q) at any time to cancel operation.\n")

    while True:
        print(
"""
How do you want to search the address book?
    (a) by first name
    (b) by last name
    (c) by address
    (d) by contact number

"""
)
        try:

        # Ask the user what field to search
            answer = input_or_cancel("Answer: ", "Search cancelled.")
            if answer is None:
                return
            
            answer = answer.lower()

            if answer != "a" and answer != "b" and answer != "c" and answer != "d":
                print("Invalid answer. Only letters a, b, c, and d.")
                continue
        
        except ValueError:
            print("Invalid input. Please enter a letter.")
            continue

        break
        
    # Call the search function with the appropriate list
    if answer == "a":
        search_term = input_or_cancel("Enter the first name: ", "Search cancelled.")
        if search_term is None:
            return
        
        search(search_term, first_name_list)

    elif answer == "b":
        search_term = input("Enter the last name: ").strip()
        
        search(search_term, last_name_list)
        
    elif answer == "c":
        search_term = input("Enter the address to search: ").strip()

        search(search_term, address_list)
        
    elif answer == "d":
        search_term = input("Enter the contact number to search: ").strip()
        
        search(search_term, contact_number_list)
        
# Function to exit the program
def exit_program():
    quit()


# ----------- Main Program Starts Here -----------

# Try to load existing address book, if it exists.
# Ito yung ginagamit para ma-load yung laman nung address book kahit pinatay mo program
try:
    with open("address_book.json", "r") as file:
        data = json.load(file)

# If file does not exist, create empty data structure
except FileNotFoundError:
    data = {
        "first names": [],
        "last names": [],
        "addresses": [],
        "contacts": []
        }

# Separate the JSON data into individual lists for easier access
first_name_list = data["first names"]
last_name_list = data["last names"]
address_list = data["addresses"]
contact_number_list = data["contacts"]

option = 0

while option != 6:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Pakita menu to the user
    display_menu()
    
    try:
        option = int(input(f"\nChoose an option: "))

        if option < 1 or option > 6:
            print("Invalid input. Only numbers 1-6 are allowed.")
            continue

    except ValueError:
        print("Invalid input. Please enter a number.")  
        continue

    # Call the appropriate function based on user input
    if option == 1:
        add_contact()

    elif option == 2:
        edit_contact()

    elif option == 3:
        delete_contact()

    elif option == 4:
        view_contacts()

    elif option == 5:
        search_address_book()

    elif option == 6:
        exit_program()
    
    input()

