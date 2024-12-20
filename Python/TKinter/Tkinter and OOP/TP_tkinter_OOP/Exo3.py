from tkinter import *
from tkinter import messagebox, Treeview, Combobox
import sqlite3 as sl3

#---------------------------Function block----------------------------------

def show_entry_fields():
    #when the insert button is clicked, entry fields will appear in the buttons_frame 
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    gender_cb.grid(row=1, column=1, padx=5, pady=5)
    city_entry.grid(row=2, column=1, padx=5, pady=5)
    email_entry.grid(row=3, column=1, padx=5, pady=5)
    phone_entry.grid(row=4, column=1, padx=5, pady=5)
    address_entry.grid(row=5, column=1, padx=5, pady=5)
    course_entry.grid(row=6, column=1, padx=5, pady=5)
    
    submit_btn.grid(row=7, column=1, padx=5, pady=5)
    cancel_btn.grid(row=7, column=2, padx=5, pady=5)

def submit_entry():
    #when the submit button is clicked a success pop up will show up when all the info has been filled
    #the info will be added to the database and the entry fields will be hidden
    #or a fail pop up will show up when there is an empty field

    if name_entry.get() == "" or gender_cb.get() == "" or city_entry.get() == "" or email_entry.get() == "" or phone_entry.get() == "" or address_entry.get() == "" or course_entry.get() == "":
        messagebox.showerror("Error", "Please fill all the fields.")
        return
    else:
        table.insert("", END, values=(name_entry.get(), gender_cb.get(), city_entry.get(), email_entry.get(), phone_entry.get(), address_entry.get(), course_entry.get()))
        messagebox.showinfo("Success", "User added successfully.")
        name_entry.delete(0, END)
        gender_cb.set("")
        city_entry.set("")
        email_entry.set("")
        phone_entry.set("")
        address_entry.set("")
        course_entry.set("")
        name_entry.grid_remove()
        gender_cb.grid_remove()
        city_entry.grid_remove()
        email_entry.grid_remove()
        phone_entry.grid_remove()
        address_entry.grid_remove()
        course_entry.grid_remove()
        submit_btn.grid_remove()
        cancel_btn.grid_remove()

#creating the window

window = Tk()
window.title("User information")
window.geometry("500x300")
window.resizable(False, False)





#creating the frames
    #creating the table frame
table_frame = Frame(window)
buttons_frame = Frame(window)

#packing the frames
table_frame.pack(pady= 10)
buttons_frame.pack(pady= 10)

#creating the table
    #creating the database
conn = sl3.connect("users.db")
cursor = conn.cursor()
  
cursor.execute("""CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
               gender TEXT,
               city TEXT,
               email TEXT,
               phone TEXT,
               address TEXT,
               course TEXT
              )""") 

  #creating the table
table = Treeview(table_frame, columns=("id", "name", "gender", "city", "email", "phone", "address", "course"), show="headings")
table.heading("id", text="ID")
table.heading("name", text="Name")
table.heading("gender", text="Gender")
table.heading("city", text="City")
table.heading("email", text="Email")
table.heading("phone", text="Phone")
table.heading("address", text="Address")
table.heading("course", text="Course")
table.pack()

#creating the buttons
    #creating the insert button
insert_btn = Button(buttons_frame, text="Insert", bootstyle="success", command=show_entry_fields)
insert_btn.pack(side=LEFT, padx=5)
    #creating the Delete button
delete_btn = Button(buttons_frame, text="Delete", bootstyle="danger", command=delete_info)    
delete_btn.pack(side=LEFT, padx=5)


#creating the entry fields and labels

name_label = Label(buttons_frame, text="Name:")
name_entry = Entry(buttons_frame)

gender_label = Label(buttons_frame, text="Gender:")
gender_cb = Combobox(buttons_frame, values=["Male", "Female"])

city_label = Label(buttons_frame, text="City:")
city_entry = Entry(buttons_frame)

email_label = Label(buttons_frame, text="Email:")
email_entry = Entry(buttons_frame)

phone_label = Label(buttons_frame, text="Phone:")
phone_entry = Entry(buttons_frame)

address_label = Label(buttons_frame, text="Address:")
address_entry = Entry(buttons_frame)

course_label = Label(buttons_frame, text="Course:")
course_entry = Entry(buttons_frame)

#creating the submit and cancel buttons

submit_btn = Button(buttons_frame, text="Submit", bootstyle="success", command=submit_entry)
cancel_btn = Button(buttons_frame, text="Cancel", bootstyle="danger", command=cancel_entry)
