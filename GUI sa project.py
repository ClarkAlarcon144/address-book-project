import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

def save_address_book(all_contacts):
    data = all_contacts

    with open("address_book.json", "w") as file:
        json.dump(data, file, indent=4)

def match(contact, category, query):
    if query == "":
        return True

    mapping = {
        "First Name": contact["first_name"],
        "Last Name": contact["last_name"],
        "Address": contact["address"],
        "Contact No.": contact["contact_number"]
    }

    return query in mapping.get(category, "").lower()

def on_search(event=None):
    query = search_bar.get().lower()
    category = search_dropdown.get()

    filtered = []

    for contact in all_contacts:
        if match(contact, category, query):
            filtered.append(contact)

    refresh_table(filtered)

def reset_search():
    search_bar.delete(0, "end")
    search_dropdown.current(0)  # reset to default category
    refresh_table()

sort_state = {}

def sort_by(column, treeview_column):
    reverse = sort_state.get(column, False)  # get current state
    sort_state[column] = not reverse  # flip for next click

    all_contacts.sort(
        key=lambda contact: contact[column],
        reverse=reverse
    )

    refresh_table()

    # Determine arrow for clicked column
    if not reverse:
        arrow = " ▲"  
    else: 
        arrow = " ▼"

    # Set header text only for the clicked column
    text = {"first": "First Name", "last": "Last Name"}.get(treeview_column, treeview_column)
    tree.heading(treeview_column, text=text + arrow)

def refresh_table(contacts=None):
    tree.delete(*tree.get_children())

    if contacts is None:
        contacts = all_contacts

    for i, contact in enumerate(contacts, start=1):
        tree.insert("", "end", iid=contact["contact_id"], values=(
            i,   
            contact["first_name"],
            contact["last_name"],
            contact["address"],
            contact["contact_number"]
        ))

def add_contact():
    add_win = tk.Toplevel(root)
    add_win.title("Add Contact")
    add_win.geometry("800x500")
        
    tk.Label(add_win, text="First Name", font=("STSong", 20)).pack(pady=5)
    first_entry = tk.Entry(add_win, font=("STSong", 20))
    first_entry.pack(pady=5)

    tk.Label(add_win, text="Last Name", font=("STSong", 20)).pack(pady=5)
    last_entry = tk.Entry(add_win, font=("STSong", 20))
    last_entry.pack(pady=5)

    tk.Label(add_win, text="Address", font=("STSong", 20)).pack(pady=5)
    address_entry = tk.Entry(add_win, font=("STSong", 20))
    address_entry.pack(pady=5)
    
    tk.Label(add_win, text="Contact Number", font=("STSong", 20)).pack(pady=5)
    contact_num_entry = tk.Entry(add_win, font=("STSong", 20))
    contact_num_entry.pack(pady=5)

    def save_contact():
        global next_id

        first = first_entry.get()
        last = last_entry.get()
        address = address_entry.get()
        contact_num = contact_num_entry.get()
        
        if not first or not last or not address or not contact_num:
            messagebox.showerror("Input Error", "All fields are required! Please fill out the entire form.")
            return
        
        contact_id = next_id
        next_id += 1
        
        new_contact = create_contact(contact_id, first, last, address, contact_num)
        
        all_contacts.append(new_contact)

        save_address_book(all_contacts)

        refresh_table()

        messagebox.showinfo("Success", "Contact Added!")
        
        add_win.destroy()
    
    tk.Button(add_win, text="Add Contact", font=(20), command=save_contact).pack(pady=5)

def edit_contact():
    selected_id = tree.focus()

    if not selected_id:
        messagebox.showerror("Error", "Please select a contact from the table to edit")
        return

    contact_id = int(selected_id)

    for contact in all_contacts:
        if contact["contact_id"] == contact_id:
            break
    
    else: # if the for loopp doesnt find a match, this will stop the whole function. Prevents crashes
        return
        
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Contact")
    edit_window.geometry("800x500")

    tk.Label(edit_window, text="First Name", font=20).pack()
    first_entry = tk.Entry(edit_window, font=20)
    first_entry.insert(0, contact["first_name"])
    first_entry.pack()

    tk.Label(edit_window, text="Last Name", font=20).pack()
    last_entry = tk.Entry(edit_window, font=20)
    last_entry.insert(0, contact["last_name"])
    last_entry.pack()

    tk.Label(edit_window, text="Address", font=20).pack()
    address_entry = tk.Entry(edit_window, font=20)
    address_entry.insert(0, contact["address"])
    address_entry.pack()

    tk.Label(edit_window, text="Contact Number", font=20).pack()
    contact_entry = tk.Entry(edit_window, font=20)
    contact_entry.insert(0, contact["contact_number"])
    contact_entry.pack()

    def save_edit():
        contact["first_name"] = first_entry.get()
        contact["last_name"] = last_entry.get()
        contact["address"] = address_entry.get()
        contact["contact_number"] = contact_entry.get()
        
        save_address_book(all_contacts)
        refresh_table()
        messagebox.showinfo("Updated", "Contact updated successfully")
        edit_window.destroy()

    tk.Button(edit_window, text="Save Changes", command=save_edit).pack()

