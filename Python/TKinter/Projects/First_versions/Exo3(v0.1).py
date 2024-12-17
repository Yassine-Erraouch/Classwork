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
        self.root.geometry("600x400")

        # Variables
        self.student_id = ttk.StringVar()
        self.name = ttk.StringVar()
        self.age = ttk.StringVar()
        self.email = ttk.StringVar()

        # UI Layout
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry Fields
        ttk.Label(self.root, text="ID:", bootstyle=INFO).grid(row=0, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(self.root, textvariable=self.student_id).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Name:", bootstyle=INFO).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(self.root, textvariable=self.name).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Age:", bootstyle=INFO).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(self.root, textvariable=self.age).grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Email:", bootstyle=INFO).grid(row=3, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(self.root, textvariable=self.email).grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        ttk.Button(self.root, text="Register", bootstyle=SUCCESS, command=self.register_student).grid(row=4, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="Update", bootstyle=WARNING, command=self.update_student).grid(row=4, column=1, padx=10, pady=10)
        ttk.Button(self.root, text="Delete", bootstyle=DANGER, command=self.delete_student).grid(row=5, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="Clear", bootstyle=PRIMARY, command=self.clear_fields).grid(row=5, column=1, padx=10, pady=10)
        ttk.Button(self.root, text="Show All", bootstyle=INFO, command=self.show_all_students).grid(row=6, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="Search", bootstyle=SECONDARY, command=self.search_student).grid(row=6, column=1, padx=10, pady=10)
        ttk.Button(self.root, text="Exit", bootstyle=DANGER, command=self.root.quit).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

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
        students = cursor.execute("SELECT * FROM students").fetchall()
        output = "\n".join([f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Email: {s[3]}" for s in students])
        messagebox.showinfo("All Students", output)

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
