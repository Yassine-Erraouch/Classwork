import ttkbootstrap as tb
from tkinter import messagebox, ttk
from abc import ABC, abstractmethod
from math import pi

# creating the abstract class

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# rectangle class inheriting from Shape class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width= width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# circle class inheriting from Shape class

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * pi * self.radius



# creating the app class
class AppForm:
    def __init__(self):
        self.root = tb.Window(themename="minty")
        self.root.title("Surface Area Calculator")
        self.root.geometry("400x300")
        
        # creating the frames
        self.shape_option = tb.Frame(self.root)
        self.rectangle_frame = tb.Frame(self.root)
        self.circle_frame = tb.Frame(self.root)
        # packing the frames
        self.shape_option.pack(padx=10, pady=10, fill="x")
        self.rectangle_frame.pack_forget()
        self.circle_frame.pack_forget()
        
# ------------------------------------------------------------------------------------------------------------------------------
        # creating the widgets for the shape_option frame (label and radio buttons)
        # the shape option label
        tb.Label(self.shape_option, text="Select a shape:").grid(row=0, column= 0, padx=10, pady=10)
        
        # # the shape_var for the radio buttons variabel. it has rectangle set as default
        self.shape_var = tb.StringVar()
        self.res_var = tb.StringVar()
        
        # the radio buttons paired with commands to show the according frame
        self.rectangle_radio = tb.Radiobutton(self.shape_option, text="Rectangle", variable=self.shape_var, value="rectangle", command=self.show_frame)
        self.circle_radio = tb.Radiobutton(self.shape_option, text="Circle", variable=self.shape_var, value="circle", command=self.show_frame)
        
        # placing the radio buttons
        self.rectangle_radio.grid(row=0, column=1, padx=10, pady=10)
        self.circle_radio.grid(row=0, column=2, padx=10, pady=10)
# -------------------------------------------------------------------------------------------------------------------------------
        
        
        
        
#-----------------------------------------------------------------------Rectangle frame-----------------------------------------------------
        # the widgets for the rectangle_frame
        
        # the variables for the height and width of the rectangle
        self.rec_height = tb.DoubleVar()
        self.rec_width = tb.DoubleVar()
        self.rec_option = tb.StringVar()
        
        # the labels and entries
        tb.Label(self.rectangle_frame, text="Height").grid(row=0, column=0, padx=10, pady=10)
        self.rec_height_entry = tb.Entry(self.rectangle_frame, textvariable=self.rec_height)
        
        tb.Label(self.rectangle_frame, text="Width").grid(row=1, column=0, padx=10, pady=10)
        self.rec_width_entry = tb.Entry(self.rectangle_frame, textvariable=self.rec_width)
        
        tb.Label(self.rectangle_frame, text="Calculate: ").grid(row=2, column=0, padx=10, pady=10)
        
        self.res_label = tb.Label(self.rectangle_frame, textvariable=self.res_var)      
        
        # the radio buttons for the calculation options

        self.rec_area_radio = tb.Radiobutton(self.rectangle_frame, text="Area", variable=self.rec_option, value="area", command=self.calc_area)
        self.rec_perimeter_radio = tb.Radiobutton(self.rectangle_frame, text="Perimeter", variable=self.rec_option, value="perimeter", command=self.calc_perimeter)
        
        # the hide button for both frames
        self.hide_btn = tb.Button(self.rectangle_frame, text="Hide", bootstyle="secondary", command=self.hide)

        # placing the entries and radio buttons
        self.rec_height_entry.grid(row=0, column=1, padx=10, pady=10)
        self.rec_width_entry.grid(row=1, column=1, padx=10, pady=10)  
        self.rec_area_radio.grid(row=2, column=1, padx=10, pady=10)
        self.rec_perimeter_radio.grid(row=2, column=2, padx=10, pady=10)
        self.res_label.grid(row=3, column=0, columnspan=2, pady=10)
        self.hide_btn.grid(row=4, column=0, padx=10, pady=10)

        

    
