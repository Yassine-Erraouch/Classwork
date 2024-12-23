import tkinter as tk
from tkinter import messagebox, ttk

# creating the variables
account_number = tk.IntVar(value=1)
owner = tk.StringVar()
initial_balance = tk.doubleVar()
account_type = tk.StringVar()
interest_rate = tk.DoubleVar()
current_balance = tk.DoubleVar()

# creating a custome font
font_var = ("garamond", 14)


# creating the UI
    # creating the window
window = tk.Tk()
window.geometry("600x150")
window.title("Bank Account Managemnt App")

    # creating the labels and buttons

account_number_lbl = tk.Label(window, text="Number", font=font_var)
account_number_display_label = tk.Label(window, textvariable=account_number, font=font_var)


owner_label = tk.Label(window, text="Owner", font=font_var)
owner_entry = tk.Entry(window, textvariable=owner ,font=font_var)


initial_balance_label = tk.Label(window, text="Initial Balance", font=font_var)
intial_balance_entry = tk.Entry(window, textvariable=initial_balance, font=font_var)


account_type_label = tk.Label(window, text='Account type', font=font_var)
savings_account = tk.Radiobutton(window, text="Credit", value="Credit", variable=account)


