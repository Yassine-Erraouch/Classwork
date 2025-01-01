import ttkbootstrap as tb
from tkinter import messagebox, ttk, Text
from datetime import *


class BillCreator(tb.Window):
    def __init__(self):
        super().__init__(themename="minty")
        self.title("Bill Creator")
        self.geometry("800x600")


        # creating the variables
        self.radio_var = tb.StringVar()
        self.couscous_var = tb.StringVar(value="Couscous")
        self.tajine_var = tb.StringVar(value="Tajine")
        self.bastila_var = tb.StringVar(value="Bastila")
        self.briouates_var = tb.StringVar(value="Briouates")
        self.hrira_var = tb.StringVar(value="Hrira")
        self.tea_var = tb.StringVar(value="Tea")
        self.coffee_var = tb.StringVar(value="Coffee")
        self.create_ui() # calling a class method that creates the widgets


    def create_ui(self):
        self.entry_frame = tb.Frame(self) # frame for the inputs
        self.output_frame = tb.Frame(self) # frame for the generated bill

        self.entry_frame.pack(padx=10, pady=10, side="left")
        self.output_frame.pack_forget()



                            # creating the widgets for the entry frame
        radios = [
            (self.couscous_radio, self.couscous_var, 0, 0),
            (self.tajine_radio, self.tajine_var, 1, 0),
            (self.bastila_radio, self.bastila_var, 2, 0),
            (self.briouates_radio, self.briouates_var, 3, 0),
            (self.hrira_radio, self.hrira_var, 4, 0),
            (self.tea_radio, self.tea_var, 5, 0),
            (self.coffee_radio, self.coffee_var, 6, 0)]
        Menu_items = [
            ("Couscous", 0, 1),
            ("Tajine", 1, 1),
            ("Bastila", 2, 1),
            ("Briouates", 3, 1),
            ("Hrira", 4, 1),
            ("Tea", 5, 1),
            ("coffee", 6, 1)]
        
        prices= [
            ("30 DH", 0, 2),
            ("45 DH", 1, 2),
            ("30 DH", 2, 2),
            ("40 Dh", 3, 2),    
            ("15 Dh", 4, 2),
            ("10 Dh", 5, 2),
            ("10 Dh", 6, 2)]
        entries = [
            (self.couscous_entry,self.couscous_var, 0, 4),
            (self.tajine_entry,self.tajine_var, 1, 4),
            (self.bastila_entry, self.bastila_var, 2, 4),
            (self.briouates_entry, self.briouates_var , 3, 4),
            (self.hrira_entry, self.hrira_var, 4, 4),
            (self.tea_entry, self.tea_var , 5, 4),
            (self.coffee_entry, self.coffee_var, 6, 4)]


        for (radio_name, var, row, column) in radios: # creating the radios
            radio_name = tb.Radiobutton(self.entry_frame, variable=self.radio_var, value=var.get(), command=self.show_entry)
            radio_name.grid(row=row, column=column, pady=10)
        for (item, row, column) in Menu_items:   # creating the labels
            tb.Label(self.entry_frame, text=item).grid(row=row, column=column, pady=10)
        for (price, row, column) in prices:  # creating the label prices
            tb.Label(self.entry_frame, text=price).grid(row=row, column=column, pady=10)
        
        for (entry, var, row, column) in entries:   # creating the spinbox entries
            entry = tb.Spinbox(self.entry_frame, textvariable=var, width=10, min=0, max=100)
            entry.grid(row=row, column=column, pady=10)

        self.generate_btn = tb.Button(self.entry_frame, text="Generate Bill", command=self.generate_bill)
        self.clear_btn = tb.Button(self.entry_frame, text="Clear", command=self.clear)
    
        self.generate_btn.grid(row=7, column=0, columnspan=2, pady=10)
        self.clear_btn.grid(row=7, column=2, columnspan=2, pady=10)



                            # creating the widgets for the output frame
        output_labels = [
            ("Bill", 0, 0),
            ("Date", 1, 0),
            ("Cost", 2, 0),
            ("Service", 3, 0),
            ("Tax", 4, 0),
            ("Total", 5, 0), 
        ]

        output_entries = [
            (self.bill_entry, 0, 1),
            (self.date_entry, 1, 1),
            (self.cost_entry, 2, 1),
            (self.service_entry, 3, 1),
            (self.tax_entry, 4, 1),
            (self.total_entry, 5, 1),
        ]

        for (label, row, column) in output_labels:
            tb.Label(self.output_frame, text=label).grid(row=row, column=column, pady=10)

        for (entry, row, column) in output_entries:
            entry = tb.Entry(self.output_frame, state="readonly", width=10, background="pink", foreground="black")
            entry.grid(row=row, column=column, pady=10)
    
    def show_entry(self):
        if self.radio_var.get() == "Couscous":
            pass


    def generate_bill(self):
        cost = 0
        service_free = 0
        tax = 0
        total = 0
        date = datetime.now()
        if self.radio_var.get() == "Couscous":
            cost += 30 * self.couscous_entry.get()
        if self.radio_var.get() == "Tajine":
            cost += 45 * self.tajine_entry.get()
        if self.radio_var.get() == "Bastila":
            cost += 30 * self.bastila_entry.get()
        if self.radio_var.get() == "Briouates":
            cost += 40 * self.briouates_entry.get()
        if self.radio_var.get() == "Hrira":
            cost += 15 * self.hrira_entry.get()
        if self.radio_var.get() == "Tea":
            cost += 10 * self.tea_entry.get()
        if self.radio_var.get() == "Coffee":
            cost += 10 * self.coffee_entry.get()

        self.output_frame.pack(padx=10, pady=10, side="right")
        tb.Label(self.output_frame, text="Bill").grid(row=0, column=0, pady=10)

app = BillCreator()
app.mainloop()