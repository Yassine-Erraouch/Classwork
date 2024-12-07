import tkinter as tk
import ttkbootstrap as ttk

window = tk.Tk()
window.title("Exo 9")
window.geometry("500x300")

entry_label = ttk.Label(window, text="Enter the value of N: ", bootstyle ="primary")
entry_label.grid(row=0, column=0, padx=20, pady=20)

number_entry = ttk.Entry(window, bootstyle="primary")
number_entry.grid(row=0, column=1, padx=20, pady=20)

result_label = ttk.Label(window, text="Here is the double of N: ", bootstyle="primary")
result_label.grid(row=1, column=0, padx=20, pady=20)

result_entry = ttk.Entry(window, bootstyle="primary")
result_entry.grid(row=1, column=1, padx=20, pady=20)

def calculate_double():
    try:
        n = int(number_entry.get())
        result = n * 2
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid input")

number_entry.bind("<Return>", lambda event: calculate_double())

window.mainloop()