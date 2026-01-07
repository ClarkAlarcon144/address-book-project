import tkinter as tk              # Core GUI library
from tkinter import ttk           # Themed widgets (Treeview, Combobox)
from tkinter import messagebox    # Popup dialogs (info, warning, error)
from tkinter import font          # Font measurement for tooltip overflow
import json                       # Data storage (JSON file)
import re                         # Input validation with regex
import pandas as pd               # Excel import/export support


# ------------------ Excel Export/Import ----------------
def export_to_excel(filename="address_book.xlsx"):
    # Export all contacts to an Excel file using pandas
    if not address_book:
        messagebox.showwarning("Empty", "No contacts to export.")
        return
    
    # Convert list of dicts to DataFrame
    data_frame = pd.DataFrame(address_book)
    
    # Optional: reorder columns for readability
    data_frame = data_frame[["contact_id", "first_name", "last_name", "address", "contact_number"]]
    
    if messagebox.askyesno("Export?", "Are you sure you want to export data to an excel file? (address_book.xlsx)"):
        # Save to Excel
        try:
            data_frame.to_excel(filename, index=False)
            messagebox.showinfo("Export successful", f"Address book exported to {filename}")
        except Exception as exception:
            messagebox.showerror("Error", f"Failed to export: {exception}")


def import_from_excel(filename="address_book.xlsx"):
    # Import contacts from Excel and add them into the address book
    global address_book, next_id
    if not messagebox.askyesno("Import?", "Are you sure you want to import data from 'address_book.xlsx'?"):
        return
    
    try:
        data_frame = pd.read_excel(filename)
    except Exception as exception:
        messagebox.showerror("Error", f"Failed to import: {exception}")
        return

    # Convert DataFrame back to list of dicts
    new_contacts = data_frame.to_dict(orient="records")

    # Assign contact_id if missing or duplicate
    for contact in new_contacts:
        if "contact_id" not in contact or any(c["contact_id"] == contact["contact_id"] for c in address_book):
            contact["contact_id"] = next_id
            next_id += 1

    address_book.extend(new_contacts)
    save_address_book(address_book)
    refresh_table()
    messagebox.showinfo("Imported", f"{len(new_contacts)} contacts imported successfully.")

tooltip = None  # global tooltip variable

def create_tooltip(widget, text):
    # Hide tooltip when cursor leaves the table
    global tooltip
    tooltip = tk.Toplevel(widget)
    tooltip.wm_overrideredirect(True)  # remove window decorations
    label = tk.Label(tooltip, text=text, background="yellow", relief="solid", borderwidth=1)
    label.pack()
    tooltip.withdraw()  # start hidden
    return tooltip

def show_tooltip(event):
    # Show tooltip only when text is wider than its column
    global tooltip
    row = tree.identify_row(event.y)
    col = tree.identify_column(event.x)

    if row and col:
        values = tree.item(row)["values"]
        text = values[int(col[1:]) - 1]  # convert "#4" -> index 3

        column_width = tree.column(col, width=None)
        text_width = font.Font().measure(str(text))

        if text_width <= column_width:
            if tooltip:
                tooltip.withdraw()
            return
            
        if not tooltip:
            create_tooltip(tree, text)
        else:
            label = tooltip.winfo_children()[0]
            label.config(text=text)

        x, y, width, height = tree.bbox(row, column=col)
        tooltip.wm_geometry(f"+{x + tree.winfo_rootx()}+{y + tree.winfo_rooty() + height}")
        tooltip.deiconify()

        
    else:
        if tooltip:
            tooltip.withdraw()

def hide_tooltip(event):
    # Hide tooltip when cursor leaves the table
    global tooltip
    if tooltip:
        tooltip.withdraw()

# --------------------- Input validation functions ---------------------
def check_name_real_time(event, entry):
    # Highlight entry if input has invalid characters
    if re.fullmatch(r"[A-Za-z\-\' ]+", entry.get()):
        entry.config(bg="white")
    else:
        entry.config(bg="#FF7F7F")  # red background for invalid input

def check_address_real_time(event, entry):
    # Make sure address is not empty
    if entry.get():
        entry.config(bg="white")
    else:
        entry.config(bg="#FF7F7F")  # red if empty

def check_contact_real_time(event, entry):
    # Check for valid 11-digit Philippine mobile number
    num = entry.get().replace(" ", "")
    if len(num) == 11 and num.isdigit():
        entry.config(bg="white")
    else:
        entry.config(bg="#FF7F7F")

