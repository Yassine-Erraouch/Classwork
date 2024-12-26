import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk

#----------------------------------------functions--------------------------------------
male = True
def change_gender():
    global male
    if male:
        male = False
        change_gender_btn.configure(image=img_female)
    else:
        male = True
        change_gender_btn.configure(image=img_male)

def clear_entry():
    height_input.delete(0, "end")
def calculate_imc():
    try:
        height = float(height_input.get())
        gender = "male" if male else "female"

        if height < 150:
            messagebox.showerror("Error", "Height must be at least 150 cm.")
            return
        ideal_weight = (height - 100) - ((height - 150) / 4) if gender == "male" else (height - 100) - ((height - 150) / 2.5)
        
        ideal_weight_label.config(text=f"Idea weight: {ideal_weight:.2f} kg")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid height.")
    clear_entry()
#---------------------------------------------------------------------------------------
window = ttk.Window()
window.title("IMC Calculator")
window.geometry("400x400")
style = ttk.Style("minty")
#---------------------------------------widgets-----------------------------------------

#creating the images
img_male = ImageTk.PhotoImage(Image.open("Python\TKinter\Tkinter_Practice\src\man.png").resize((50, 100)))
img_female = ImageTk.PhotoImage(Image.open("Python\TKinter\Tkinter_Practice\src\woman.png").resize((50, 100)))

#creating the labels and entry fields
#label for the height input
height_label = ttk.Label(window, text = "Height in cm:", font = ("garamond", 16,"bold"))
height_label.pack(pady=5)

#Entry for the height input
height_input = ttk.Entry(window, font = ("garamond", 12), width= 25)
height_input.pack(pady=5)

#label for the gender
gender_label = ttk.Label(window, text = "Gender:", font=("garamond", 16,"bold"))
change_gender_btn = ttk.Button(window, image=img_male, command=change_gender, bootstyle="light-outline")
change_gender_btn.pack(pady=5)

#calculate button
calculate_btn = ttk.Button(window, text = "Calculate", style="garamond.TButton", command= calculate_imc)
calculate_btn.pack(pady=5)

#label for the weight output
ideal_weight_label = ttk.Label(window, text = "Ideal weight:", font=("garamond", 16,"bold"), foreground="#85c8b5")
ideal_weight_label.pack(pady=5)


#--------------------------------------Mainloop-----------------------------------------
window.mainloop()