import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

def toggle_entry(check_var, entry):
    if check_var.get():
        entry.config(state="normal")
    else:
        entry.delete(0, tb.END)
        entry.config(state="disabled")

def calculate():
    try:
        total = 0
        if bread_entry.get():
            total += float(bread_entry.get()) * 4
        if beef_entry.get():
            total += float(beef_entry.get()) * 4
        if vegetable_entry.get():
            total += float(vegetable_entry.get()) * 9
        if pasta_entry.get():
            total += float(pasta_entry.get()) * 4
        if rice_entry.get():
            total += float(rice_entry.get()) * 4
        if milk_entry.get():
            total += float(milk_entry.get()) * 4
        
        result_label.config(text=f"Your meal's caloric value is: {total:.2f} kcal")
    except ValueError:
        messagebox.showerror("Error", "Please Enter valid numeric values.")

# Creating the window
root = tb.Window()
root.title("Colories Calculator")
root.style.theme_use("journal")
root.geometry("300x350")

# Variables for the checkboxes
bread_var = tb.BooleanVar()
beef_var = tb.BooleanVar()
vegetable_var = tb.BooleanVar()
pasta_var = tb.BooleanVar()
rice_var = tb.BooleanVar()
milk_var = tb.BooleanVar()

bread_entry_var = tb.StringVar()
beef_entry_var = tb.StringVar()
vegetable_entry_var = tb.StringVar()
pasta_entry_var = tb.StringVar()
rice_entry_var = tb.StringVar()
milk_entry_var = tb.StringVar()






# widgets
bread_check = tb.Checkbutton(root, text="Bread", variable=bread_entry_var,
                                command=lambda: toggle_entry(bread_var, bread_entry))
bread_check.grid(row=0, column=0, sticky="w", pady= 10, padx=5)
bread_entry = tb.Entry(root, state="disabled")
bread_entry.grid(row=0, column=1)
tb.Label(root, text="g").grid(row=0, column=2, pady= 10, padx=5)



beef_check = tb.Checkbutton(root, text="Beef", variable=beef_entry_var,
                             command=lambda: toggle_entry(beef_var, beef_entry))
beef_check.grid(row=1, column=0, sticky="w", pady= 10, padx=5)
beef_entry = tb.Entry(root, state="disabled")
beef_entry.grid(row=1, column=1, pady= 10, padx=5)
tb.Label(root, text="g").grid(row=1, column=2, pady= 10, padx=5)


vegetable_check = tb.Checkbutton(root, text="Vegetables", variable=vegetable_entry_var,
                            command=lambda: toggle_entry(vegetable_var, vegetable_entry))
vegetable_check.grid(row=2, column=0, sticky="w", pady= 10, padx=5)
vegetable_entry = tb.Entry(root, state="disabled")
vegetable_entry.grid(row=2, column=1, pady= 10, padx=5)
tb.Label(root, text="g").grid(row=2, column=2, pady= 10, padx=5)

# add more food items and add their corresponding variables in the same fashion

pasta_check = tb.Checkbutton(root, text="Pasta", variable=pasta_entry_var,
                                command=lambda: toggle_entry(pasta_var, pasta_entry))
pasta_check.grid(row=3, column=0, sticky="w", pady= 10, padx=5)
pasta_entry = tb.Entry(root, state="disabled")
pasta_entry.grid(row=3, column=1, pady= 10, padx=5)
tb.Label(root, text="g").grid(row=3, column=2, pady= 10, padx=5)


rice_check = tb.Checkbutton(root, text="Rice", variable=rice_entry_var,
                             command=lambda: toggle_entry(rice_var, rice_entry))
rice_check.grid(row=4, column=0, sticky="w", pady= 10, padx=5)
rice_entry = tb.Entry(root, state="disabled")
rice_entry.grid(row=4, column=1, pady= 10, padx=5)
tb.Label(root, text="g").grid(row=4, column=2, pady= 10, padx=5)


milk_check = tb.Checkbutton(root, text="Milk", variable=milk_entry_var,
                            command=lambda: toggle_entry(milk_var, milk_entry))
milk_check.grid(row=5, column=0, sticky="w", pady= 10, padx=5)
milk_entry = tb.Entry(root, state="disabled")
milk_entry.grid(row=5, column=1, pady= 10, padx=5)
tb.Label(root, text="ml").grid(row=5, column=2, pady= 10, padx=5)


calculate_button = tb.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=6, column=0, columnspan=2)

result_label = tb.Label(root, text="Your meal's caloric value is: 0 Kcal")
result_label.grid(row=7, column=0, columnspan=2)

# launching the window
root.mainloop()