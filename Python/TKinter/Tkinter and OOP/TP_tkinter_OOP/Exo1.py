#------------------------------Imports-------------------------------------
import ttkbootstrap as ttk
import sqlite3 as sl
from ttkbootstrap import Treeview as tv
#------------------------------Setting up the database---------------------
connection = sl.connect('products.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL, quantity INTEGER)')

#------------------------------Classes-------------------------------------
class Product:
    product_id= 0
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def Save_info(self):
        global product_id
        product_id += 1
        if self.name == "" or self.price == "" or self.quantity == "":
            ttk.Messagebox.showerror("Error", "Please fill in all the fields.")
            return
        else:
            cursor.execute("INSERT INTO products (id, name, price, quantity) VALUES (?, ?, ?, ?)", (self.id, self.name, self.price, self.quantity))
            return
    
    def update_info(self):
        if self.name == "" or self.price == "" or self.quantity == "":
            ttk.Messagebox.showerror("Error", "Please fill in all the fields.")
            return
        else:
            confirm_update = ttk.Messagebox.yesno("Confirmation", "Are you sure you want to update this product?")
            if confirm_update:
                cursor.execute("UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?", (self.name, self.price, self.quantity, self.id))
                return
            else:
                return



    def delete_info(self):
        confirm_delete= ttk.Messagebox.yesno("Confirmation", "Are you sure you want to delete this product?")
        if confirm_delete:
            cursor.execute("DELETE FROM products WHERE id = ?", (self.id,))
            return
        else:
            return
    

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Products inventory")
        self.root.geometry("1100x220")
        self.style = ttk.Style("minty")

        #creating the widgets
        self.input_frame = ttk.Frame(self.root, width=20)
        self.treeview_frame = ttk.Frame(self.root, width=10)

        self.input_frame.grid(row=0, column=0, padx=5, pady=5)
        self.treeview_frame.grid(row=0, column=1, padx=5, pady=5)

        #creating the input inputs and labels
        self.id_label = ttk.Label(self.input_frame, text="ID:")
        self.name_label = ttk.Label(self.input_frame, text="Name:") 
        self.price_label = ttk.Label(self.input_frame, text="Price:")
        self.quantity_label = ttk.Label(self.input_frame, text="Quantity:")

        #creating textvariables for the entry widgets
        
        self.txt_name = ttk.StringVar()
        self.txt_price = ttk.StringVar()
        self.txt_quantity = ttk.StringVar()
        
        self.id_entry = ttk.Entry(self.input_frame, textariable=self.Product.product_id, state="readonly")
        self.name_entry = ttk.Entry(self.input_frame, textvariable=self.txt_name)
        self.price_entry = ttk.Entry(self.input_frame, textvariable=self.txt_price)
        self.quantity_entry = ttk.Entry(self.input_frame, textvariable=self.txt_quantity)

        self.id_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.price_label.grid(row=2, column=0, padx=5, pady=5)
        self.quantity_label.grid(row=3, column=0, padx=5, pady=5)

        self.id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.price_entry.grid(row=2, column=1, padx=5, pady=5)
        self.quantity_entry.grid(row=3, column=1, padx=5, pady=5)

        #creating the treeview
        self.treeview = tv(self.treeview_frame, columns=("ID", "Name", "Price", "Quantity"), show="headings")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Name", text="Name")
        self.treeview.heading("Price", text="Price")
        self.treeview.heading("Quantity", text="Quantity")
        self.treeview.grid(row=0, column=0, padx=5, pady=5)

        #creating the buttons
        self.add_button = ttk.Button(self.input_frame, text="Add", command=self.add_product, bootstyle="success")
        self.update_button = ttk.Button(self.input_frame, text="Update", command=self.update_product, bootstyle="info")
        self.delete_button = ttk.Button(self.input_frame, text="Delete", command=self.delete_product, bootstyle="danger") 

        self.add_button.grid(row=4, column=0, padx=2, pady=5)
        self.update_button.grid(row=4, column=1, padx=2, pady=5)
        self.delete_button.grid(row=4, column=2, padx=2, pady=5)

        self.populate_treeview()
    
    def clear_fields(self):
        self.txt_name.set("")
        self.txt_price.set("")
        self.txt_quantity.set("")
        #-----------------------------------Methods------------------------------------
    def add_product(self):
        product= Product(self.name_entry.get(), self.price_entry.get(), self.quantity_entry.get())
        product.Save_info()
        self.clear_fields()
        return

    def update_product(self):
        product= Product(self.name_entry.get(), self.price_entry.get(), self.quantity_entry.get())
        product.update_info()
        self.clear_fields()
        return
    
    def delete_product(self):
        product= Product(self.name_entry.get(), self.price_entry.get(), self.quantity_entry.get())
        product.delete_info()
        self.clear_fields()
        return


    def populate_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            self.treeview.insert("", "end", values=row)
        return

#-----------------------------------Main------------------------------------
root = ttk.Window()
app = StoreApp(root)
root.mainloop()