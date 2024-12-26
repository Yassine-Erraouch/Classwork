import ttkbootstrap as tb
from tkinter import messagebox, ttk
import json as js

class EmpPerformance:
    def __init__(self):
        self.app = tb.Window(themename="minty")
        self.app.title("Employee Performance Review App")
        self.app.geometry("600x400")

        # creating the variables
        self.matricule= tb.StringVar()
        self.nom = tb.StringVar()
        self.prenom = tb.StringVar()
        self.assiduité = tb.DoubleVar(value=0.0)
        self.discipline = tb.DoubleVar(value=0.0)
        self.animation_cours = tb.DoubleVar(value=0.0)
        self.encadrement = tb.DoubleVar(value=0.0)
        self.prep_cours = tb.DoubleVar(value=0.0)
        self.note = tb.DoubleVar(value=0.0)
        self.decision = tb.StringVar()
        
        
        
        
        # creating the UI
        self.display_frame = tb.Frame(self.app)
        self.info_frame = tb.Frame(self.app)
        
        self.display_frame.pack(pady=10, padx=10, fill='x')
        self.info_frame.pack_forget()
        
        # creating the treeview
        
        self.table = tb.Treeview(self.display_frame, columns=("Matricule","Nom","Prénom","Note","Décision"), show="headings") 
        self.table.heading("Matricule", text="Matricule")
        self.table.heading("Nom", text="Nom")
        self.table.heading("Prénom", text="Prénom")
        self.table.heading("Note", text="Note")
        self.table.heading("Décision", text="Décision")
        
        self.table.column("Matricule", width=100)
        self.table.column("Nom", width=100)
        self.table.column("Prénom", width=100)
        self.table.column("Note", width=100)
        self.table.column("Décision", width=100)
        
        self.table.pack()
        #loading the employees' info from employees.json
        with open('employees.json') as f:
            self.employees = js.load(f)
            
        #displaying the employees' info in the treeview
        for employee in self.employees:
            self.table.insert("", "end", values=(employee["id"], employee["last_name"], employee["first_name"], employee["note"], employee["decision"]))
        
        #binding the treeview
        self.table.bind("<<TreeviewSelect>>", self.show_info)
        
        
        #creating the input form
        tb.Label(self.info_frame, text="Matricule").grid(row=0, column=0, pady=5)
        tb.Label(self.info_frame, text="Nom").grid(row=1, column=0, pady=5)
        tb.Label(self.info_frame, text="Prénom").grid(row=2, column=0, pady=5)
        tb.Label(self.info_frame, text="Assiduité").grid(row=3, column=0, pady=5)
        tb.Label(self.info_frame, text="Discipline").grid(row=4, column=0, pady=5)
        tb.Label(self.info_frame, text="Animation Cours").grid(row=5, column=0, pady=5)
        tb.Label(self.info_frame, text="Encadrement").grid(row=6, column=0, pady=5)
        tb.Label(self.info_frame, text="Preparation Cours").grid(row=7, column=0, pady=5)
        
        
        self.matricule_entry = tb.Entry(self.info_frame, textvariable=self.matricule, state="readonly")
        self.matricule_entry.grid(row=0, column=1, pady=5, padx=5)
        
        self.nom_entry = tb.Entry(self.info_frame, textvariable=self.nom, state="readonly")
        self.nom_entry.grid(row=1, column=1, pady=5, padx=5)
        
        self.prenom_entry = tb.Entry(self.info_frame, textvariable=self.prenom, state="readonly")
        self.prenom_entry.grid(row=2, column=1, pady=5, padx=5)
        
        self.assiduité_entry = tb.Entry(self.info_frame, textvariable=self.assiduité)
        self.assiduité_entry.grid(row=3, column=1, pady=5, padx=5)
        
        self.discipline_entry = tb.Entry(self.info_frame, textvariable=self.discipline)
        self.discipline_entry.grid(row=4, column=1, pady=5, padx=5)
        
        self.animation_cours_entry = tb.Entry(self.info_frame, textvariable=self.animation_cours)
        self.animation_cours_entry.grid(row=5, column=1, pady=5, padx=5)
        
        self.encadrement_entry = tb.Entry(self.info_frame, textvariable=self.encadrement)
        self.encadrement_entry.grid(row=6, column=1, pady=5, padx=5)
        
        self.prep_cours_entry = tb.Entry(self.info_frame, textvariable=self.prep_cours)
        self.prep_cours_entry.grid(row=7, column=1, pady=5, padx=5)
        
        self.calculate_btn = tb.Button(self.info_frame, text="Calculer", command=self.calculate)
        self.calculate_btn.grid(row=8, column=0, pady=5, padx=5)
        
        self.cancel_btn = tb.Button(self.info_frame, text="Annuler",bootstyle="secondary", command=self.cancel)
        self.cancel_btn.grid(row=8, column=1, pady=5, padx=5)       
        
        
    def cancel(self):
        self.app.geometry("600x400")
        self.info_frame.pack_forget()
    
    
    def show_info(self, event):
        self.app.geometry("600x600")
        self.info_frame.pack()
        selection = self.table.selection()
        if selection:
            item = self.table.item(selection)
            values = item["values"]
        
            self.matricule.set(str(values[0]))
            self.nom.set(str(values[1]))
            self.prenom.set(str(values[2]))

    def calculate(self):
        if (self.assiduité.get() >= 0.00 and self.assiduité.get() <= 20.00) and (self.discipline.get() >= 0.00 and self.discipline.get() <= 20.00) and (self.animation_cours.get() >= 0.00 and self.animation_cours.get() <= 20.00) and (self.encadrement.get() >= 0.00 and self.encadrement.get() <= 20.00) and (self.prep_cours.get() >= 0.00 and self.prep_cours.get() <= 20.00):
            note = (self.assiduité.get() + self.discipline.get() + self.animation_cours.get() + self.encadrement.get() + self.prep_cours.get()) 
            if note <= 50:
                self.note.set(note)
                self.decision.set("Lent")
            elif note < 70:
                self.note.set(note)
                self.decision.set("moyen")
            else:
                self.note.set(note)
                self.decision.set("rapide")
            
            self.info_frame.pack_forget()
        else:
            messagebox.showerror("Error", "Veuillez entrer des notes entre 0 et 20")
        
        self.update_table()
        
    def update_table(self):
        # for row in self.table.get_children():
        #     self.table.delete(row)

        # for employee in self.employees:
        #     self.table.insert("", "end", values=(employee["id"], employee["last_name"], employee["first_name"], employee["note"], employee["decision"]))
         pass
            
       
        
        
        


app = EmpPerformance()
app.app.mainloop()

            
        