import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import sqlite3

# Database setup
connection = sqlite3.connect('students.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    contact_number TEXT,
                    city TEXT,
                    street TEXT,
                    dob TEXT
                )''')
connection.commit()

# Main Application Class
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management App")
        self.root.geometry("800x600")

        # Variables
        self.student_id = ttk.StringVar()
        self.first_name = ttk.StringVar()
        self.last_name = ttk.StringVar()
        self.contact_number = ttk.StringVar()
        self.city = ttk.StringVar()
        self.street = ttk.StringVar()
        self.dob = None

        # UI Layout
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        ttk.Label(self.root, text="Student Management System", bootstyle=PRIMARY, font=("Helvetica", 18, "bold")).pack(pady=20)

        # Form Frame
        form_frame = ttk.Frame(self.root, padding=20)
        form_frame.pack(fill=X)

        # Labels and Entry Fields
        ttk.Label(form_frame, text="ID:", bootstyle=INFO).grid(row=0, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(form_frame, textvariable=self.student_id).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(form_frame, text="First Name:", bootstyle=INFO).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(form_frame, textvariable=self.first_name).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(form_frame, text="Last Name:", bootstyle=INFO).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(form_frame, textvariable=self.last_name).grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(form_frame, text="Contact Number:", bootstyle=INFO).grid(row=3, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(form_frame, textvariable=self.contact_number).grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(form_frame, text="City:", bootstyle=INFO).grid(row=4, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(form_frame, textvariable=self.city).grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(form_frame, text="Street:", bootstyle=INFO).grid(row=5, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(form_frame, textvariable=self.street).grid(row=5, column=1, padx=10, pady=10)

        ttk.Label(form_frame, text="Date of Birth:", bootstyle=INFO).grid(row=6, column=0, padx=10, pady=10, sticky=W)
        self.dob_entry = ttk.DateEntry(form_frame, bootstyle=INFO)
        self.dob_entry.grid(row=6, column=1, padx=10, pady=10)

        # Buttons Frame
        button_frame = ttk.Frame(self.root, padding=20)
        button_frame.pack()

        ttk.Button(button_frame, text="Register", bootstyle=SUCCESS, command=self.register_student).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(button_frame, text="Update", bootstyle=WARNING, command=self.update_student).grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(button_frame, text="Delete", bootstyle=DANGER, command=self.delete_student).grid(row=0, column=2, padx=10, pady=10)
        ttk.Button(button_frame, text="Clear", bootstyle=PRIMARY, command=self.clear_fields).grid(row=0, column=3, padx=10, pady=10)
        ttk.Button(button_frame, text="Show All", bootstyle=INFO, command=self.show_all_students).grid(row=0, column=4, padx=10, pady=10)
        ttk.Button(button_frame, text="Search", bootstyle=SECONDARY, command=self.search_student).grid(row=0, column=5, padx=10, pady=10)
        ttk.Button(button_frame, text="Exit", bootstyle=DANGER, command=self.root.quit).grid(row=0, column=6, padx=10, pady=10)

        # Table Frame
        table_frame = ttk.Frame(self.root, padding=20)
        table_frame.pack(fill=BOTH, expand=True)

        self.student_table = ttk.Treeview(table_frame, columns=("ID", "First Name", "Last Name", "Contact", "City", "Street", "DOB"), bootstyle=INFO)
        self.student_table.heading("ID", text="ID")
        self.student_table.heading("First Name", text="First Name")
        self.student_table.heading("Last Name", text="Last Name")
        self.student_table.heading("Contact", text="Contact")
        self.student_table.heading("City", text="City")
        self.student_table.heading("Street", text="Street")
        self.student_table.heading("DOB", text="Date of Birth")
        self.student_table.column("ID", width=50, anchor=CENTER)
        self.student_table.column("First Name", width=100, anchor=W)
        self.student_table.column("Last Name", width=100, anchor=W)
        self.student_table.column("Contact", width=100, anchor=W)
        self.student_table.column("City", width=100, anchor=W)
        self.student_table.column("Street", width=100, anchor=W)
        self.student_table.column("DOB", width=100, anchor=W)
        self.student_table.pack(fill=BOTH, expand=True)

    def register_student(self):
        try:
            self.dob = self.dob_entry.get_date()
            cursor.execute("INSERT INTO students (first_name, last_name, contact_number, city, street, dob) VALUES (?, ?, ?, ?, ?, ?)",
                           (self.first_name.get(), self.last_name.get(), self.contact_number.get(), self.city.get(), self.street.get(), self.dob))
            connection.commit()
            messagebox.showinfo("Success", "Student registered successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_student(self):
        try:
            self.dob = self.dob_entry.get_date()
            cursor.execute("UPDATE students SET first_name=?, last_name=?, contact_number=?, city=?, street=?, dob=? WHERE id=?",
                           (self.first_name.get(), self.last_name.get(), self.contact_number.get(), self.city.get(), self.street.get(), self.dob, self.student_id.get()))
            connection.commit()
            messagebox.showinfo("Success", "Student updated successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_student(self):
        try:
            cursor.execute("DELETE FROM students WHERE id=?", (self.student_id.get(),))
            connection.commit()
            messagebox.showinfo("Success", "Student deleted successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        self.student_id.set("")
        self.first_name.set("")
        self.last_name.set("")
        self.contact_number.set("")
        self.city.set("")
        self.street.set("")
        self.dob_entry.set_date("")

    def show_all_students(self):
        for row in self.student_table.get_children():
            self.student_table.delete(row)

        students = cursor.execute("SELECT * FROM students").fetchall()
        for student in students:
            self.student_table.insert("", END, values=student)

    def search_student(self):
        student = cursor.execute("SELECT * FROM students WHERE id=?", (self.student_id.get(),)).fetchone()
        if student:
            self.first_name.set(student[1])
            self.last_name.set(student[2])
            self.contact_number.set(student[3])
            self.city.set(student[4])
            self.street.set(student[5])
            self.dob_entry.set_date(student[6])
        else:
            messagebox.showerror("Error", "Student not found!")

# Run Application
if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = StudentApp(root)
    root.mainloop()

# Close database connection on exit
connection.close()
