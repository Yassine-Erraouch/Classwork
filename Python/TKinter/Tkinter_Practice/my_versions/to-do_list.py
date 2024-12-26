import ttkbootstrap as tb
from tkinter import messagebox, ttk


class Shell():
    def __init__(self):
        self.root = tb.Window(themename="litera")
        self.root.title("To-Do List App")
        self.root.geometry("100x300")
        
        
    def create_ui(self):
        # frame creation
        input_frame = tb.Frame(self.root)
        ongoing_tasks_frame = tb.Frame(self.root)
        completed_tasks_frame = tb.Frame(self.root)
        
        # frame packing
        input_frame.pack_forget()
        ongoing_tasks_frame.pack_forget()
        completed_tasks_frame.pack_forget()
        
        
        # widget creation for the input frame
        self.task_var = tb.StringVar() # task string variable
        
        self.task_entry = tb.Entry(input_frame, textvariable=self.task_var) # task entry widget
        self.add_button = tb.Button(input_frame, text="Add", command=self.add_task) # button to add a task
        
        # widget packing for the input frame
        self.task_entry.pack(pady=10)
        self.add_button.pack(pady=10)
        
        # widget creation for the ongoing tasks frame
        self.task_list = tb.Listbox(ongoing_tasks_frame)
        self.complete_button = tb.Button(ongoing_tasks_frame, text="Complete", command=self.complete_task)
        self.delete_button = tb.Button(ongoing_tasks_frame, text="Delete", command=self.delete_task)