# ---------------------------------------------------------------Circle frame----------------------------------------------------------------
        # the widgets for the circle_frame
        
        # variable for the radius of the circle
        
        self.circle_radius = tb.DoubleVar()
        self.circle_option = tb.StringVar()
        
        # the labels and entries
        tb.Label(self.circle_frame, text="Radius").grid(row=0, column=0, padx=10, pady=10)
        tb.Label(self.circle_frame, text="Calculate: ").grid(row=1, column=0, padx=10, pady=10)
        self.circle_radius_entry = tb.Entry(self.circle_frame, textvariable=self.circle_radius)
        
        self.res_label = tb.Label(self.circle_frame, textvariable=self.res_var)
        
       
        
        
        
        # the radio buttons for the calculation options
        self.cir_area_radio = tb.Radiobutton(self.circle_frame, text="Area", variable=self.circle_option , value="area", command=self.calc_area)
        self.cir_perimeter_radio = tb.Radiobutton(self.circle_frame, text="Perimeter", variable=self.circle_option,  value="perimeter", command=self.calc_perimeter)
        
        # the hide button for bothe frames
        self.hide_btn = tb.Button(self.circle_frame, text="Hide", bootstyle="secondary", command=self.hide)
        
        
        # placing the entries and radio buttons
        self.circle_radius_entry.grid(row=0, column=1, padx=10, pady=10)
        self.cir_area_radio.grid(row=1, column=1, padx=10, pady=10)
        self.cir_perimeter_radio.grid(row=1, column=2, padx=10, pady=10)
        self.res_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.hide_btn.grid(row=3, column=0, padx=10, pady=10)
        
# -------------------------------------------------------------------------------------------------------------------------------

        
        
       
        
        
        
    # function for showing frame appropriate to selection
    def show_frame(self):
        if self.shape_var.get() == "rectangle":
            self.circle_frame.pack_forget()
            self.rectangle_frame.pack(padx=10, pady=10, fill="x")
        else:
            self.rectangle_frame.pack_forget()
            self.circle_frame.pack(padx=10, pady=10, fill="x")
        
    
    
    
    
    # function for calculating area
    def calc_area(self):
        if self.shape_var.get() == "rectangle":
            if self.rec_height.get() == "" or self.rec_width.get() == "" or self.rec_height.get() == 0 or self.rec_width.get() == 0:
                self.res_var.set("Please enter height and width")
            else:
                area = Rectangle(self.rec_height.get(), self.rec_width.get()).area()
                self.res_var.set(f'Area: {area: .2f}')
                return
        else:
            if self.circle_radius.get() == "" or self.circle_radius.get() == 0:
                self.res_var.set("Please enter radius")
            else:
                area = Circle(self.circle_radius.get()).area()
                self.res_var.set(f'Area: {area: .2f}')
                return
    
            
        

        
    
    # function for calculating perimeter
    def calc_perimeter(self):
        if self.shape_var.get() == "rectangle":
            if self.rec_height.get() == "" or self.rec_width.get() == "" or self.rec_height.get() == 0 or self.rec_width.get() == 0:
                self.res_var.set("Please enter height and width")
            else:
                perimeter = Rectangle(self.rec_height.get(), self.rec_width.get()).perimeter()
                self.res_var.set(f'Perimeter: {perimeter: .2f}')
        else:
            if self.circle_radius.get() == "" or self.circle_radius.get() == 0:
                self.res_var.set("Please enter radius")
            else:
                perimeter = Circle(self.circle_radius.get()).perimeter()
                self.res_var.set(f'Perimeter: {perimeter: .2f}')
        
        
            
            
    
    # function for hiding the rectangle and circle frames
    def hide(self):
        self.rectangle_frame.pack_forget()
        self.circle_frame.pack_forget()
        # resetting the variables
        self.shape_var.set("")
        self.res_var.set("")
        self.rec_height.set(0.0)
        self.rec_width.set(0.0)
        self.circle_radius.set(0.0)
        self.circle_option.set("")
        self.rec_option.set("")
  
    
     
     
     
        


app = AppForm()
app.root.mainloop()