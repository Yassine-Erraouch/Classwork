import tkinter as tk

#creating the window
root = tk.Tk()
root.title("Exo 1")
root.geometry("600x400")

#creating the labels and text boxes
label1 = tk.Label(root, text = "Entrez N: ")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text = "Le double de N est: ")
Entry = tk.Entry(root)
#creating the button
button = tk.Button(root, text = "Calculer", command = lambda: on_click())

def on_click():
    try:
        N = int(entry1.get())
        Entry.delete(0, tk.END)
        Entry.insert(0, str(N*2))
    except:
        Entry.delete(0, tk.END)
        Entry.insert(0, "Veuillez entrer un nombre entier")

#packing the elements
label1.grid(row = 0, column = 2)
entry1.grid(row = 0, column = 3)

label2.grid(row = 1, column = 2)
Entry.grid(row = 1, column = 3)

button.grid(row = 2, column = 3, columnspan = 2)
#placing the widgets




root.mainloop()