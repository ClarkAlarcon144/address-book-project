
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
import re

colorama.init(autoreset=True, convert=True)

def check_valid_name(name):
    if re.fullmatch(r"[A-Za-z\-\' ]+", name):
        return True
    else:
        print("Invalid input. Please use only letters, hyphens, or apostrophes.")

def check_valid_contact_number(contact_number, valid_lenght=11):
    contact_number = contact_number.replace(" ", "")
    if contact_number.isdigit() and len(contact_number) == valid_lenght:
        return True
    else:
        print("Invalid format. Please enter an 11-digit mobile number (e.g., 09123456789).")

def check_valid_address(address):
    if address:
        return True
    else:
        print("Address cannot be empty.")

def check_valid_index(index, max_len=None):
    if max_len is None:
        max_len = len(address_book)

    try:
        index = int(index)

        if index < 1 or index > max_len:
            print(f"Invalid entry number. There are curretnly {max_len} entries.")
            return
        
        return True
    
    except ValueError:
        print("\nInvalid input. Please enter a number.\n")

def check_valid_multiple_choice(choice):
    valid_choices = ['a','b','c','d']

    if choice.lower() in valid_choices:
        return True
    else:
        print("Invalid answer. Only letters a, b, c, and d are accepted.")

def input_or_cancel(input_prompt, validity_check, cancel_message, allow_blank=False):
    while True:
        value = input(input_prompt).strip()

        if value.lower() == "q":
            print(cancel_message)
            return None
        
        if allow_blank and value == "":
            return "unchanged"

        if validity_check is not None:
            if validity_check(value):
                return value
            else:
                continue

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

def save_address_book(address_book):
    data = address_book

    with open("address_book.json", "w") as file:
        json.dump(data, file, indent=4)

def display_table_of_contacts(address_book):
    table = PrettyTable()
    table.border = True
    table.header = True
    table.hrules = True

    table.field_names = [
        f"{Fore.CYAN}No.{Style.RESET_ALL}",
        f"{Fore.LIGHTBLUE_EX}First Name{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}Last Name{Style.RESET_ALL}",
        f"{Fore.LIGHTYELLOW_EX}Address{Style.RESET_ALL}",
        f"{Fore.LIGHTRED_EX}Contact Number{Style.RESET_ALL}"
        ]

    for i, contact in enumerate(address_book):
        index_num = str(contact.get("original_index", i+1))

        table.add_row(
            [
            Fore.CYAN + index_num + Style.RESET_ALL,
            Fore.LIGHTBLUE_EX + contact["first_name"] + Style.RESET_ALL,
            Fore.LIGHTGREEN_EX + contact["last_name"] + Style.RESET_ALL,
            Fore.YELLOW + contact["address"] + Style.RESET_ALL,
            Fore.LIGHTRED_EX + contact["contact_number"] + Style.RESET_ALL
            ]
        )

    print(table)

def view_contacts(address_book):
    if not address_book:
        print("\nAddress book is empty.")
        return None

    print(f"\nList of Contacts (total of {len(address_book)}):")
    
    display_table_of_contacts(address_book)

    return True

def add_contact(address_book, max_contacts=100):
    if len(address_book) == max_contacts:
        print("Address book is full. Only a maximum of 100 entries are allowed.")
        return

    print("Press (q) at any time to cancel operation.")
    
    first_name = input_or_cancel("First Name: ", check_valid_name, "Add contact cancelled.")
    if first_name is None:
        return
    
    last_name = input_or_cancel("Last Name: ", check_valid_name, "Add contact cancelled.")
    if last_name is None:
        return
        
    address = input_or_cancel("Address: ", check_valid_address ,"Add contact cancelled.")
    if address is None:
        return
    
    contact_number = input_or_cancel("Contact Number: ", check_valid_contact_number,"Add contact cancelled.")
    if contact_number is None:
        return

    first_name = first_name.title()
    last_name = last_name.title()
    contact_number =  contact_number.replace(" ", "")

    contact = create_contact(first_name, last_name, address, contact_number)
    
    address_book.append(contact)

    save_address_book(address_book)

    print("\nContact has been added.")

def edit_contact(address_book):
    if not address_book:
        print("\nAddress book is empty.")
        return
    
    view_contacts(address_book)

    print("\nEnter (q) at any time to cancel the operation.")

    index = input_or_cancel("What number do you want to edit? ", check_valid_index, "Edit contact cancelled.")
    if index is None:
        return

    old_contact = address_book[index-1]

    print("\nInput blank space to keep the information as is.\n")
    
    first_name = input_or_cancel(

        f"First Name ({old_contact['first_name']}): ", 
        check_valid_name, 
        "Edit contact cancelled.", 
        allow_blank=True

        )
    
    if first_name is None:
        return
    if first_name == "unchanged":
        first_name = old_contact["first_name"]

    last_name = input_or_cancel(

        f"Last Name ({old_contact['last_name']}): ", 
        check_valid_name, 
        "Edit contact cancelled.", 
        allow_blank=True

        )
    
    if last_name is None:
        return
    if last_name == "unchanged":
        last_name = old_contact["last_name"]

    address = input_or_cancel(

        f"Address ({old_contact['address']}): ", 
        check_valid_address, 
        "Edit contact cancelled.", 
        allow_blank=True

        )
    
    if address is None:
        return
    if address == "unchanged":
        address = old_contact["address"]
 
    contact_number = input_or_cancel(

        f"Contact Number ({old_contact['contact_number']}): ", 
        check_valid_contact_number, 
        "Edit contact cancelled.",
        allow_blank=True

        )
    
    if contact_number is None:
        return
    if contact_number == "unchanged":
        contact_number = old_contact["contact_number"]


    new_contact = create_contact(

        first_name.title(), 
        last_name.title(), 
        address, 
        contact_number.replace(" ", "")

        )

    address_book[index-1] = new_contact

    save_address_book(address_book)

    print("\nContact has been edited.")

