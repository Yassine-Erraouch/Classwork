import tkinter as tk

#creating the window
root = tk.Tk()
root.title("Exo 2")
root.geometry("300x150")

#creating the labels and text boxes
label1 = tk.Label(root, text = "Entrez la valeur de N: ")
entry1 = tk.Entry(root, width=10)

label2 = tk.Label(root, text = "Diviseurs de N: ")

#creating the button
button = tk.Button(root, text = "Valider l'operation", command = lambda: on_click)

def on_click():
    try: 
        N = int(entry1.get())
        entry1.delete(0, tk.END)
    except:
        entry1.delete(0, tk.END)
        entry1.insert(0, "Veuillez entrer un nombre entier")

    divisors = ""
    for i in range(1, N+1):
        if N % i == 0:
            divisors += str(i) + " "
    label2.config(text = "Diviseurs de N: " + divisors)

#packing the elements
label1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)

label2.grid(row = 1, column = 0, columnspan = 2)

button.grid(row = 2, column = 0, columnspan = 2)
#placing the widgets

root.mainloop()