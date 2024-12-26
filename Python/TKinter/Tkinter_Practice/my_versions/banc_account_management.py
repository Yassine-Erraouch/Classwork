import tkinter as tk
from tkinter import messagebox, ttk

# Simplified Bank Account Management Application
root = tk.Tk()
root.title("Gestion des Comptes Bancaires")

# Variables
account_number = tk.IntVar(value=1)
owner_name = tk.StringVar()
initial_balance = tk.DoubleVar()
account_type = tk.StringVar(value="Courant")
interest_rate = tk.DoubleVar()
overdraft_limit = tk.DoubleVar()
accounts = []

# Functions
def update_fields():
    if account_type.get() == "Courant":
        interest_entry.config(state="disabled")
        overdraft_entry.config(state="normal")
    else:
        interest_entry.config(state="normal")
        overdraft_entry.config(state="disabled")

def create_account():
    owner = owner_name.get()
    balance = initial_balance.get()
    acc_type = account_type.get()
    interest = interest_rate.get() if acc_type == "Épargne" else None
    overdraft = overdraft_limit.get() if acc_type == "Courant" else None

    if not owner or balance <= 0:
        messagebox.showerror("Erreur", "Veuillez remplir correctement les champs.")
        return

    account = {
        "Numéro": account_number.get(),
        "Propriétaire": owner,
        "Solde Initial": balance,
        "Type": acc_type,
        "Taux Intérêt": interest,
        "Montant Découvert": overdraft
    }

    accounts.append(account)
    account_number.set(account_number.get() + 1)
    owner_name.set("")
    initial_balance.set(0.0)
    interest_rate.set(0.0)
    overdraft_limit.set(0.0)
    update_table()

def update_table():
    for row in table.get_children():
        table.delete(row)

    for account in accounts:
        table.insert("", "end", values=(
            account['Numéro'],
            account['Propriétaire'],
            account['Solde Initial'],
            account['Type'],
            account['Taux Intérêt'],
            account['Montant Découvert']
        ))

# GUI Components
# Form
tk.Label(root, text="Numéro:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=account_number, state="disabled").grid(row=0, column=1, sticky="w")

tk.Label(root, text="Propriétaire:").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=owner_name).grid(row=1, column=1, sticky="w")

tk.Label(root, text="Solde Initial:").grid(row=2, column=0, sticky="w")
tk.Entry(root, textvariable=initial_balance).grid(row=2, column=1, sticky="w")
tk.Label(root, text="Euro").grid(row=2, column=2, sticky="w")

tk.Label(root, text="Type:").grid(row=3, column=0, sticky="w")
tk.Radiobutton(root, text="Courant", variable=account_type, value="Courant", command=update_fields).grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Épargne", variable=account_type, value="Épargne", command=update_fields).grid(row=3, column=2, sticky="w")

tk.Label(root, text="Taux Intérêt:").grid(row=4, column=0, sticky="w")
interest_entry = tk.Entry(root, textvariable=interest_rate)
interest_entry.grid(row=4, column=1, sticky="w")
tk.Label(root, text="%").grid(row=4, column=2, sticky="w")

tk.Label(root, text="M. Découvert:").grid(row=5, column=0, sticky="w")
overdraft_entry = tk.Entry(root, textvariable=overdraft_limit)
overdraft_entry.grid(row=5, column=1, sticky="w")

tk.Button(root, text="Création Compte", command=create_account).grid(row=6, column=0, columnspan=3)

# Table using Treeview
table = ttk.Treeview(root, columns=("Numéro", "Propriétaire", "Solde Initial", "Type", "Taux Intérêt", "Montant Découvert"), show="headings")
table.grid(row=7, column=0, columnspan=3, pady=10)

# Define columns
table.heading("Numéro", text="Numéro")
table.heading("Propriétaire", text="Propriétaire")
table.heading("Solde Initial", text="Solde Initial")
table.heading("Type", text="Type")
table.heading("Taux Intérêt", text="Taux Intérêt")
table.heading("Montant Découvert", text="Montant Découvert")

table.column("Numéro", width=100)
table.column("Propriétaire", width=150)
table.column("Solde Initial", width=120)
table.column("Type", width=100)
table.column("Taux Intérêt", width=120)
table.column("Montant Découvert", width=150)

update_fields()
root.mainloop()
