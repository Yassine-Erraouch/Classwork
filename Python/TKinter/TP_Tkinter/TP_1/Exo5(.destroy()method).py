import tkinter as tk

window= tk.Tk()
window.title("Exo 5")
window.geometry("300x150")
#creating the close window button

def close_window():
    window.destroy()
tk.Button(window, text = "Close windows", width= 14, command= close_window).grid(row = 2, column = 0, padx= 100, pady= 50)

#starting the window
window.mainloop()