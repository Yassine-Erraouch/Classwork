import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from math import pi, exp

# Main Application Class
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x500")

        # Entry to display calculations
        self.display = ttk.Entry(root, font=("Helvetica", 16), justify="right")
        self.display.pack(fill="x", padx=10, pady=10)

        # Button Layout
        self.create_buttons()

        # Store current input and operation
        self.current_input = ""

    def create_buttons(self):
        button_frame = ttk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ('AC', '<-', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('(', ')', '0', '='),
            ('π', 'Exp', 'x^2', 'C')
        ]

        for row in buttons:
            row_frame = ttk.Frame(button_frame)
            row_frame.pack(expand=True, fill="both")
            for button_text in row:
                button = ttk.Button(row_frame, text=button_text, bootstyle=SECONDARY, command=lambda t=button_text: self.on_button_click(t))
                button.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def on_button_click(self, button_text):
        if button_text == "AC":
            self.current_input = ""
        elif button_text == "C":
            self.current_input = ""
        elif button_text == "<-":
            self.current_input = self.current_input[:-1]
        elif button_text == "=":
            try:
                self.current_input = str(eval(self.current_input))
            except Exception:
                self.current_input = "Error"
        elif button_text == "%":
            try:
                self.current_input = str(eval(f"({self.current_input})/100"))
            except Exception:
                self.current_input = "Error"
        elif button_text == "x^2":
            try:
                self.current_input = str(eval(f"({self.current_input})**2"))
            except Exception:
                self.current_input = "Error"
        elif button_text == "π":
            self.current_input += str(pi)
        elif button_text == "Exp":
            self.current_input += str(exp(1))
        else:
            self.current_input += button_text

        self.display.delete(0, "end")
        self.display.insert(0, self.current_input)

# Run Application
if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = CalculatorApp(root)
    root.mainloop()
