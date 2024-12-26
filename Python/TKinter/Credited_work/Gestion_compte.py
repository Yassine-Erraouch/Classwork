import ttkbootstrap as tb
from tkinter import messagebox, ttk
from abc import ABC, abstractmethod

class Compte(ABC):
    def __init__(self, numero: int, proprietaire: str, solde_initial: float):
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde_initial = solde_initial
        
    @abstractmethod
    def obtenir_informations(self):
        return (self.numero, self.proprietaire, self.solde_initial)
    
class CompteCourant(Compte):
    def __init__(self, numero, proprietaire, solde_initial, montant_decouvert: float):
        super().__init__(numero, proprietaire, solde_initial)
        self.montant_decouvert = montant_decouvert
        
    def obtenir_informations(self):
        return (self.numero, self.proprietaire, self.solde_initial, "Courant", "-", self.montant_decouvert)

class CompteEpargne(Compte):
    def __init__(self, numero, proprietaire, solde_initial, taux_interet: float):
        super().__init__(numero, proprietaire, solde_initial)
        self.taux_interet = taux_interet
        
    def obtenir_informations(self):
        return (self.numero, self.proprietaire, self.solde_initial, "Épargne", self.taux_interet, "-")
    

class GestionCompteApp(tb.Window):
    def __init__(self):
        super().__init__()
        self.title('Gestion des Comptes Bancaires')
        self.geometry("750x520")
        # interface variables
        self.numero = 1 
        self.type_var = tb.StringVar(value="Courant") 
        self.proprietaire_var = tb.StringVar() 
        self.solde_var = tb.DoubleVar() 
        self.taux_interet_var = tb.DoubleVar() 
        self.montant_decouvert_var = tb.DoubleVar() 
 
        # account list
        self.comptes = [] 
 
        # widget creation 
        self.creer_widgets() 
 
    def creer_widgets(self): 
        # form widgets 
        tb.Label(self, text="Numéro:").grid(row=0, column=0, pady=10) 
        tb.Label(self, textvariable=tb.StringVar(value=str(self.numero))).grid(row=0, column=1) 
        tb.Label(self, text="Propriétaire:").grid(row=1, column=0, pady=10) 
        tb.Entry(self, textvariable=self.proprietaire_var).grid(row=1, column=1) 
        tb.Label(self, text="Solde Initial:").grid(row=2, column=0, pady=10) 
        tb.Entry(self, textvariable=self.solde_var).grid(row=2, column=1, pady=10) 
        tb.Label(self, text="Euro").grid(row=2, column=2, pady=10, sticky='w') 
        tb.Label(self, text="Type:").grid(row=3, column=0, pady=10) 
        tb.Radiobutton(self, text="Courant", variable=self.type_var, value="Courant", command=self.toggle_fields).grid(row=3, column=1 , pady=10, padx= 10) 
        tb.Radiobutton(self, text="Épargne", variable=self.type_var, value="Épargne", command=self.toggle_fields).grid(row=3, column=2, pady=10, padx= 10) 
        tb.Label(self, text="Taux Intérêt:").grid(row=4, column=0, pady=10) 
        self.taux_interet_entry = tb.Entry(self, textvariable=self.taux_interet_var, state="disabled") 
        self.taux_interet_entry.grid(row=4, column=1, pady=10) 
        tb.Label(self, text="M. Découvert:").grid(row=5, column=0, pady=10) 
        self.montant_decouvert_entry = tb.Entry(self, textvariable=self.montant_decouvert_var) 
        self.montant_decouvert_entry.grid(row=5, column=1, pady=10) 
        tb.Button(self, text="Création Compte", command=self.creer_compte).grid(row=6, column=1, pady=10) 
 
        # table for displaying the accounts 
        self.table_frame = tb.Frame(self,)
        self.table_frame.grid(row=7, column=0, columnspan=3, pady=10, padx= 10)
    
        self.table = tb.Treeview(self.table_frame, columns=("Numéro", "Propriétaire", "Solde Initial", "Type", "Taux Intérêt", "Montant Découvert"), show="headings") 
        self.table.heading("Numéro", text="Numéro")
        self.table.heading("Numéro", text="Propriétaire")
        self.table.heading("Solde Initial", text="Solde Initial")
        self.table.heading("Type", text="Type")
        self.table.heading("Taux Intérêt", text="Taux Intérêt")
        self.table.heading("Montant Découvert", text="Montant Découvert")
    
    
        self.table.column("Numéro", width=100)
        self.table.column("Solde Initial", width=100)
        self.table.column("Type", width=100)
        self.table.column("Taux Intérêt", width=100)
        self.table.column("Montant Découvert", width=100)
        self.table.pack(fill="both", expand=True, padx=10)
        
    
 
    def toggle_fields(self): 
        if self.type_var.get() == "Courant": 
            self.taux_interet_entry.config(state="disabled") 
            self.montant_decouvert_entry.config(state="normal") 
        else: 
            self.taux_interet_entry.config(state="normal") 
            self.montant_decouvert_entry.config(state="disabled") 
 
    def creer_compte(self): 
        proprietaire = self.proprietaire_var.get() 
        solde = self.solde_var.get() 
        
        if proprietaire == "" or solde == "":
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return
        
        else:
            if self.type_var.get() == "Courant": 
                montant_decouvert = self.montant_decouvert_var.get() 
                compte = CompteCourant(self.numero, proprietaire, solde, montant_decouvert) 
            else: 
                taux_interet = self.taux_interet_var.get() 
                compte = CompteEpargne(self.numero, proprietaire, solde, taux_interet) 
    
            self.comptes.append(compte) 
            self.numero += 1 
            self.rafraichir_tableau() 
            self.proprietaire_var.set("") 
            self.solde_var.set(0) 
            self.taux_interet_var.set(0) 
            self.montant_decouvert_var.set(0) 
        
    
   
    def rafraichir_tableau(self): 
        for row in self.table.get_children():
            self.table.delete(row)
        for compte in self.comptes: 
            self.table.insert("", "end", values=compte.obtenir_informations())            
app = GestionCompteApp()
app.mainloop()