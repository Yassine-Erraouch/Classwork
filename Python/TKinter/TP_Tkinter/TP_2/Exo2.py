
import tkinter as tk
import ttkbootstrap as ttk

window = tk.Tk()
window.title("Exo 2")
window.geometry("400x400")

# Use ttkbootstrap for styling (e.g., 'cosmo' theme)
window.style = ttk.Style(window)
window.style.theme_use("cosmo")

#using the treeview widget
tree = ttk.Treeview(window, columns=("label","name", "ID", "Favourite Pizza"))
#creating the headings for the treeview widget
tree.heading("label", text="Label")
tree.heading("name", text="name")
tree.heading("ID", text="ID")
tree.heading("Favourite Pizza", text="Favourite Pizza")

#adding data to the treeview widget
tree.insert("", "end", text="Label 1", values=("name 1", "ID 1", "Favourite Pizza 1"))
tree.insert("", "end", text="Label 2", values=("name 2", "ID 2", "Favourite Pizza 2"))
tree.insert("", "end", text="Label 3", values=("name 3", "ID 3", "Favourite Pizza 3"))
tree.insert("", "end", text="Label 4", values=("name 4", "ID 4", "Favourite Pizza 4"))
tree.insert("", "end", text="Label 5", values=("name 5", "ID 5", "Favourite Pizza 5"))

tree.pack()

window.mainloop()
