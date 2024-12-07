# import tkinter as tk
# import ttkbootstrap as ttk

# window = tk.Tk()
# window.title("Exo 8")
# window.geometry("300x150")
# def show_message():
#     print("Hello " + name_field.get())
# name = ttk.Label(window, text="Nom :", font=("sans serif",16), padx=20,pady=20)
# name_field = ttk.Entry(window, font=("sans serif",16),width=30, bootstyle="primary")
# button = ttk.Button(window, text = "Validate", width= 12, bootstyle="primary", command= show_message)
# name.grid(row=0,column=0)
# name_field.grid(row=0,column=1, columnspan=2,padx=100)
# button.grid(row=1,column=0, padx= 30, pady= 20)
# window.mainloop()

import tkinter as tk
import ttkbootstrap as ttk

window = tk.Tk()
window.title("Exo 8")
window.geometry("300x150")

def show_message():
    greeting_label =ttk.Label(window, text = "Hello " + name_field.get())
    greeting_label.grid(row = 1, column = 1, padx= 30, pady= 20)

# Use padding as a tuple (x, y)
name = ttk.Label(window, text="Nom :", font=("sans serif",16), padding=(20, 20))  # Changed padx/pady to padding
name_field = ttk.Entry(window, font=("sans serif",16), width=10, bootstyle="primary")
button = ttk.Button(window, text="Validate", width=12, bootstyle="primary", command=show_message)

# Grid layout
name.grid(row=0, column=0)
name_field.grid(row=0, column=1, columnspan=2)
button.grid(row=1, column=0)

window.mainloop()
