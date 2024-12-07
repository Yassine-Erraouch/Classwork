import tkinter as tk

window= tk.Tk()
window.title("Exo 5")
window.geometry("300x150")
#creating the close window button

tk.Button(window, text = "Close windows", width= 14, command= quit).grid(row = 2, column = 0, padx= 30, pady= 20)

#starting the window
window.mainloop()