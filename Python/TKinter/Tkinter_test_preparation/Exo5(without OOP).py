from tkinter import *
from tkinter import ttk
import tkcolorpicker as tkcp

# Function to open the color picker and display the selected color
def select_color():
    color = tkcp.askcolor()[1] # askcolor() returns (color, color_name)
    selected_color.set(f"Selected Color : {color}")
    selected_color_label.config(bg=color)






# creating a window

window = Tk()
window.title("Color Picker")
window.geometry("300x150")

# creating a font
font_regular = ("garamond", 14)
font_lg_bold = ("garamond", 16, "bold")

# creating a label to display the selected color and the accompanying stringVar()
selected_color = StringVar()
selected_color.set("Select a color")
selected_color_label = Label(window, textvariable=selected_color, font=font_lg_bold, padx=10, pady=10)
selected_color_label.pack(pady=10)

# creating a button
select_btn = Button(window, text="Select Color", font=font_regular, command=select_color)
select_btn.pack(pady=10)

# starting the window
window.mainloop()


