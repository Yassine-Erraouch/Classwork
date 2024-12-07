import tkinter as tk
from tkinter import ttk
#ttk est un module complémentaire de tkinter qui offre des widgets modernes et plus stylisés, comme Treeview.
# Create the main window
root = tk.Tk()
root.title("Treeview Example")

# Create a Treeview widget
#show="headings" indique que seules les en-têtes de colonnes seront visibles (sans affichage des colonnes par défaut).
tree = ttk.Treeview(root, columns=("ID", "Title", "Price", "Category"), show="headings")

# Define the columns
#Pour chaque colonne, on définit l'en-tête à afficher en utilisant la méthode heading(). Par exemple, la colonne "ID" aura l'en-tête "ID", et ainsi de suite.
tree.heading("ID", text="ID")
tree.heading("Title", text="Title")
tree.heading("Price", text="Price")
tree.heading("Category", text="Category")

# Define the columns' widths
#La méthode column() permet de définir la largeur de chaque colonne (en pixels).
tree.column("ID", width=100)
tree.column("Title", width=200)
tree.column("Price", width=100)
tree.column("Category", width=150)

# Add some sample data
#Les données des produits sont ajoutées avec insert(). La méthode insert() prend plusieurs arguments, dont :
#Le premier argument "" indique que l'élément sera ajouté à la racine (pas d'élément parent).
#"end" spécifie que les éléments doivent être insérés à la fin.
#values=(1, "Product 1", "10.99", "Category A") représente les données du produit sous forme de tuple,
#  correspondant aux colonnes définies précédemment.
tree.insert("", "end", values=(1, "Product 1", "10.99", "Category A"))
tree.insert("", "end", values=(2, "Product 2", "20.49", "Category B"))
tree.insert("", "end", values=(3, "Product 3", "15.99", "Category A"))
tree.insert("", "end", values=(4, "Product 4", "30.00", "Category C"))

# Pack the Treeview into the window
#tree.pack() ajoute le widget Treeview à la fenêtre principale. 
# fill=tk.BOTH permet au tableau de remplir toute la fenêtre,
#  et expand=True permet au tableau de s'adapter à la taille de la fenêtre lorsqu'elle est redimensionnée.
tree.pack(fill=tk.BOTH, expand=True)

# Start the GUI event loop
root.mainloop()
