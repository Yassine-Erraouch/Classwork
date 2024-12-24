import ttkbootstrap as tb
from tkinter import messagebox, ttk
import tkinter as tk



#-----------------------------------------UI----------------------------------------------------

# creating the window
window = tb.Window()
window.title("Savings Calculator")
window.geometry("800x600")
style = tb.Style("minty")

# creating the variables
revenue = tb.DoubleVar(value=0.0)
elec = tb.DoubleVar(value=0.0)
water = tb.DoubleVar(value=0.0)
phone= tb.DoubleVar(value=0.0)
other = tb.DoubleVar(value=0.0)


# creating a custom font
custom_font = ("garamond", 14)

# creating the frames
entries_frame = tb.Frame(window)
calculate_frame = tb.Frame(window)


# creating the widgets
    # for the entries
tb.Label(entries_frame, text="Revenue", font=custom_font).grid(row=0, column=0, padx=10, pady=5)
revenue_entry = tb.Entry(entries_frame, textvariable=revenue, font=custom_font, width=780)
revenue_entry.grid(row=1, column=0, padx=10, pady=5)


tb.Label(entries_frame, text="Electricity", font=custom_font).grid(row=2, column=0, padx=10, pady=5)
elec_entry = tb.Entry(entries_frame, textvariable=elec, font=custom_font, width=780)
elec_entry.grid(row=3, column=0, padx=10, pady=5)

tb.Label(entries_frame, text="Water", font=custom_font).grid(row=4, column=0, padx=10, pady=5)
water_entry = tb.Entry(entries_frame, textvariable=water, font=custom_font, width=780)
water_entry.grid(row=5, column=0, padx=10, pady=5)

tb.Label(entries_frame, text="Phone", font=custom_font).grid(row=6, column=0, padx=10, pady=5)
phone_entry = tb.Entry(entries_frame, textvariable=phone, font=custom_font, width=780)
phone_entry.grid(row=7, column=0, padx=10, pady=5)

add_expense = tb.Button(entries_frame, text="Add expense", font=custom_font, width=780)
add_expense.grid(row=8, column=0, padx=10, pady=5)


    # for the calculate frame
tb.Label(calculate_frame, text="Savings", font=custom_font).grid(row=0, column=0, padx=10, pady=5)
savings_entry = tb.Entry(calculate_frame, font=custom_font, width=780, state="disabled")
savings_entry.grid(row=1, column=0, padx=10, pady=5)


tb.Label(calculate_frame, text="Total expenses", font=custom_font).grid(row=0, column=1, padx=10, pady=5)
total_expenses_entry = tb.Entry(calculate_frame, font=custom_font, width=780, state="disabled")
total_expenses_entry.grid(row=1, column=1, padx=10, pady=5)

tb.Label(calculate_frame, text="total Revenue", font=custom_font).grid(row=0, column=2, padx=10, pady=5)
total_revenue_entry = tb.Entry(calculate_frame, font=custom_font, width=780, state="disabled")
total_revenue_entry.grid(row=1, column=2, padx=10, pady=5)

calculate_btn = tb.Button(calculate_frame, text="Calculate", font=custom_font, width=780)
calculate_btn.grid(row=2, column=0, columnspan=3, padx=10, pady=5)