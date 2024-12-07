import tkinter as tk
import ttkbootstrap as ttk
import sqlite3
from ttkbootstrap.constants import *

window = tk.Tk()
window.geometry("800x800+300+100")

frame1 = ttk.Frame(window)
frame1.place(x=0,y=0)

number_label = ttk.Label(frame1, text="Numero Employé :", font=("sans serif",16), padx=20,pady=20)
number_label.grid(row=0,column=0)

name_label = ttk.Label(frame1, text="Nom :", font=("sans serif",16), padx=20,pady=20)
name_label.grid(row=1,column=0)

first_name_label = ttk.Label(frame1, text="Prenom :", font=("sans serif",16), padx=20,pady=20)
first_name_label.grid(row=2,column=0)

gender_label = ttk.Label(frame1, text="Sexe :", font=("sans serif",16), padx=20,pady=20)
gender_label.grid(row=3,column=0)
male_radio = ttk.Radiobutton(frame1, text="Masculin")
female_radio = ttk.Radiobutton(frame1, text="Feminin")

date_label = ttk.Label(frame1, text="Date de naissance :", font=("sans serif",16), padx=20,pady=20)
date_label.grid(row=4,column=0)

function_label = ttk.Label(frame1, text="Fonction :", font=("sans serif",16), padx=20,pady=20)
function_label.grid(row=5,column=0)


window.mainloop()
