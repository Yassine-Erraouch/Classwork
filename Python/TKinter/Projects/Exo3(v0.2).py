import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import sqlite3

# Database setup
connection = sqlite3.connect('students.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    email TEXT
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
        self.name = ttk.StringVar()
        self.age = ttk.StringVar()
        self.email = ttk.StringVar()

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

        ttk.Label(form_frame, text="Name:", bootstyle=INFO).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(form_frame, textvariable=self.name).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(form_frame, text="Age:", bootstyle=INFO).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(form_frame, textvariable=self.age).grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(form_frame, text="Email:", bootstyle=INFO).grid(row=3, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(form_frame, textvariable=self.email).grid(row=3, column=1, padx=10, pady=10)

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

        self.student_table = ttk.Treeview(table_frame, columns=("ID", "Name", "Age", "Email"), bootstyle=INFO)
        self.student_table.heading("ID", text="ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Age", text="Age")
        self.student_table.heading("Email", text="Email")
        self.student_table.column("ID", width=50, anchor=CENTER)
        self.student_table.column("Name", width=150, anchor=W)
        self.student_table.column("Age", width=50, anchor=CENTER)
        self.student_table.column("Email", width=200, anchor=W)
        self.student_table.pack(fill=BOTH, expand=True)

    def register_student(self):
        try:
            cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
                           (self.name.get(), self.age.get(), self.email.get()))
            connection.commit()
            messagebox.showinfo("Success", "Student registered successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_student(self):
        try:
            cursor.execute("UPDATE students SET name=?, age=?, email=? WHERE id=?",
                           (self.name.get(), self.age.get(), self.email.get(), self.student_id.get()))
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
        self.name.set("")
        self.age.set("")
        self.email.set("")

    def show_all_students(self):
        for row in self.student_table.get_children():
            self.student_table.delete(row)

        students = cursor.execute("SELECT * FROM students").fetchall()
        for student in students:
            self.student_table.insert("", END, values=student)

    def search_student(self):
        student = cursor.execute("SELECT * FROM students WHERE id=?", (self.student_id.get(),)).fetchone()
        if student:
            self.name.set(student[1])
            self.age.set(student[2])
            self.email.set(student[3])
        else:
            messagebox.showerror("Error", "Student not found!")

# Run Application
if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = StudentApp(root)
    root.mainloop()

# Close database connection on exit
connection.close()
