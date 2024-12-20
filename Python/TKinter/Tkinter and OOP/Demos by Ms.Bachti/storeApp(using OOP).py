import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Name")
        self.root.geometry("900x600")

        # Connexion à la base de données SQLite
        self.conn = sqlite3.connect("store.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # Widgets pour les entrées
        tk.Label(root, text="ID").grid(row=0, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(root)
        
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
        self.txtName=tk.StringVar()
        self.entry_name = tk.Entry(root,textvariable=self.txtName)
     
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Price").grid(row=2, column=0, padx=10, pady=5)
        self.txtPrice=tk.StringVar()
        self.entry_price = tk.Entry(root,textvariable=self.txtPrice)
        self.entry_price.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Quantity").grid(row=3, column=0, padx=10, pady=5)
        self.txtQte=tk.StringVar()
        self.entry_quantity = tk.Entry(root,textvariable=self.txtQte)
        self.entry_quantity.grid(row=3, column=1, padx=10, pady=5)
        #ajouter un combobox avec une liste de categorie
        #***************************************************
        # Boutons pour les opérations
        tk.Button(root, text="Enter", bg="blue", fg="white", command=self.add_product).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(root, text="Update", bg="yellow", fg="black", command=self.update_product).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(root, text="Delete", bg="red", fg="white", command=self.delete_product).grid(row=4, column=2, padx=10, pady=10)

        # Table pour afficher les données
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Price", "Quantity"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        self.tree.bind("<ButtonRelease-1>", self.select_row)
        self.load_data()

    def create_table(self):
        """Créer la table dans la base de données si elle n'existe pas."""
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL,
                quantity INTEGER
            )"""
        )
        self.conn.commit()

    def add_product(self):
        """Ajouter un produit à la base de données."""
        try:
            id_ = int(self.entry_id.get())
            name = self.entry_name.get()
            price = float(self.entry_price.get())
            quantity = int(self.entry_quantity.get())

            # Insertion dans la base de données
            self.cursor.execute("INSERT INTO products (id, name, price, quantity) VALUES (?, ?, ?, ?)",
                                (id_, name, price, quantity))
            self.conn.commit()
            self.load_data()
            self.clear_inputs()
            messagebox.showinfo("Succès", "Produit ajouté avec succès.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "L'ID existe déjà.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    def update_product(self):
        """Mettre à jour un produit dans la base de données."""
        try:
            id_ = int(self.entry_id.get())
            name = self.entry_name.get()
            price = float(self.entry_price.get())
            quantity = int(self.entry_quantity.get())
            confirm=messagebox.askokcancel('confirmation','are you sure you want to update ? ')
            if(confirm):
                # Mise à jour dans la base de données
                self.cursor.execute("UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?",
                                    (name, price, quantity, id_))
                self.conn.commit()
                self.load_data()
                self.clear_inputs()
                messagebox.showinfo("Succès", "Produit mis à jour avec succès.")
            else:
                self.clear_inputs()
                return
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    def delete_product(self):
        """Supprimer un produit de la base de données."""
        try:
            id_ = int(self.entry_id.get())
            self.cursor.execute("DELETE FROM products WHERE id = ?", (id_,))
            self.conn.commit()
            self.load_data()
            self.clear_inputs()
            messagebox.showinfo("Succès", "Produit supprimé avec succès.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un ID valide.")

    def load_data(self):
        """Charger les données depuis la base de données et les afficher dans la table."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.cursor.execute("SELECT * FROM products")
        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=row)

    def select_row(self, event):
        """Sélectionner une ligne dans la table et remplir les champs."""
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.txtName.set("")
            self.entry_name.insert(0, values[1])
            self.entry_price.delete(0, tk.END)
            self.entry_price.insert(0, values[2])
            self.entry_quantity.delete(0, tk.END)
            self.entry_quantity.insert(0, values[3])

    def clear_inputs(self):
        """Effacer les champs de saisie."""
        self.entry_id.delete(0, tk.END)
        self.txtName.set("")
        self.txtPrice.set("")
        self.txtQte("")
    def showWindow(self):
        self.root.mainloop()


root = tk.Tk()
app = StoreApp(root)
#root.mainloop()
app.showWindow()