def delete_contact(address_book):
    if not address_book:
        print("\nAddress book is empty.")
        return
    
    view_contacts(address_book)

    print("\nPress (q) at any time to cancel operation.")
    
    index = input_or_cancel("What number do you want to delete? ", check_valid_index, "Delete contact cancelled.")
    if index is None:
        return

    confirm = input("\nAre you sure you want to delete this contact? (y/n): ").lower()
    if confirm != "y":
        print("\nDelete cancelled.")
        return

    address_book.pop(int(index)-1)

    save_address_book(address_book)

    print("\nContact has been deleted.")

def search(search_term, category):
    found = False 

    searched_contacts_list = []

    for i, contact in enumerate(address_book):
        if str(search_term).lower().replace(" ", "") in str(contact[category]).lower().replace(" ", ""):
            result = contact.copy()
            result["original_index"] = i + 1

            searched_contacts_list.append(result)

            found = True

    if found:
        return searched_contacts_list

    if not found:
        print("\nEntry does not exist.")

def search_address_book(address_book):
    print("\nPress (q) at any time to cancel operation.")

    print(
f"""
{Fore.LIGHTCYAN_EX}How do you want to search the address book?
{Fore.LIGHTRED_EX}(a) by first name
{Fore.LIGHTGREEN_EX}(b) by last name
{Fore.YELLOW}(c) by address
{Fore.LIGHTMAGENTA_EX}(d) by contact number
"""
)
    
    answer = input_or_cancel("Answer: ", check_valid_multiple_choice, "Search cancelled.")
    if answer is None:
        return

    if answer == "a":
        search_term = input_or_cancel("Enter the first name: ", check_valid_name, "Search cancelled.")
        if search_term is None:
            return
        searched_contacts_list = search(search_term, "first_name")

    elif answer == "b":
        search_term = input_or_cancel("Enter the last name: ", check_valid_name, "Search cancelled.")
        if search_term is None:
            return
        searched_contacts_list = search(search_term, "last_name")

    elif answer == "c":
        search_term = input_or_cancel("Enter the address to search: ", check_valid_address, "Search cancelled.")
        if search_term is None:
            return
        searched_contacts_list = search(search_term, "address")
        
    elif answer == "d":
        search_term = input_or_cancel("Enter the contact number to search: ", check_valid_contact_number,"Search cancelled.")
        if search_term is None:
            return
        searched_contacts_list = search(search_term, "contact_number")

    if searched_contacts_list is not None:
        display_table_of_contacts(searched_contacts_list)
        return searched_contacts_list

def exit_program():
    save_address_book(address_book)
    print("All changes have been saved.")
    sys.exit()

def sort_contacts(address_book):
    print(f"""
Sort contacts by:
    (a) First Name (A-Z)
    (b) First Name (Z-A)
    (c) Last Name (A-Z)
    (d) Last Name (Z-A)
""")

    choice = input_or_cancel("Choice: ", check_valid_multiple_choice, "Sort contact cancelled.")
    if choice is None:
        return
    
    choice = choice.lower()

    if choice == "a":
        address_book.sort(key=lambda contact: contact["first_name"].lower())

    elif choice == "b":
        address_book.sort(key=lambda contact: contact["first_name"].lower(), reverse=True)
    
    elif choice == "c":
        address_book.sort(key=lambda contact: contact["last_name"].lower())
    
    elif choice == "d":
        address_book.sort(key=lambda contact: contact["last_name"].lower(), reverse=True)
    
    save_address_book(address_book)

    print("\nContacts sorted.")

# ----------- Main Program Starts Here -----------


try:
    with open("address_book.json", "r") as file:
        data = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
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
        add_contact(address_book)

    elif option == 2:
        edit_contact(address_book)

    elif option == 3:
        delete_contact(address_book)

    elif option == 4:
        if view_contacts(address_book) is not None:
            choice = input("\nSort the contacts? (y/n) ").lower()

            while choice == "y":
                sort_contacts(address_book)
                view_contacts(address_book)
                choice = input("\nSort the contacts? (y/n) ").lower()

    elif option == 5:
        if view_contacts(address_book):
            choice = "y"

            while choice == "y":
                searched_contacts_list = search_address_book(address_book)

                if searched_contacts_list is not None:
                    sort_choice = input("\nSort the searched contacts? (y/n)\n(Sorting searched contacts is purely for convenience and does not change the original indices)\n").lower()

                    while sort_choice == "y":
                        sort_contacts(searched_contacts_list)
                        view_contacts(searched_contacts_list)
                        sort_choice = input("\nSort the searched contacts? (y/n) ").lower()
                    
                    choice = input("\nSearch again? (y/n) ")

    elif option == 6:
        exit_program()
    
    input("\nEnter any key to show menu again. ")
