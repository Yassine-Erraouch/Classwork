import tkinter as tk

window = tk.Tk()
window.title("Exo 3")
window.geometry("300x150")
#creating the buttons and placing them using the grid method
tk.Button(window, text = "Button 1", width= 12).grid(row = 0, column = 0, padx= 30, pady= 20)
tk.Button(window, text = "Button 2", width= 12).grid(row = 0, column = 1, padx= 20, pady= 20)
tk.Button(window, text = "Button 3", width= 12).grid(row = 1, column = 0, padx= 30, pady= 20)
tk.Button(window, text = "Button 4", width= 12).grid(row = 1, column = 1, padx= 20, pady= 20)

#starting the window
window.mainloop()