def delete_contact():
    selected_id = tree.focus()

    if not selected_id:
        messagebox.showerror("Error", "Choose a contact from the table to delete")
        return

    contact_id = int(selected_id)

    for i, contact in enumerate(all_contacts):
        if contact_id == contact["contact_id"]:
            name = f"{contact['first_name']} {contact['last_name']}"
            break
    
    else:
        return

    if messagebox.askyesno("Delete Contact?", f"Are you sure you want to delete {name}?"):
        all_contacts.pop(i)
        save_address_book(all_contacts)
        refresh_table()

def on_double_click(event):
    selected = tree.selection()  # get selected rows
    if selected:  # only proceed if a row is actually selected
        edit_contact()

def create_contact(contact_id, first_name, last_name, address, contact_number):
        return {
            "contact_id": contact_id,
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "contact_number": contact_number
        }



try:
    with open("address_book.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

all_contacts = data  # Keep the loaded contacts

# next_id for new contacts
if all_contacts:
    next_id = max(c["contact_id"] for c in all_contacts) + 1
else:
    next_id = 1

filtered_contacts = []



root = tk.Tk()
root.geometry("800x500")
root.title("Address Book")

# Title bar at the top
title = tk.Label(root, text="Address Book", font=("cascadia code", 30), bg="pink", fg="black")

# Search bar at the top below the title
search_frame = tk.Frame(root, bg="pink")

# Box before the dropdown showing "Search By: "
search_by = tk.Label(search_frame, fg="black", text="Search By:", font=("cascadia code", 20))

# The dropdown for search categories
search_dropdown = ttk.Combobox(search_frame, values=["First Name", "Last Name", "Address", "Contact No."], width=20, font=("cascadia code", 20), state="readonly")
search_dropdown.current(0)

reset_btn = tk.Button(search_frame, text="Clear", font=("cascadia code", 15), command=reset_search)

# The actual search bar where user inputs
search_bar = tk.Entry(search_frame, font=("cascadia code", 20))

# Frame containing the buttons and the table
main_frame = tk.Frame(root, bg="black")

# Buttons at side
buttons_frame = tk.Frame(main_frame, bg="pink")

# Table of contacts at the right
contacts_frame = tk.Frame(main_frame, bg="pink")

# -------------------------------
# Bindings (after widgets exist)
search_dropdown.bind("<<ComboboxSelected>>", on_search)
search_bar.bind("<KeyRelease>", on_search)

# -------------------------------
# Pack / layout at the bottom
title.pack(fill="x")
search_frame.pack(fill="x", padx=10, pady=10)
search_by.pack(side="left", padx=20, pady=10)
search_dropdown.pack(side="left", padx=5, pady=10)
reset_btn.pack(side="left", padx=5)
search_bar.pack(side="left", fill="x", expand=True, padx=5, pady=10)

main_frame.pack(fill="both", expand=True, padx=10, pady=10)
buttons_frame.pack(side="left", fill="y", padx=10, pady=10)
contacts_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

buttons = {
    "Add Contact": add_contact, 
    "Edit Contact": edit_contact,
    "Delete Contact": delete_contact
    }

for button_text, button_function in buttons.items():
    btn = tk.Button(buttons_frame, text=button_text, bg="pink", fg="black", font=("cascadia code", 15), command=lambda f=button_function: f())
    btn.pack(padx=10, pady=30)



style = ttk.Style()
style.theme_use("clam") # Necessary for custom fonts to show on headings

# 2. Configure the Heading style globally
style.configure("Treeview", font=("cascadia code", 15), rowheight=35)
style.configure("Treeview.Heading", font=("cascadia code", 12), background="pink", foreground="black")

tree = ttk.Treeview(contacts_frame, columns=("index", "first", "last", "address", "contact"), show="headings")

tree.heading("index", text="No.")
tree.heading("first", text="First Name", command=lambda: sort_by("first_name", "first"))
tree.heading("last", text="Last Name", command=lambda: sort_by("last_name", "last"))
tree.heading("address", text="Address")
tree.heading("contact", text="Contact Number")

tree.column("index", width=40, anchor="center")
tree.column("first", width=150, anchor="center")
tree.column("last", width=150, anchor="center")
tree.column("address", width=200, anchor="center")
tree.column("contact", width=150, anchor="center")

tree.bind("<Double-1>", on_double_click)

scrollbar_y = tk.Scrollbar(contacts_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar_y.set)

scrollbar_x = tk.Scrollbar(contacts_frame, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=scrollbar_x.set)

scrollbar_x.pack(side="bottom", fill="x")
scrollbar_y.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

refresh_table()

root.mainloop()


