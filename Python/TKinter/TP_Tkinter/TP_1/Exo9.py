import tkinter as tk
import ttkbootstrap as ttk

window = tk.Tk()
window.title("Exo 9")
window.geometry("300x150")

def show_message(event):
    greeting_label =ttk.Label(window, text = "Hello " + name_field.get())
    greeting_label.grid(row = 1, column = 1, padx= 30, pady= 20)

# Use padding as a tuple (x, y)
name = ttk.Label(window, text="Nom :", font=("sans serif",16), padding=(20, 20))  # Changed padx/pady to padding
name_field = ttk.Entry(window, font=("sans serif",16), width=10, bootstyle="primary")
name_field.bind("<Return>", show_message)


# Grid layout
name.grid(row=0, column=0)
name_field.grid(row=0, column=1, columnspan=2)


window.mainloop()
