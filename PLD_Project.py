'''----------------------------
Address Book Project
Each function is labeled and commented.
Please intindihin niyo yung mga ginawa para gets niyo rin pag defense na.
----------------------------'''

import json
import os
import colorama 
from colorama import Fore, Style
import time
from prettytable import PrettyTable
import sys

colorama.init(autoreset=True, convert=True)


def input_or_cancel(input_prompt, cancel_message):
    value = input(input_prompt).strip()

    if value.lower() == "q":
        print(cancel_message)
        return None
    
    return value

def create_contact(first_name, last_name, address, contact_number):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "contact_number": contact_number
    }

def display_menu():
    welcome_message = "Hello User, Welcome to our Address Book!"
    
    for char in welcome_message:
        
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + char, end='', flush=True)
        time.sleep(0.011)

    print() 

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
    data = address_book

    with open("address_book.json", "w") as file:
        json.dump(data, file, indent=4)

def view_contacts():
    if not address_book:
        print("\nAddress book is empty.")
        return

    print("\nList of Contacts:")

    table = PrettyTable()

    table.field_names = [
        f"{Fore.CYAN}No.{Style.RESET_ALL}",
        f"{Fore.LIGHTBLUE_EX}First Name{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}Last Name{Style.RESET_ALL}",
        f"{Fore.LIGHTYELLOW_EX}Address{Style.RESET_ALL}",
        f"{Fore.LIGHTRED_EX}Contact Number{Style.RESET_ALL}"
        ]
    
    for i, contact in enumerate(address_book):
        table.add_row(
            [
            Fore.CYAN + str(i + 1) + Style.RESET_ALL,
            Fore.LIGHTBLUE_EX + contact["first_name"] + Style.RESET_ALL,
            Fore.LIGHTGREEN_EX + contact["last_name"] + Style.RESET_ALL,
            Fore.YELLOW + contact["address"] + Style.RESET_ALL,
            Fore.LIGHTRED_EX + contact["contact_number"] + Style.RESET_ALL
            ]
        )

    print(table)

def add_contact():
    print("Press (q) at any time to cancel operation.")

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
    
    first_name = first_name.title()
    last_name = last_name.title()

    contact = create_contact(first_name, last_name, address, contact_number)
    
    print("\nContact has been added.")
    
    address_book.append(contact)

    save_address_book()

def edit_contact():
    if not address_book:
        print("\nAddress book is empty.")
        return
    
    view_contacts()

    print("\nEnter (q) at any time to cancel operation.")

    while True:
        try:
            index = input_or_cancel("What number do you want to edit? ", "Edit contact cancelled.")
            if index is None:
                return
            
            index = int(index)

            # Check if the index is valid
            if index < 1 or index > len(address_book):
                print("Invalid entry number.")
                continue
        
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        break
    
    old_contact = address_book[index-1]

    print("\nInput blank space to keep information as is.\n")
    
    first_name = input_or_cancel(f"First Name ({old_contact["first_name"]}): ", "Edit contact cancelled.")
    if first_name is None:
        return
    
    if first_name == "":
        first_name = old_contact["first_name"]
    
    last_name = input_or_cancel(f"Last Name ({old_contact["last_name"]}): ", "Edit contact cancelled.")
    if last_name is None:
        return
    
    if last_name == "":
        last_name = old_contact["last_name"]

    address = input_or_cancel(f"Address ({old_contact["address"]}): ", "Edit contact cancelled.")
    if address is None:
        return
    
    if address == "":
        address = old_contact["address"]

    contact_number = input_or_cancel(f"Contact Number ({old_contact["contact_number"]}): ", "Edit contact cancelled.")
    if contact_number is None:
        return
    
    if contact_number == "":
        contact_number = old_contact["contact_number"]

    first_name = first_name.title()
    last_name = last_name.title()

    new_contact = create_contact(first_name, last_name, address, contact_number)

    address_book[index-1] = new_contact

    save_address_book()

    print("\nContact has been edited.")

def delete_contact():
    if not address_book:
        print("\nAddress book is empty.")
        return
    
    view_contacts()

    print("\nPress (q) at any time to cancel operation.")
    
    while True:
        try:
            index = input_or_cancel("What number do you want to delete? ", "Delete contact cancelled.")
            if index is None:
                return
            
            index = int(index)
            
            if index < 1 or index > len(address_book):
                print("Invalid entry number.")
                continue
        
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        break

    confirm = input("\nAre you sure you want to delete this contact? (y/n): ").lower()
    if confirm != "y":
        print("\nDelete cancelled.")
        return

    address_book.pop(index-1)

    save_address_book()

    print("\nContact has been deleted.")

