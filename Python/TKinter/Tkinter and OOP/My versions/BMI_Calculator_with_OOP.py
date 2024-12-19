#---------------------------------Imports-------------------------------------
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#---------------------------------Classes--------------------------------------

class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        if self.height > 0:
            return self.weight / (self.height ** 2)
        return 0 
    
    def bmi_category(self,bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
        
    
class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Body Mass Index Calculator")
        self.root.geometry("400x400")
        self.style = ttk.Style("minty")
    
        #creating the labels and entry fields
        self.weight_label = ttk.Label(root, text="Weight (kg):", font=("Garamond", 12, "bold"))
        self.weight_label.pack(pady=10, padx=5)
        
        self.weight_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.weight_entry.pack(pady=10, padx=5)
        
        self.height_label = ttk.Label(root, text="Height (m):", font=("garamond", 12, "bold"))
        self.height_label.pack(pady=10, padx=5)
        
        self.height_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.height_entry.pack(pady=10, padx=5)
        
        #creating the calculate button
        self.style.configure("garamond.TButton", font=("garamond", 12), relief= FLAT)
        self.calculate_button = ttk.Button(root, text="Calculate BMI", command=self.calculate_bmi, style="garamond.TButton")
        self.calculate_button.pack(pady=10, padx=5)
        
        #creating the result label
        self.result_label = ttk.Label(root, text= "", font=("garamond", 12, "bold"))
        self.result_label.pack(pady=10, padx=5)
        
    def calculate_bmi(self):
        
        try:
            weight = float(self.weight_entry.get())
            height =float(self.height_entry.get())
            
            #cacluclating the bmi using BMICalculator
            bmi_calculator = BMICalculator(weight,height)
            bmi = bmi_calculator.calculate_bmi()
            category = bmi_calculator.bmi_category(bmi)
            
            #showing the results
            result = f"BMI: {bmi:.2f} ({category})"
            self.result_label.config(text= result)
        except ValueError:
            ttk.messagebox.showerror("Error", "Please enter valid weight and height.")
            

#creating the main window

root = ttk.Window()
app = BMIApp(root)
root.mainloop()
            