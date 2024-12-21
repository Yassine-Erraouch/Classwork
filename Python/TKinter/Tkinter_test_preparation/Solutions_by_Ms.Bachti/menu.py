import tkinter as tk
from tkinter import Menu,messagebox

# Create the main window
parent = tk.Tk()
parent.title("Menu ")

# Create a menu bar
menu_bar = Menu(parent)
parent.config(menu=menu_bar)

# Create a File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu items to the File menu
file_menu.add_command(label="New",command=lambda: messagebox.showinfo('information','New Clicked'))
file_menu.add_command(label="Open",command=lambda: messagebox.showwarning('warning','Open Clicked'))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=parent.quit)

# Create an Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add menu items to the Edit menu
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Create a Help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add menu items to the Help menu
help_menu.add_command(label="About Spyder")

# Start the Tkinter event loop
parent.mainloop()
