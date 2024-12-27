import tkinter as tk
from abc import ABC, abstractmethod 
import math 
 
class Calculatrice(ABC):  # abstract calculator class
    def __init__(self): 
        self.operande = "" 
        self.resultat = 0 
     
    @abstractmethod 
    def calculer(self): # class method for calculating
        pass 
 
    def afficher_resultat(self):  # method for displaying the result
        return self.resultat
    


class CalculatriceScientifique(Calculatrice): # scientific calculator class
    def __init__(self): 
        super().__init__() 
        
    def calculer(self, expression): 
        try: 
            self.operande = expression 
            #----------------------------------------
            # Modified: Added "sqrt" handling
            if "sin" in expression: 
                self.resultat = math.sin(math.radians(float(expression[3:]))) 
            elif "cos" in expression: 
                self.resultat = math.cos(math.radians(float(expression[3:]))) 
            elif "tan" in expression: 
                self.resultat = math.tan(math.radians(float(expression[3:]))) 
            elif "sqrt" in expression:  # New handling for square root
                self.resultat = math.sqrt(float(expression[4:])) 
            else: 
                self.resultat = eval(expression)  # Use eval for other calculations 
            #----------------------------------------
        except Exception as e: 
            self.resultat = "Erreur"  # Handle invalid input more gracefully


class CalculatriceApp(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        self.title("Calculatrice Scientifique") 
        self.geometry("400x600") 
         
        self.calculatrice = CalculatriceScientifique() 
 
        # calling the method to create the widgets
        self.creer_widgets() 
 
    def creer_widgets(self): 
        # field to show operation 
        self.texte = tk.Entry(self, width=20, font=("Arial", 24), borderwidth=2, relief="solid") 
        self.texte.grid(row=0, column=0, columnspan=4) 
         
        # buttons
        boutons = [ 
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), 
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), 
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), 
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3), 
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3), 
        ] 
 
        for (text, row, col) in boutons: 
            bouton = tk.Button(self, text=text, width=5, height=2, command=lambda t=text: 
self.on_button_click(t)) 
            bouton.grid(row=row, column=col) 
 
    def on_button_click(self, texte): 
        if texte == "=": 
            expression = self.texte.get() 
            self.calculatrice.calculer(expression) 
            #----------------------------------------
            # Modified: Graceful result handling
            self.texte.delete(0, tk.END) 
            self.texte.insert(tk.END, self.calculatrice.afficher_resultat()) 
            #----------------------------------------
        elif texte == "C": 
            self.texte.delete(0, tk.END) 
        else: 
            current = self.texte.get() 
            self.texte.delete(0, tk.END) 
            self.texte.insert(tk.END, current + texte) 
 
app = CalculatriceApp() 
app.mainloop()
