import tkinter as tk
import ttkbootstrap as ttk

window = tk.Tk()
window.title("Exo 1 : Window Menu")
window.geometry("400x400")

#creating the menu bar with ttkbootstrap
menuBar = ttk.Menu(window)
window.config(menu=menuBar)

#creating the file menu
fileMenu = ttk.Menu(menuBar)
menuBar.add_cascade(label="File", menu=fileMenu)

#creating the edit menu
editMenu = ttk.Menu(menuBar)
menuBar.add_cascade(label="Edit", menu=editMenu)

#creating the help menu
helpMenu = ttk.Menu(menuBar)
menuBar.add_cascade(label="Help", menu=helpMenu)    

window.mainloop()