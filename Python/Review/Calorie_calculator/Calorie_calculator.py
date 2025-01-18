import ttkbootstrap as tb


class CaloriesCalculator(tb.Window):
    def __init__self(self):
        self.title("Calories Calculator")
        self.style = tb.Style("minty")
    
    
    
        # creating the frames
        self.title_frame = tb.Frame(self)
        self.input_frame = tb.Frame(self)
        self.output_frame = tb.Frame(self)

        
        # packing the frames
        self.title_frame.pack(padx=10, pady=10)
        self.input_frame.pack(padx=10, pady=10)
        self.output_frame.pack(padx=10, pady=10)

        # creating the ui
        self.create_ui()
    def create_ui(self):
        # creating the title labels
        tb.Label(self.title_frame, text="Calories Calculator", bootstyle="primary").pack()
        tb.Label(self.input_frame, text="Choose your meal's ingrendients:").pack()
        
        # creating the input fields
        inputs_list = ["Rice", "Pasta", "Bread", "Potatoes", "Carrot", "Banana", "Apple", "Yogurt", "Eggs", "Chicken", "Beef", "Salmon"]
        
        inputs_list_with_cal = [
            ("Rice", 130), ("Pasta", 131), ("Bread", 265), ("Potatoes", 87), ("Carrot", 41), ("Banana", 89), ("Apple", 52), ("Yogurt", 61), ("Eggs", 155), ("Chicken", 165), ("Beef", 250), ("Salmon", 206)
        ]
        
        for input in inputs_list:
            tb.Checkbutton(self.input_frame, text=input, command=enable_field).grid(row=inputs_list.index(input), column=0)
            tb.Entry(self.input_frame, textvariable=tb.StringVar()).grid(row=inputs_list.index(input), column=1)
            tb.Label(self.input_frame, text="g").grid(row=inputs_list.index(input), column=2)
        
        # creating the calculate buton
        tb.Label(self.input_frame, text="Calculate", command=calculate_cals).grid(row = len(inputs_list) + 1, column=1)
        
        
        # creating the output labels
        tb.Label(self.output_frame, text="Your meal has :").grid(row=0, column=0)
        tb.input(self.output_frame, textvariable=tb.StringVar(), state="readonly").grid(row=0, column=1)
        tb.Label(self.output_frame, text="Kilo Calories").grid(row=0, column=2)




# testing code
app = CaloriesCalculator()
app.mainloop()