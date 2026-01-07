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
    font=("Times New Roman", 30)
    
)
menu_title.pack(fill="x", pady=10)

root.mainloop()