import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#----------------------------------------functions--------------------------------------
def calculate_bmi():
    try:
        weight = float(weight_input.get())
        height = float(height_input.get()) / 100

        bmi = weight / (height ** 2)
        classification = ""

        if bmi < 18.5:
            classification = "Underweight"
            color = "gray"
        elif 18.5 <= bmi < 25:
            classification = "Normal weight"
            color = "green"
        elif 25 <= bmi < 30:
            classification = "Overweight"
            color = "orange"
        else:
            classification = "Obese"
            color = "red"
    except:
        print('please enter valid values')

    output_label.config(text = f"Your BMI is: {bmi:.2f} ")
    classification_label.config(text= f'{classification}',style="primary.TLabel", foreground=color)

#---------------------------------------------------------------------------------------

window = ttk.Window()
window.geometry('400x400')
window.title('BMI Calculator')
style = ttk.Style("minty")

#---------------------------------------widgets-----------------------------------------

#title label
title_label = ttk.Label(window, text= "BMI Calculator", font = ("garamond", 20, "bold"))
title_label.pack(pady=10)

#label and entry field for weight
weight_label = ttk.Label(window, text = "Weight (kg):", font = ("garamond", 12))
weight_label.pack(pady=5)
weight_input = ttk.Entry(window, font = ("garamond", 12), width= 25)
weight_input.pack(pady=5)

#label and entry field for height
height_label = ttk.Label(window, text = "Height (cm):", font= ("garamond", 12))
height_label.pack(pady=5)
height_input = ttk.Entry(window, font = ("garamond", 12), width= 25)
height_input.pack(pady=5)

#calculate button
style.configure("garamond.TButton", font=("garamond", 12, "bold"), relief= FLAT)
calculate_button = ttk.Button(window, text = "Calculate", style="garamond.TButton", command= calculate_bmi, )
calculate_button.pack(pady=5)

#output label
output_label = ttk.Label(window, text= "Your BMI is:", font = ("garamond", 12))
output_label.pack(pady=5)

#classification label
classification_label = ttk.Label(window, text= "Classification:", font = ("garamond", 12))
classification_label.pack(pady=5)

#---------------------------------------mainloop----------------------------------------

window.mainloop()