# --------------------- Contact creation helper ---------------------
def create_contact(contact_id, first_name, last_name, address, contact_number):
    # Return a dictionary for a contact
    return {
        "contact_id": contact_id,
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "contact_number": contact_number
    }

# --------------------- Data saving/loading ---------------------
def save_address_book(address_book):
    # Save all contacts to a JSON file
    data = address_book
    with open("address_book.json", "w") as file:
        json.dump(data, file, indent=4)

def load_address_book():
    #Load contacts from JSON file; return empty list if file missing or corrupt.
    try:
        with open("address_book.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
# --------------------- Search functions ---------------------
def match(contact, category, query):
    # Check if contact matches search query for a category
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
    # Get query and selected category
    query = search_bar.get().lower()
    category = search_dropdown.get()

    # Clear selection highlight in combobox
    search_dropdown.selection_clear()  

    filtered = []

    # Filter contacts by matching query
    for contact in address_book:
        if match(contact, category, query):
            filtered.append(contact)

    refresh_table(filtered)  # Update table with filtered contacts

def reset_search():
    # Clear search bar and reset category
    search_bar.delete(0, "end")
    search_dropdown.current(0)
    refresh_table()  # Refresh table to show all contacts

# --------------------- Sorting ---------------------
sort_state = {}  # Keep track of sorting direction for each column

def sort_by(column, treeview_column):
    # Determine current sort direction and flip it
    reverse = sort_state.get(column, False)
    sort_state[column] = not reverse

    # Sort contacts in memory by column
    sorted_contacts = sorted(address_book, key=lambda contact: contact[column], reverse=reverse)
    refresh_table(sorted_contacts)

    # Reset column headers to default text
    tree.heading("first", text="First Name")
    tree.heading("last", text="Last Name")
    tree.heading("address", text="Address")
    tree.heading("contact", text="Contact Number")
    tree.heading("index", text="No.")

    # Add arrow to indicate sorting direction
    if not reverse:
        arrow = " ▲"
    else:
        arrow = " ▼"

    text = {"first": "First Name", "last": "Last Name"}.get(treeview_column, treeview_column)
    tree.heading(treeview_column, text=text + arrow)

# --------------------- Table refresh ---------------------
def refresh_table(contacts=None):
    # Clear existing rows
    tree.delete(*tree.get_children())

    if contacts is None:
        contacts = address_book  # Show all contacts if none provided

    # Insert each contact into Treeview
    for i, contact in enumerate(contacts, start=1):
        tree.insert("", "end", iid=contact["contact_id"], values=(
            i,   
            contact["first_name"],
            contact["last_name"],
            contact["address"],
            contact["contact_number"]
        ))

# --------------------- Entry creation helper ---------------------
def create_labeled_entry(parent, label_text, helper_text):
    # Create a label, helper text, and entry box stacked vertically
    tk.Label(parent, text=label_text, font=("STSong", 20)).pack(pady=5)
    tk.Label(parent, text=helper_text, font=("STSong", 12), fg="gray").pack()
    entry = tk.Entry(parent, font=("STSong", 20))
    entry.pack(pady=5)
    return entry

# --------------------- Add contact ---------------------
def add_contact():
    add_win = tk.Toplevel(root)  # New window for adding
    add_win.title("Add Contact")
    add_win.geometry("800x500")

    # Create labeled entries
    first_entry = create_labeled_entry(add_win, "First Name", "Input only letters, apostrophes, or dashes.")
    last_entry = create_labeled_entry(add_win, "Last Name", "Input only letters, apostrophes, or dashes.")
    address_entry = create_labeled_entry(add_win, "Address", "Address cannot be empty.")
    contact_num_entry = create_labeled_entry(add_win, "Contact Number", "Input an 11-digit mobile number (e.g., 09123456789)")

    first_entry.focus_set()  # Auto-focus first field

    # Bind real-time validation
    first_entry.bind("<KeyRelease>", lambda e: check_name_real_time(e, first_entry))
    last_entry.bind("<KeyRelease>", lambda e: check_name_real_time(e, last_entry))
    address_entry.bind("<KeyRelease>", lambda e: check_address_real_time(e, address_entry))
    contact_num_entry.bind("<KeyRelease>", lambda e: check_contact_real_time(e, contact_num_entry))

    def save_contact():
        global next_id

        # Get values from entries
        first = first_entry.get()
        last = last_entry.get()
        address = address_entry.get()
        contact_num = contact_num_entry.get().replace(" ", "")

        # Check for invalid entries (red background)
        if first_entry['bg'] == '#FF7F7F' or last_entry['bg'] == '#FF7F7F' or address_entry['bg'] == '#FF7F7F' or contact_num_entry['bg'] == '#FF7F7F':
            messagebox.showerror("Invalid Input", "There are invalid fields. Please fix them before adding.")
            return
        
        # Assign unique ID and increment
        contact_id = next_id
        next_id += 1
        
        # Create new contact dictionary
        new_contact = create_contact(contact_id, first, last, address, contact_num)
        address_book.append(new_contact)  # Add to list
        save_address_book(address_book)  # Save to file
        refresh_table()  # Update table
        messagebox.showinfo("Success", "Contact Added!")
        add_win.destroy()  # Close add window
    
    # Button to save new contact
    tk.Button(add_win, text="Add Contact", font=("STSong", 20), command=save_contact).pack(pady=5)

# ----------------- Edit contact -----------------------
def on_double_click(event): # Double-click to edit
    selected = tree.selection()  # Get selected row
    if selected:  
        edit_contact()  # Open edit window

def edit_contact():
    selected_id = tree.focus()  # Get selected row ID

    if not selected_id:
        messagebox.showerror("Error", "Please select a contact from the table to edit")
        return

    contact_id = int(selected_id)

    # Find the contact dictionary
    for contact in address_book:
        if contact["contact_id"] == contact_id:
            break
    else:  
        return  # If not found, exit function

    edit_window = tk.Toplevel(root)  # New window for editing
    edit_window.title("Edit Contact")
    edit_window.geometry("800x500")

    # Create labeled entries and populate with existing data
    first_entry = create_labeled_entry(edit_window, "First Name", "Input only letters, apostrophes, or dashes.")
    last_entry = create_labeled_entry(edit_window, "Last Name", "Input only letters, apostrophes, or dashes.")
    address_entry = create_labeled_entry(edit_window, "Address", "Address cannot be empty.")
    contact_num_entry = create_labeled_entry(edit_window, "Contact Number", "Input an 11-digit mobile number (e.g., 09123456789)")

    first_entry.insert(0, contact["first_name"])
    last_entry.insert(0, contact["last_name"])
    address_entry.insert(0, contact["address"])
    contact_num_entry.insert(0, contact["contact_number"])

    first_entry.focus_set()  # Auto-focus first field

    # Bind real-time validation
    first_entry.bind("<KeyRelease>", lambda e: check_name_real_time(e, first_entry))
    last_entry.bind("<KeyRelease>", lambda e: check_name_real_time(e, last_entry))
    address_entry.bind("<KeyRelease>", lambda e: check_address_real_time(e, address_entry))
    contact_num_entry.bind("<KeyRelease>", lambda e: check_contact_real_time(e, contact_num_entry))

    def save_edit():
        # Validate fields
        if first_entry['bg'] == '#FF7F7F' or last_entry['bg'] == '#FF7F7F' or address_entry['bg'] == '#FF7F7F' or contact_num_entry['bg'] == '#FF7F7F':
            messagebox.showerror("Invalid Input", "There are invalid fields. Please fix them before saving.")
            return
        
        # Update contact dictionary
        contact["first_name"] = first_entry.get()
        contact["last_name"] = last_entry.get()
        contact["address"] = address_entry.get()
        contact["contact_number"] = contact_num_entry.get().replace(" ", "")
        
        save_address_book(address_book)  # Save changes
        refresh_table()  # Update table
        messagebox.showinfo("Updated", "Contact updated successfully")
        edit_window.destroy()  # Close edit window

    # Button to save changes
    tk.Button(edit_window, text="Save Changes", command=save_edit).pack()

# --------------------- Delete contact ---------------------
def on_delete_key(event):
    delete_contact()  # Bind Delete key to function

def delete_contact():
    selected_id = tree.focus()  # Get selected row

    if not selected_id:
        messagebox.showerror("Error", "Choose a contact from the table to delete")
        return

    contact_id = int(selected_id)

    # Find contact index in list
    for i, contact in enumerate(address_book):
        if contact_id == contact["contact_id"]:
            name = f"{contact['first_name']} {contact['last_name']}"
            break
    else:
        return

    # Confirm deletion
    if messagebox.askyesno("Delete Contact?", f"Are you sure you want to delete {name}?"):
        address_book.pop(i)  # Remove from list
        save_address_book(address_book)  # Save changes
        refresh_table()  # Update table

def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# ------------------ Main Program ----------------


address_book = load_address_book()  # Keep loaded contacts in memory

# Determine next available ID
if address_book:
    next_id = max(contact["contact_id"] for contact in address_book) + 1
else:
    next_id = 1

filtered_contacts = []  # Initialize empty filtered contacts

# --------------------- GUI ---------------------
root = tk.Tk()
root.geometry("800x500")
root.title("Address Book")

# Title label
title = tk.Label(root, text="Address Book", font=("cascadia code", 30), bg="pink", fg="black")

# Frame for search bar
search_frame = tk.Frame(root, bg="pink")

# Search category label
search_by = tk.Label(search_frame, fg="black", text="Search By:", font=("cascadia code", 20))

# Dropdown for category selection
search_dropdown = ttk.Combobox(search_frame, values=["First Name", "Last Name", "Address", "Contact No."], width=20, font=("cascadia code", 20), state="readonly")
search_dropdown.current(0)

# Reset search button
reset_btn = tk.Button(search_frame, text="Clear", font=("cascadia code", 15), command=reset_search)

# Search bar entry
search_bar = tk.Entry(search_frame, font=("cascadia code", 20))
search_bar.focus_set()  # Auto-focus

# Main frame containing buttons and table
main_frame = tk.Frame(root, bg="black")

# Buttons on the left
buttons_frame = tk.Frame(main_frame, bg="pink")

# Contacts table frame on the right
contacts_frame = tk.Frame(main_frame, bg="pink")

# --------------------- Bindings ---------------------
search_dropdown.bind("<<ComboboxSelected>>", on_search)  # Filter on category change
search_bar.bind("<KeyRelease>", on_search)  # Filter on typing

# --------------------- Pack widgets ---------------------
title.pack(fill="x")
search_frame.pack(fill="x", padx=10, pady=10)
search_by.pack(side="left", padx=20, pady=10)
search_dropdown.pack(side="left", padx=5, pady=10)
reset_btn.pack(side="left", padx=5)
search_bar.pack(side="left", fill="x", expand=True, padx=5, pady=10)

main_frame.pack(fill="both", expand=True, padx=10, pady=10)
buttons_frame.pack(side="left", fill="y", padx=10, pady=10)
contacts_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# --------------------- Buttons ---------------------
buttons = {
    "Add Contact": add_contact, 
    "Edit Contact": edit_contact,
    "Delete Contact": delete_contact,
    "Export Excel": export_to_excel,
    "Import Excel": import_from_excel,
    "Exit": exit_program
}

# Create button widgets
for button_text, button_function in buttons.items():
    btn = tk.Button(buttons_frame, text=button_text, bg="pink", fg="black", font=("cascadia code", 15), command=lambda f=button_function: f())
    btn.pack(padx=10, pady=28)



# --------------------- Treeview styling ---------------------
style = ttk.Style()
style.theme_use("clam")  # Theme needed for custom heading fonts

# Global Treeview style
style.configure("Treeview", font=("cascadia code", 15), rowheight=35)
style.configure("Treeview.Heading", font=("cascadia code", 12), background="pink", foreground="black")

# --------------------- Treeview setup ---------------------
tree = ttk.Treeview(contacts_frame, columns=("index", "first", "last", "address", "contact"), show="headings")

# Define column headings
tree.heading("index", text="No.")
tree.heading("first", text="First Name", command=lambda: sort_by("first_name", "first"))
tree.heading("last", text="Last Name", command=lambda: sort_by("last_name", "last"))
tree.heading("address", text="Address")
tree.heading("contact", text="Contact Number")

# Define column widths and alignment
tree.column("index", width=20, anchor="center")
tree.column("first", width=100, anchor="center")
tree.column("last", width=100, anchor="center")
tree.column("address", width=460, anchor="w", stretch=True)
tree.column("contact", width=140, anchor="center")

# Bind double-click and delete key
tree.bind("<Double-1>", on_double_click)
tree.bind("<Delete>", on_delete_key)
tree.bind("<Motion>", show_tooltip)   # hover over a row
tree.bind("<Leave>", hide_tooltip)    # leave the treeview area

# Scrollbars
scrollbar_y = tk.Scrollbar(contacts_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar_y.set)

scrollbar_x = tk.Scrollbar(contacts_frame, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=scrollbar_x.set)

scrollbar_y.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")
tree.pack(fill="both", expand=True)

# Initial table refresh
refresh_table()

# Start the Tkinter event loop
root.mainloop()
