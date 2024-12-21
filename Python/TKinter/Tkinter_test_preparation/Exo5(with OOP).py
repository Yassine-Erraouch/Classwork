from tkinter import *
from tkinter import ttk
from tkcolorpicker import askcolor

class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker App")
        self.root.geometry("400x300")

        # Variables
        self.selected_color = None

        # UI Layout
        self.create_widgets()
    
    def create_widgets(self):
        # creating a font variable
        font_regular = ("garamond", 14)
        font_lg_bold = ("garamond", 16, "bold")

        # creating a label to display the selected color and the accompanying stringVar()
        self.selected_color = StringVar()
        self.selected_color.set("Select a color")
        self.selected_color_label = Label(self.root, textvariable=self.selected_color, font=font_lg_bold, padx=10, pady=10)
        self.selected_color_label.pack(pady=10)

        # creating a button
        self.select_btn = Button(self.root, text="Select Color", font=font_regular, command=self.select_color)
        self.select_btn.pack(pady=10)
        
    def select_color(self):
        color = askcolor()[1] # askcolor() returns (color, color_name)
        self.selected_color.set(f"Selected Color : {color}")
        self.selected_color_label.config(bg=color)
        
root = Tk()
app = ColorPickerApp(root)
root.mainloop()
