import tkinter as tk

window = tk.Tk()
window.title("Exo 6")
window.geometry("300x150")

def show_message():
    tk.Label(window, text = "hello world!", width= 12).grid(row = 0, column = 0, padx= 30, pady= 20)


tk.Button(window, text = "click on me", width= 12, command= show_message).grid(row = 1, column = 0, padx= 30, pady= 20)


window.mainloop()