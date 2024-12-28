from tkinter import ttk, messagebox, simpledialog
import ttkbootstrap as tb
from student_db import StudentDB
from datetime import *

class StudentManager(tb.Window):
    def __init__(self):
        super().__init__(themename="minty")
        self.title("Student Manager- Filter by Major")
        self.db = StudentDB() # creating an instance of StudentDB
        
        # creating the variables for the entries and radio buttons
        self.name_var = tb.StringVar()
        self.birth_date_var = tb.StringVar()
        self.major_var = tb.StringVar()
        self.filter_radio_var = tb.StringVar()
        
        
        
        self.create_ui() # creating the UI

        self.populate_treeview() # populating the treeview
        
        # self.mainloop()
    
    def create_ui(self):
        # creating frames for the entries, the buttons, and the radio buttons
        self.entry_frame = tb.Frame(self)
        self.button_frame = tb.Frame(self)
        self.radio_frame = tb.Frame(self)
        self.table_frame = tb.Frame(self)
        
        
        self.entry_frame.pack(padx=10, pady=10)
        self.button_frame.pack(padx=10, pady=10)
        self.radio_frame.pack(padx=10, pady=10)
        self.table_frame.pack_forget()
        
        # creating the labels and placing them
        tb.Label(self.entry_frame, text="Name: ").grid(row=0, column=0, pady=10)
        tb.Label(self.entry_frame, text="Birth Date:  ").grid(row=1, column=0, pady=10)
        tb.Label(self.entry_frame, text="Major: ").grid(row=2, column=0, pady=10)
        
        # creating the entries and placing them
        self.name_entry = tb.Entry(self.entry_frame, textvariable=self.name_var)
        self.birth_entry = tb.DateEntry(self.entry_frame, startdate=None)
        self.major_entry = tb.Combobox(self.entry_frame, textvariable=self.major_var, values=["Maths", "Computer Science", "Chemistry"])
        
        self.name_entry.grid(row=0, column=1, pady=10)
        self.birth_entry.grid(row=1, column=1, pady=10)
        self.major_entry.grid(row=2, column=1, pady=10)
        
        
        # creating the add, update, delete, and show buttons and placing them
        self.add_btn = tb.Button(self.button_frame, text="Add Student", command=self.add_student, bootstyle="success")
        self.update_btn = tb.Button(self.button_frame, text="Update Student information", command=self.update_student, bootstyle="secondary")
        self.delete_btn = tb.Button(self.button_frame, text="Delete Student", command=self.delete_student, bootstyle="danger")
        self.show_tv_btn = tb.Button(self.button_frame, text="Show Students", command=self.show_students, bootstyle="primary")
        
        self.add_btn.grid(row=0, column=0, padx=10, pady=10)
        self.update_btn.grid(row=0, column=1, padx=10, pady=10)
        self.delete_btn.grid(row=0, column=2, padx=10, pady=10)
        self.show_tv_btn.grid(row=0, column=3, padx=10, pady=10)
        
        # creating the radio buttons and placing them
        self.filter_radio_var.set("All")
        
        self.all_rb = tb.Radiobutton(self.radio_frame, text="All", variable=self.filter_radio_var, value="All")
        self.Maths_rb = tb.Radiobutton(self.radio_frame, text="Maths", variable=self.filter_radio_var, value="Maths")
        self.compe_sci_rb = tb.Radiobutton(self.radio_frame, text="Computer Science", variable=self.filter_radio_var, value="Computer Science")
        self.Chemistry_rb = tb.Radiobutton(self.radio_frame, text="Chemistry", variable=self.filter_radio_var, value="Chemistry")
        
        self.all_rb.grid(row=0, column=0, padx=10, pady=10)
        self.Maths_rb.grid(row=0, column=1, padx=10, pady=10)
        self.compe_sci_rb.grid(row=0, column=2, padx=10, pady=10)
        self.Chemistry_rb.grid(row=0, column=3, padx=10, pady=10)
        
        
        self.create_treeview() # calling the method within create_ui so that when create_ui is called, the treeview is also created
        self.students.bind("<<TreeviewSelect>>", self.select_student)
    def clear_fields(self):
        self.name_var.set("")
        self.birth_entry.entry.configure(text="")
        self.major_var.set("")
        
        
    def create_treeview(self):
        self.students = tb.Treeview(self.table_frame, columns=("ID","Name","Birth Date", "Major"), show="headings")
        self.students.heading("ID", text="ID")
        self.students.heading("Name", text="Name")
        self.students.heading("Birth Date", text="Birth Date")
        self.students.heading("Major", text="Major")
        self.students.pack(fill='x', expand=True)
        
    def populate_treeview(self):
        for row in self.students.get_children():
            self.students.delete(row)
        
       
        # showing the students according to the filter
        if self.filter_radio_var.get() == "All":
            data = self.db.get_all()
            for student in data:
                self.students.insert("", "end", values=student)
        elif self.filter_radio_var.get() == "Maths":
            data = self.get_by_major("Maths")
            for student in data:
                self.students.insert("", "end", values=student)
        elif self.filter_radio_var.get() == "Computer Science":
            data = self.get_by_major("Computer Science")
            for student in data:
                self.students.insert("", "end", values=student)
        elif self.filter_radio_var.get() == "Chemistry":
            data = self.get_by_major("Chemistry")
            for student in data:
                self.students.insert("", "end", values=student)
            
    def add_student(self):
        # getting all the data from the entries
        name = self.name_var.get()
        birth_date = self.birth_entry.entry.get()
        major = self.major_var.get()
        
        if name == "" or birth_date == "" or major == "":
            messagebox.showerror("Error", "All fields must be filled.")
            return
        else:
            self.db.create(name, birth_date, major)
            self.populate_treeview()
            self.clear_fields()
    
    def select_student(self, event):
        selected = self.students.focus()
        if selected == "": # if nothing is selected
            messagebox.showerror("Error", "Please select a student to update.")
            return
        else:
            # getting the id of the student that is selected
            student = self.students.item(selected)["values"]
            # setting the old data in the entry fields
            self.name_var.set(student[1])
            bd = datetime.strptime(student[2], "%d/%m/%Y")
            self.birth_entry.configure(startdate=bd)
            self.major_var.set(student[3])
    
    
    def update_student(self):
        selected = self.students.focus()
        if selected == "": # if nothing is selected
            messagebox.showerror("Error", "Please select a student to update.")
            return
        else:
            student = self.students.item(selected)["values"]
            student_id = student[0]
            self.name_var.set(student[1])
            bd = datetime.strptime(student[2], "%d/%m/%Y")
            self.birth_entry.configure(startdate=bd)
            self.major_var.set(student[3])
            self.db.update(student[0], self.name_var.get(), self.birth_entry.entry.get(), self.major_var.get())
            self.populate_treeview()
    def delete_student(self):
        selected = self.students.focus()
        if selected == "": # if nothing is selected
            messagebox.showerror("Error", "Please select a student to delete.")
            return
        else:
            ask = messagebox.askyesno("Confirmation", "Are you sure you want to delete this student?")
            if ask:
                student_id = self.students.item(selected)["values"][0]
                self.db.delete(student_id)
                self.populate_treeview()
    
    def show_students(self):
        if self.table_frame.winfo_ismapped():
            self.table_frame.pack_forget()
            self.show_tv_btn.configure(text="Show Students")
        else:
            self.table_frame.pack(padx=10, pady=10)
            self.show_tv_btn.configure(text="Hide Students")
            self.populate_treeview()
        
            

app = StudentManager()
app.mainloop()
        