def search(search_term, category):
    found = False 
    
    table = PrettyTable()
    
    table.field_names = [
        f"{Fore.CYAN}No.{Style.RESET_ALL}",
        f"{Fore.LIGHTBLUE_EX}First Name{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}Last Name{Style.RESET_ALL}",
        f"{Fore.LIGHTYELLOW_EX}Address{Style.RESET_ALL}",
        f"{Fore.LIGHTRED_EX}Contact Number{Style.RESET_ALL}"
        ]
    
    table.border = True
    table.header = True
    table.hrules = True

    for i, contact in enumerate(address_book):

        if search_term.lower() in contact[category].lower(): 
            first_name = contact["first_name"]
            last_name = contact["last_name"]
            address = contact["address"]
            contact_number = contact["contact_number"]

            table.add_row(
                [
                Fore.CYAN + str(i + 1) + Style.RESET_ALL,
                Fore.LIGHTBLUE_EX + first_name + Style.RESET_ALL,
                Fore.LIGHTGREEN_EX + last_name + Style.RESET_ALL,
                Fore.YELLOW + address + Style.RESET_ALL,
                Fore.LIGHTRED_EX + contact_number + Style.RESET_ALL
                ]
            )

            found = True 

    if found:
        print(table)

    if not found:
        print("\nEntry does not exist.")

def search_address_book():
    if not address_book:
        print("\nAddress book is empty.")
        return
    
    print("\nPress (q) at any time to cancel operation.")

    while True:
        print(
f"""
{Fore.LIGHTCYAN_EX}How do you want to search the address book?
    {Fore.LIGHTRED_EX}(a) by first name
    {Fore.LIGHTGREEN_EX}(b) by last name
    {Fore.YELLOW}(c) by address
    {Fore.LIGHTMAGENTA_EX}(d) by contact number

"""
)
        try:
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

    if answer == "a":
        search_term = input_or_cancel("Enter the first name: ", "Search cancelled.")
        if search_term is None:
            return
        
        search(search_term, "first_name")

    elif answer == "b":
        search_term = input_or_cancel("Enter the last name: ", "Search cancelled.")
        if search_term is None:
            return
        
        search(search_term, "last_name")
        
    elif answer == "c":
        search_term = input_or_cancel("Enter the address to search: ", "Search cancelled.")
        if search_term is None:
            return

        search(search_term, "address")
        
    elif answer == "d":
        search_term = input_or_cancel("Enter the contact number to search: ", "Search cancelled.")
        if search_term is None:
            return
        
        search(search_term, "contact_number")
 
def exit_program():
    sys.exit()

def sort_contacts():
    print(f"""
Sort contacts by:
    (a) First Name (A-Z)
    (b) First Name (Z-A)
    (c) Last Name (A-Z)
    (d) Last Name (Z-A)
""")
    
    while True:
        choice = input_or_cancel("Choice: ", "Sort contact cancelled.")

        if choice is None:
            return
        
        choice = choice.lower()

        if choice == "a":
            address_book.sort(key=lambda contact: contact["first_name"].lower())
            break

        elif choice == "b":
            address_book.sort(key=lambda contact: contact["first_name"].lower(), reverse=True)
            break
        
        elif choice == "c":
            address_book.sort(key=lambda contact: contact["last_name"].lower())
            break
        
        elif choice == "d":
            address_book.sort(key=lambda contact: contact["last_name"].lower(), reverse=True)
            break

        else:
            print("\nInvalid input. Only input letters a, b, c, and d.")
            continue
    
    print("\nContacts sorted.")



# ----------- Main Program Starts Here -----------

try:
    with open("address_book.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    data = []

address_book = data

option = 0

while option != 6:
    os.system('cls' if os.name == 'nt' else 'clear')

    display_menu()
    
    try:
        option = int(input(f"\nChoose an option: "))

        if option < 1 or option > 6:
            print("\nInvalid input. Only numbers 1-6 are allowed.")
            continue

    except ValueError:
        print("\nInvalid input. Please enter a number.")  
        continue

    if option == 1:
        add_contact()

    elif option == 2:
        edit_contact()

    elif option == 3:
        delete_contact()

    elif option == 4:
        view_contacts()
        choice = input("\nSort the contacts? (y/n) ").lower()

        while choice == "y":
            sort_contacts()
            view_contacts()
            choice = input("\nSort the contacts? (y/n) ").lower()

    elif option == 5:
        search_address_book()

    elif option == 6:
        exit_program()
    
    input("\nEnter any key to show menu again. ")

