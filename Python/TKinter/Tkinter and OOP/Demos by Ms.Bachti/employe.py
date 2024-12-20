import tkinter as tk
from tkinter import ttk,messagebox

def show_insert_frame():
    # Cacher les boutons
    insert_button.pack_forget()
    delete_button.pack_forget()

    # Afficher le frame d'insertion
    insert_frame.pack(pady=10)
    root.geometry('400x430')

def hide_insert_frame():
    # Réafficher les boutons
    insert_button.pack(side=tk.LEFT, padx=5)
    delete_button.pack(side=tk.LEFT, padx=5)

    # Cacher le frame d'insertion
    insert_frame.pack_forget()
    root.geometry('400x300')

def insert_item():
    # Ajouter un élément au Treeview
    tree.insert("", tk.END, values=(entry_name.get(), entry_age.get()))
    
    # Effacer les champs d'entrée
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

    # Cacher le frame et réafficher les boutons
    hide_insert_frame()

def delete_selected_item():
    # Supprimer l'élément sélectionné
    selected_item = tree.selection()
    if selected_item:
        conf=messagebox.askokcancel('confirmation','Voulez vous vraiment supprimer ? ')
        if(conf):
            tree.delete(selected_item)
        else:
            return

# Création de la fenêtre principale
root = tk.Tk()
root.title("Treeview Insert/Delete Example")
root.geometry("400x300")

# Création du Treeview
tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings", height=8)
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.pack(pady=10)

# Boutons Insert et Delete
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

insert_button = tk.Button(button_frame, text="Insert", command=show_insert_frame)
insert_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete", command=delete_selected_item)
delete_button.pack(side=tk.LEFT, padx=5)

# Frame pour l'insertion des données
insert_frame = tk.Frame(root)

label_name = tk.Label(insert_frame, text="Name:")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(insert_frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_age = tk.Label(insert_frame, text="Age:")
label_age.grid(row=1, column=0, padx=5, pady=5)
entry_age = tk.Entry(insert_frame)
entry_age.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(insert_frame, text="Add", command=insert_item)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Lancement de la boucle principale
root.mainloop()
