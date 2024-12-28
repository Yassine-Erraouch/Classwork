import ttkbootstrap as tb
from CRUD_App import CRUDApp
import json as js
from tkinter import filedialog
class Menu(tb.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self.file_menu = tb.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="Home", command=lambda: parent.destroy() or CRUDApp().mainloop())
        self.file_menu.add_command(label="Tasks App", command=lambda: parent.destroy() or CRUDApp().mainloop())
        self.file_menu.add_command(label="Save File", command=self.save_file)

    def save_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Json Files", "*.json")])
        if file:
            with open(file, "w") as write_file:
                js.dump(CRUDApp().tasks, write_file, indent=4)
