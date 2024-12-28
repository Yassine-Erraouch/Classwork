import ttkbootstrap as tb
from tkinter import messagebox, filedialog, simpledialog
import json
from dbManager import DataBaseManager
from datetime import *


class CRUDApp(tb.Window):
    def __init__(self):
        super().__init__(themename="minty")
        self.title('Task Manager')
        # self.geometry("800x600")
        self.db = DataBaseManager() # database instance from dbManager
        
        self.create_ui() # creates the UI
        self.create_treeview() # method to create the treeview
        self.populate_treeview() # method to load initial data into the treeview
        
    def create_ui(self):  # function to create the visual interface
        # creatiing the frames
        self.entry_frame = tb.Frame(self)
        self.button_frame = tb.Frame(self)
        self.table_frame = tb.Frame(self)
        
        # packing the frames
        self.entry_frame.pack(padx=10, pady=10)
        self.button_frame.pack(padx=10, pady=10)
        self.table_frame.pack(padx=10, pady=10)
        
        # creating the variables
        self.id = 0
        
        self.id_var = tb.StringVar()
        self.id_var.set(str(self.id + 1))
        self.title_var = tb.StringVar()
        self.description_var = tb.StringVar()
        self.priority_var = tb.StringVar()
        self.status_var = tb.StringVar()
        self.due_date_var = tb.StringVar()
        
       
        self.create_widgets() # method to create the widgets
        self.create_buttons() # method to create the buttons
        
        
       
       
    
    def create_widgets(self): # function to create the widgets for the entry frame and buttons for the button frame
        # the labels
        tb.Label(self.entry_frame, text="ID:").grid(row=0, column=0, pady=10)
        tb.Label(self.entry_frame, text="Title: ").grid(row=1, column=0, pady=10)
        tb.Label(self.entry_frame, text="Description: ").grid(row=2, column=0, pady=10)
        tb.Label(self.entry_frame, text="Priority: ").grid(row=3, column=0, pady=10)
        tb.Label(self.entry_frame, text="Status: ").grid(row=4, column=0, pady=10)
        tb.Label(self.entry_frame, text="Due Date: ").grid(row=5, column=0, pady=10)
        tb.Label(self.entry_frame, text="To do").grid(row=4, column=2, pady=10)
        tb.Label(self.entry_frame, text="Ongoing").grid(row=4, column=4, pady=10)
        tb.Label(self.entry_frame, text="Done").grid(row=4, column=6, pady=10)
    
        # the entries
        self.id_label = tb.Label(self.entry_frame, textvariable=self.id_var)
        self.title_entry = tb.Entry(self.entry_frame, textvariable=self.title_var)
        self.description_entry = tb.Entry(self.entry_frame, textvariable=self.description_var)
        self.priority_entry = tb.Combobox(self.entry_frame, textvariable=self.priority_var, values=["High", "medium", "low"])
        self.todo_status = tb.Radiobutton(self.entry_frame, variable=self.status_var, value="To Do")
        self.ongoing_status = tb.Radiobutton(self.entry_frame, variable=self.status_var, value="Ongoing")
        self.done_status = tb.Radiobutton(self.entry_frame, variable=self.status_var, value="Done")
        self.due_date_entry = tb.DateEntry(self.entry_frame)
        

        # placing the items using the grid
        self.id_label.grid(row=0, column=1, pady=10)
        self.title_entry.grid(row=1, column=1, pady=10)
        self.description_entry.grid(row=2, column=1, pady=10)
        self.priority_entry.grid(row=3, column=1, pady=10)
        self.todo_status.grid(row=4, column=1, pady=10)
        self.ongoing_status.grid(row=4, column=3, pady=10)
        self.done_status.grid(row=4, column=5, pady=10)
        self.due_date_entry.grid(row=5, column=1, pady=10)

    def create_buttons(self):
        # the buttons
        self.create_button = tb.Button(self.button_frame, text="Create", command=self.create_task)
        self.update_button = tb.Button(self.button_frame, text="Update", command=self.update_task, bootstyle="secondary")
        self.delete_button = tb.Button(self.button_frame, text="Delete", command=self.delete_task, bootstyle="danger")
        
        # placing the buttons
        self.create_button.grid(row=0, column=0, padx=10)
        self.update_button.grid(row=0, column=1, padx=10)
        self.delete_button.grid(row=0, column=2, padx=10)
        
        
        
    def create_treeview(self):
        # the treeview
        self.tasks = tb.Treeview(self.table_frame, columns=("ID", "Title", "Description", "Priority", "Status", "Due Date"), show="headings")
        self.tasks.heading("ID", text="ID")
        self.tasks.heading("Title", text="Title")
        self.tasks.heading("Description", text="Description")
        self.tasks.heading("Priority", text="Priority")
        self.tasks.heading("Status", text="Status")
        self.tasks.heading("Due Date", text="Due Date")
        self.tasks.pack(fill='x', expand=True)

    def populate_treeview(self):
        for task in self.tasks.get_children(): # gets all current elements of the treeview and removes them
            self.tasks.delete(task)
        
        data = self.db.read_all() # fetches data from the database
        
        for record in data:  # inserts data into the treeview 
            self.tasks.insert("", "end", values=record)
    
    
    def create_task(self):
        # fetching all the information from the variables set beforehand
        title = self.title_var.get()
        description = self.description_var.get()
        priority = self.priority_var.get()
        status = self.status_var.get()
        due_date = self.due_date_entry.entry.get()
        creation_date = datetime.now()
        
        messagebox.showinfo('info', f'title: {title}, {type(title)}, description: {description} {type(description)}, priority: {priority}, {type(priority)} status: {status},{type(status)} due_date: {due_date}, {type(due_date)} creation_date: {creation_date}, {type(creation_date)}')
        
        
        # if title == "" or priority == "" or status == "" or due_date == "":
        #     messagebox.showerror("Error", "Please fill in all the fields.")
        #     return
        
        
        
        
        # self.db.create(title, description, priority, status, creation_date, due_date)
   
        
        # self.title_var.set("")
        # self.description_var.set("")
        # self.priority_var.set("")
        # self.status_var.set("")
        # self.due_date_var.set("")
        
        # self.populate_treeview() # updates the treeview after adding a new item
        
        
        
    def update_task(self):
        ask_id = simpledialog.askinteger("Update", "Enter the ID of the task you want to update: ")
        id = ask_id
        # messagebox.showinfo("info", f"{self.db.read_all()}")
        if id is None or id not in [item[0] for item in self.db.read_all()]:
            messagebox.showerror("Error", "Please enter a valid ID.")
            return
        else:
            item = self.db.get_by_id(id)
            messagebox.showinfo("item", f"{item}")
            self.title_var.set(item[1])
            self.description_var.set(item[2])
            self.priority_var.set(item[3])
            self.status_var.set(item[4])
            self.due_date_var.set(item[6])
           
    def delete_task(self):
        ask_id = simpledialog.askinteger("Update", "Enter the ID of the task you want to update: ")
        id = int(ask_id)
        if id is None or id not in self.db.read_all():
            messagebox.showerror("Error", "Please enter a valid ID.")    
            return
        else:
            self.db.delete(id)
            self.populate_treeview()
 
app = CRUDApp()
app.mainloop()