import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x600")

        # Default gender
        self.gender = "male"

        # Title
        ttk.Label(root, text="BMI Calculator", font=("Helvetica", 20, "bold"), bootstyle=PRIMARY).pack(pady=20)

        # Gender Frame
        self.gender_frame = ttk.Frame(root)
        self.gender_frame.pack(pady=10)

        # Load images
        self.male_image = ImageTk.PhotoImage(Image.open("male_icon.png").resize((80, 80)))
        self.female_image = ImageTk.PhotoImage(Image.open("female_icon.png").resize((80, 80)))

        self.male_button = ttk.Button(self.gender_frame, image=self.male_image, bootstyle=INFO, command=lambda: self.set_gender("male"))
        self.male_button.grid(row=0, column=0, padx=20)

        self.female_button = ttk.Button(self.gender_frame, image=self.female_image, bootstyle=INFO, command=lambda: self.set_gender("female"))
        self.female_button.grid(row=0, column=1, padx=20)

        # Input Frame
        self.input_frame = ttk.Frame(root, padding=10)
        self.input_frame.pack(pady=20)

        ttk.Label(self.input_frame, text="Height (cm):", bootstyle=INFO).grid(row=0, column=0, pady=10, sticky=W)
        self.height_entry = ttk.Entry(self.input_frame)
        self.height_entry.grid(row=0, column=1, pady=10)

        ttk.Label(self.input_frame, text="Weight (kg):", bootstyle=INFO).grid(row=1, column=0, pady=10, sticky=W)
        self.weight_entry = ttk.Entry(self.input_frame)
        self.weight_entry.grid(row=1, column=1, pady=10)

        # Calculate Button
        self.calculate_button = ttk.Button(root, text="Calculate BMI", bootstyle=SUCCESS, command=self.calculate_bmi)
        self.calculate_button.pack(pady=20)

        # Result Label
        self.result_label = ttk.Label(root, text="", font=("Helvetica", 16), bootstyle=INFO)
        self.result_label.pack(pady=20)

    def set_gender(self, gender):
        self.gender = gender
        messagebox.showinfo("Gender Selected", f"Gender set to {self.gender.capitalize()}.")

    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get()) / 100  # Convert cm to meters
            weight = float(self.weight_entry.get())
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive.")

            bmi = weight / (height ** 2)
            category = self.get_bmi_category(bmi)

            self.result_label.config(text=f"BMI: {bmi:.2f} ({category})")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

# Run Application
if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = BMICalculator(root)
    root.mainloop()
