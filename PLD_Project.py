import json #Import json to read/write the address book as a JSON file. 
            #Ito yung ginagamit para ma-save yung laman ng address book kahit i-close program.

# Function to display the main menu of the address book
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

# Function to add a new contact to the lists
def add_contact():
    # Ask user for contact details
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    address = input("Address: ").strip()
    contact_number = input("Contact Number: ").strip()

    # Add each piece of information to its respective list
    first_name_list.append(first_name)
    last_name_list.append(last_name)
    address_list.append(address)
    contact_number_list.append(contact_number)
    
    print("Contact has been added.")

# Function to edit an existing contact
def edit_contact():
    index = int(input("What number do you want to edit? "))

    # Check if the index is valid
    if index < 1 or index > len(first_name_list):
        print("Invalid entry number.")
        return 
    
    # Update the contact information at the selected index
    first_name_list[index-1] = input("First Name: ").strip()
    last_name_list[index-1] = input("Last Name: ").strip()
    address_list[index-1] = input("Address: ").strip()
    contact_number_list[index-1] = input("Contact Number: ").strip()

    print("Contact has been edited.")

# Function to delete a contact from the lists
def delete_contact():
    index = int(input("What number do you want to delete? "))
    
    # Check if the index is valid
    if index < 1 or index > len(first_name_list):
        print("Invalid entry number.")
        return 
    
    # Remove the contact from all lists
    first_name_list.pop(index-1)
    last_name_list.pop(index-1)
    address_list.pop(index-1)
    contact_number_list.pop(index-1)

    print("Contact has been deleted.")

# Function to view all contacts
def view_contacts():
    print("List of Contacts:")

    # Loop through each contact and display their information
    for i in range(len(first_name_list)):
        first_name = first_name_list[i]
        last_name = last_name_list[i]
        address = address_list[i]
        contact_number = contact_number_list[i]

        # Print in a readable format with numbering. Dito papasok yung prettytable and shit
        print(f"{i+1}) {first_name} | {last_name} | {address} | {contact_number}")

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
    
        # Ask the user what field to search
        answer = input("Answer: ").strip().lower()

        # Call the search function with the appropriate list
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

# Pakita menu to the user
display_menu()
option = int(input("Choose an option: "))

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
    json.dump(data, file)
