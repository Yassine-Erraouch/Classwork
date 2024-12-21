import tkinter as tk
from tkcolorpicker import askcolor

# Function to open the color picker and display the selected color
def choose_color():
    color = askcolor()[1]  # askcolor() returns (color, color_name)
    if color:
        color_label.config(text=f"Selected Color: {color}", bg=color)

# Create the main window
parent = tk.Tk()
parent.title("Color Picker")
parent.geometry('300x300')

# Create a label to display the selected color
color_label = tk.Label(parent, text="Selected Color: None", font=("Helvetica", 14), padx=10, pady=10)
color_label.pack(pady=10)

# Create a button to open the color picker
choose_button = tk.Button(parent, text="Choose Color", command=choose_color)
choose_button.pack(pady=10)

# Start the Tkinter event loop
parent.mainloop()
