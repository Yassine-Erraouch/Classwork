import tkinter as tk

window = tk.Tk()
window.title("Exo 7")
window.geometry("300x150")
message = tk.StringVar(window, 'Hello world!')
def show_message():
    tk.Label(window, textvariable=message).grid(row = 0, column = 0, padx= 30, pady= 20)
button = tk.Button(window, text = "click on me", width= 12, command= show_message).grid(row = 1, column = 0, padx= 30, pady= 20)


window.mainloop()