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
        if bread_var.get():
            total += float(bread_entry.get() or 0) * 4
        if beef_var.get():
            total += float(beef_entry.get() or 0) * 4
        if vegetable_var.get():
            total += float(vegetable_entry.get() or 0) * 0.5
        if pasta_var.get():
            total += float(pasta_entry.get() or 0) * 3.5
        if rice_var.get():
            total += float(rice_entry.get() or 0) * 3.6
        if milk_var.get():
            total += float(milk_entry.get() or 0) * 0.6
        if cheese_var.get():
            total += float(cheese_entry.get() or 0) * 4
        if fish_var.get():
            total += float(fish_entry.get() or 0) * 2
        if egg_var.get():
            total += float(egg_entry.get() or 0) * 1.55

        result_label.config(text=f"Your meal's caloric value is: {total:.2f} kcal")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Creating the window
root = tb.Window()
root.title("Calorie Calculator")
root.style.theme_use("journal")
root.geometry("400x500")

# Variables for the checkboxes
bread_var = tb.BooleanVar()
beef_var = tb.BooleanVar()
vegetable_var = tb.BooleanVar()
pasta_var = tb.BooleanVar()
rice_var = tb.BooleanVar()
milk_var = tb.BooleanVar()
cheese_var = tb.BooleanVar()
fish_var = tb.BooleanVar()
egg_var = tb.BooleanVar()

# Header
header_label = tb.Label(root, text="Calorie Calculator", font=("Helvetica", 16, "bold"), anchor="center")
header_label.grid(row=0, column=0, columnspan=3, pady=10)

# Food item widgets
def add_food_item(row, text, check_var, entry_var, entry_unit):
    check = tb.Checkbutton(root, text=text, variable=check_var, \
                           command=lambda: toggle_entry(check_var, entry_var))
    check.grid(row=row, column=0, sticky="w", pady=5, padx=10)
    entry_var.config(state="disabled")
    entry_var.grid(row=row, column=1, pady=5, padx=10)
    tb.Label(root, text=entry_unit).grid(row=row, column=2, pady=5, padx=10)

bread_entry = tb.Entry(root)
add_food_item(1, "Bread", bread_var, bread_entry, "g")

beef_entry = tb.Entry(root)
add_food_item(2, "Beef", beef_var, beef_entry, "g")

vegetable_entry = tb.Entry(root)
add_food_item(3, "Vegetables", vegetable_var, vegetable_entry, "g")

pasta_entry = tb.Entry(root)
add_food_item(4, "Pasta", pasta_var, pasta_entry, "g")

rice_entry = tb.Entry(root)
add_food_item(5, "Rice", rice_var, rice_entry, "g")

milk_entry = tb.Entry(root)
add_food_item(6, "Milk", milk_var, milk_entry, "ml")

cheese_entry = tb.Entry(root)
add_food_item(7, "Cheese", cheese_var, cheese_entry, "g")

fish_entry = tb.Entry(root)
add_food_item(8, "Fish", fish_var, fish_entry, "g")

egg_entry = tb.Entry(root)
add_food_item(9, "Eggs", egg_var, egg_entry, "units")

# Calculate Button
calculate_button = tb.Button(root, text="Calculate", command=calculate, bootstyle="primary")
calculate_button.grid(row=10, column=0, columnspan=3, pady=20)

# Result Label
result_label = tb.Label(root, text="Your meal's caloric value is: 0 Kcal", font=("Helvetica", 12))
result_label.grid(row=11, column=0, columnspan=3, pady=10)

# Launching the window
root.mainloop()
