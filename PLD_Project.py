import json

def display_menu():
    print(
        """
        What would you like to do?
        1. Add Contact 
        2. Edit Contact
        3. Delete Contact
        4. View Contacts
        5. Search Address Book
        6. Exit
        """
          )

def add_contact():
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    address = input("Address: ").strip()
    contact_number = input("Contact Number: ").strip()

    first_name_list.append(first_name)
    last_name_list.append(last_name)
    address_list.append(address)
    contact_number_list.append(contact_number)
    
    print("Contact has been added.")

def edit_contact():
    index = int(input("What number do you want to edit? "))

    if index < 1 or index > len(first_name_list):
        print("Invalid entry number.")
        return 
    
    first_name_list[index-1] = input("First Name: ").strip()
    last_name_list[index-1] = input("Last Name: ").strip()
    address_list[index-1] = input("Address: ").strip()
    contact_number_list[index-1] = input("Contact Number: ").strip()

    print("Contact has been edited.")

def delete_contact():
    index = int(input("What number do you want to delete? "))
    
    if index < 1 or index > len(first_name_list):
        print("Invalid entry number.")
        return 
    
    first_name_list.pop(index-1)
    last_name_list.pop(index-1)
    address_list.pop(index-1)
    contact_number_list.pop(index-1)

    print("Contact has been deleted.")

def view_contacts():
    print("List of Contacts:")

    for i in range(len(first_name_list)):
        first_name = first_name_list[i]
        last_name = last_name_list[i]
        address = address_list[i]
        contact_number = contact_number_list[i]

        print(f"{i+1}) {first_name} | {last_name} | {address} | {contact_number}")

def search(search_term, search_term_list):
    found = False

    for i, data in enumerate(search_term_list):

        if search_term.lower() == data.lower():
            first_name = first_name_list[i]
            last_name = last_name_list[i]
            address = address_list[i]
            contact_number = contact_number_list[i]
    
            print(f"{i+1}) {first_name} | {last_name} | {address} | {contact_number}")

            found = True
    
    if not found:
        print("Entry does not exist.")

def search_address_book():
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
    
        answer = input("Answer: ").strip().lower()

        if answer == "a":
            search_term = input("Enter the first name: ").strip()
            
            search(search_term, first_name_list)
            break

        elif answer == "b":
            search_term = input("Enter the last name: ").strip()
            
            search(search_term, last_name_list)
            break
            
        elif answer == "c":
            search_term = input("Enter the address to search: ").strip()

            search(search_term, address_list)
            break

        elif answer == "d":
            search_term = input("Enter the contact number to search: ").strip()
            
            search(search_term, contact_number_list)
            break

        else:
            print("Invalid input. Try again.")
            continue

def exit_program():
    quit()



try:
    with open("address_book.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    data = {
        "first names": [],
        "last names": [],
        "addresses": [],
        "contacts": []
        }

first_name_list = data["first names"]
last_name_list = data["last names"]
address_list = data["addresses"]
contact_number_list = data["contacts"]


display_menu()
option = int(input("Choose an option: "))

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

data = {
    "first names": first_name_list,
    "last names": last_name_list,
    "addresses": address_list,
    "contacts": contact_number_list
}

with open("address_book.json", "w") as file:
    json.dump(data, file)
