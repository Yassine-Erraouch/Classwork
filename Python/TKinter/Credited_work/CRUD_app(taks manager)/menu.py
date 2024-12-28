import ttkbootstrap as tb
from CRUD_App import CRUDApp
from dbManager import DataBaseManager
import json as js
from tkinter import filedialog, messagebox



class MainWindow(tb.Window): # Creating the main window
    def __init__(self):
        super().__init__(themename="minty")
        self.title("Task Manager")
        self.geometry("800x600")
        
        self.db = DataBaseManager() # creating an instance of DataBaseManager
        
        self.create_menu() # creating the menu


        self.home_frame = tb.Frame(self)
        self.home_frame.pack(padx=10, pady=10, fill="both", expand=True)
        tb.Label(self.home_frame, text="Task Manager",font=("arial",24)).pack(pady=10, padx=10)
        tb.Label(self.home_frame, text="Use the menu bar to navigate", font=("arial",18)).pack(pady=10, padx=10)
        self.app_frame = tb.Frame(self)

    def create_menu(self): # method to create the menu
        menu_bar = tb.Menu(self)
        
        main_menu = tb.Menu(menu_bar, tearoff=0)
        
        main_menu.add_command(label="Home", command=self.home)
        main_menu.add_command(label="Open Tasks App", command=self.open_tasks_app)
        main_menu.add_command(label="Save File", command=self.save_file)
        main_menu.add_command(label="Exit", command=self.destroy)
        
        menu_bar.add_cascade(label="Menu", menu=main_menu)
        
        self.config(menu=menu_bar)
       
    def home(self):
        self.home_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    def open_tasks_app(self):
        self.home_frame.pack_forget()
        app = CRUDApp()
        app.pack(fill="both", expand=True)
        
    
    def save_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Json Files", "*.json")])
        if file:
            try:
                data= self.db.read_all()
                data_list = [{"id":row[0], "title": row[1] ,"description":row[2], "priority":row[3], "status":row[4], "due_date":row[5]} for row in data]
                with open(file, "w") as write_file:
                    js.dump(data_list, write_file, indent=4)
                    messagebox.showinfo("Success", "File saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {e}")
    

        
        
    def save_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Json Files", "*.json")])
        if file:
            with open(file, "w") as write_file:
                js.dump(CRUDApp().tasks, write_file, indent=4)


app = MainWindow()
app.mainloop()