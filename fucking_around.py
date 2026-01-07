import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Address Book")
root.geometry("800x500")
root.configure(bg="white")

menu_title = tk.Label(
    root,
    text="Address Book",
    bg="yellow",
    fg="black",
    width=15,
    font=("Times New Roman", 50)
    
)
menu_title.pack(fill="x", pady=10)


main_menu_frame = tk.Label(root, bg="white")
main_menu_frame.pack(fill="both", expand=True)

menu_container = tk.Frame(main_menu_frame, bg="#d3dbd5")
menu_container.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5)




options = ["Add Contact", "Edit Contact", "Delete Contact", "View Contacts", "Search Address Book", "Exit"]

for i, option in enumerate(options):
    button = tk.Button(
        menu_container,
        text=option,
        bg="gray",
        fg="black",
        font=("Times New Roman", 20)
    )
    
    button.pack(fill="x", pady=10, padx=10)


root.mainloop()
