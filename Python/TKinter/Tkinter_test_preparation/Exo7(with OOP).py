from tkinter import *

class TempConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x300")
        
       
        # UI Layout
        self.create_widgets()
        
    def create_widgets(self):
        # creating a font
        font_regular = ("garamond", 14)
        font_lg= ("garamond", 16, "bold")
        # creating the temperature label and entry
        self.temp = StringVar()
        self.temp_label = Label(self.root, text="Input Temerature:", font=font_lg)
        self.temp_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        self.temp_entry = Entry(self.root, textvariable=self.temp, font=font_regular)
        self.temp_entry.place(relx=0.5, rely=0.25, anchor=CENTER)
        # creating a label that shows which unit we're converting from
        self.temp_initial_unit = StringVar()
        self.temp_initial_unit_label = Label(self.root, textvariable=self.temp_initial_unit, font=font_regular)
        self.temp_initial_unit_label.place(relx=0.7, rely=0.25, anchor=CENTER)
        
        # creating a label
        self.temp_unit_label = Label(self.root, text="Select Temperature Unit To Convert From:", font=font_lg)
        self.temp_unit_label.place(relx=0.5, rely=0.35, anchor=CENTER)
        
        # creating the celsuis and fahrenheit radio buttons
        self.temp_unit = StringVar()
        self.celsuis = Radiobutton(self.root, text="Celsuis", variable=self.temp_unit, value="celsuis", font=font_regular, command=self.show_unit)
        self.celsuis.place(relx=0.3, rely=0.5, anchor=CENTER)
        
        self.fahrenheit = Radiobutton(self.root, text="Fahrenheit", variable=self.temp_unit, value="fahrenheit", font=font_regular, command=self.show_unit)
        self.fahrenheit.place(relx=0.6, rely=0.5, anchor=CENTER)
        # creating the convert button
        self.conver_btn = Button(self.root, text= "Convert", command=self.convert_temp, font=font_regular)
        self.conver_btn.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        # creating the result label
        self.result = StringVar()
        self.result_label = Label(self.root, textvariable=self.result)
        self.result_label.place(relx=0.5, rely=0.9, anchor=CENTER)
    
    def show_unit(self):
        if self.temp_unit.get() == "celsuis":
            self.temp_initial_unit.set("Celsuis")
        else:
            self.temp_initial_unit.set("Fahrenheit")
    def convert_temp(self):
        try:
            temp = float(self.temp.get())
            if self.temp_unit.get() == "celsuis":
                fahrenheit = (temp * 9/5) + 32
                self.result.set(f"{temp} Celsuis is equal to {fahrenheit:.2f} Fahrenheit")
            else:
                celsuis = (temp - 32) * 5/9
                self.result.set(f"{temp} Fahrenheit is equal to {celsuis:.2f} Celsuis")
        except ValueError:
            self.result.set("Please enter a valid temperature.")
            
root = Tk()
app = TempConverter(root)
root.mainloop()