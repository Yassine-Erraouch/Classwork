import ttkbootstrap as ttk
import sqlite3 as sl
from ttkbootstrap import Treeview as tv

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Products inventory")
        self.root.geometry("1100x220")
        self.style = ttk.Style("minty")

        #connecting to the SQLite database
        self.conn = sl.connect("store.db")
        self.cursor = self.conn.cursor()
        self.create_table()
        
        #creating the frames
        self.inputs_frame = ttk.Frame(self.root, width=20)
        self.treeview_frame = ttk.Frame(self.root, width=10)
        #placing the frames
        self.inputs_frame.place(x=100, y=10)
        self.treeview_frame.place(x= 400, y=10)
        
        #creating the widgets for the inputs frame
        
            #the id label and entry
        ttk.Label(self.inputs_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = ttk.Entry(self.inputs_frame)
        
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)
        
            #the name label and entry
        ttk.Label(self.inputs_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.txt_name = ttk.StringVar()
        self.name_entry = ttk.Entry(self.inputs_frame, textvariable= self.txt_name)
        
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
            #the price label and entry
        ttk.Label(self.inputs_frame, text="Price:").grid(row=2, column=0, padx=5, pady=5)
        self.txt_price = ttk.StringVar()
        self.price_entry = ttk.Entry(self.inputs_frame, textvariable= self.txt_price)
        
        self.price_entry.grid(row=2, column=1, padx=5, pady=5)
            #the quantity label and entry
        ttk.Label(self.inputs_frame, text="Quantity:").grid(row=3, column=0, padx=5, pady=5)
        self.txt_quantity = ttk.StringVar()
        self.quantity_entry = ttk.Entry(self.inputs_frame, textvariable= self.txt_quantity)
        
        self.quantity_entry.grid(row=3, column=1, padx=5, pady=5)
        
            #the product category combobox
        ttk.Label(self.inputs_frame, text="Category:").grid(row=4, column=0, padx=5, pady=5)
        self.category_cb = ttk.Combobox(self.inputs_frame)
        
        for option in ["Electronics", "Clothing and Accessories", "Home and Kitchen", "Beauty and Personal Care", "Sports and Outdoors", "Books and Media", "Toys and Games", "Food and Beverage"]:
            self.category_cb.insert(0, option)
        self.category_cb.grid(row=4, column=1, padx=5, pady=5)
        
        #creating the buttons for the inputs frame
        ttk.Button(self.inputs_frame, text="Add", bootstyle="success", command=self.add_product).grid(row=5, column=0, padx=5, pady=5)
        ttk.Button(self.inputs_frame, text="Update", bootstyle="warning", command=self.update_product).grid(row=5, column=1, padx=5, pady=5)
        ttk.Button(self.inputs_frame, text="Delete", bootstyle="danger", command=self.delete_product).grid(row=5, column=2, padx=5, pady=5)
        
        #creating a table to show the information
        self.tree = tv(self.treeview_frame, columns=("ID", "Name", "Price", "Quantity", "Category"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Category", text="Category")
        self.tree.grid(row=0, column=0, padx=5, pady=5)
        
        self.tree.bind("<TreeviewSelect>", self.select_row)
        self.load_date()        
        
        
        #methods to create table and load data
        def create_table(self):
            self.cursor.execute("""CREATE TABEL IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL,
                quantity INTEGER,
                category TEXT
            """)
            self.conn.commit()
            
        #fucntion to add product
        def add_product(self):
            try:
                product_id = int(self.entry_id.get())
                name= self.entry_name.get()
                price = float(self.entry_price.get())
                quantity = int(self.entry_quantity.get())
                category = self.category_cb.get()
                
                #inserting into the database
                self.cursor.execute("INSERT INTO products (id, name, price, quantity, category) VALUES (?, ?, ?, ?, ?)",
                                    (product_id, name, price, quantity, category))
                self.conn.commit()
                self.load_data()
                self.clear_inputs()
                ttk.Messagebox.showinfo('Success', "Product added successfully.")
            except sl.IntegrityError:
                ttk.Messagebox.showerror("Error", "Product ID already exists.")
            except ValueError:
                ttk.Messagebox.showerror("Error", "Please enter valid values.")
            
        #function to update products
        def update_product(self):
            try:
                product_id = int(self.entry_id.get())
                name= self.entry_name.get()
                price = float(self.entry_price.get())
                quantity = int(self.entry_quantity.get())
                category = self.category_cb.get()
                
                confirm = ttk.Messagebox.askokcancel("Confirmation", "Are you sure you want to update this product?")
                if confirm:
                    #updating the database
                    self.cursor.execute("UPDATE products SET name = ?, price = ?, quantity = ?, category = ? WHERE id = ?",
                                        (name, price, quantity, category, product_id))
                    self.conn.commit()
                    self.load_data()
                    self.clear_inputs()
                    ttk.Messagebox.showinfo('Success', "Product updated successfully.")
                else:
                    self.clear_inputs()
                    return
            except ValueError:
                ttk.Messagebox.showerror("Error", "Please enter valid values.")
                
        
        #function to delete products
        def delete_product(self):
            try:
                product_id = int(self.entry_id.get())
                self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
                self.conn.commit()
                self.load_data()
                self.clear_inputs()
                ttk.Messagebox.showinfo('Success', "Product deleted successfully.")
            except ValueError:
                ttk.Messagebox.showerror("Error", "Please enter valid values.")
                
        #function to load data from database into the table in treeview
        def load_data(self):
            for row in self.tree.get_children():
                self.tree.delete(row)
            
            self.cursor.execute("SELECT * FROM products")
            for row in self.cursor.fetchall():
                self.tree.insert("", ttk.end, values = row)
                
        #function to select a row in the table and fill the inputs        
        def select_row(self, event):
            selected = self.tree.focus()
            if selected:
                values = self.tree.item(selected, "values")
                self.entry_id.delete(0, ttk.END)
                self.entry_id.insert(0, values[0])
                self.txt_name.set("")
                self.txt_name.set(values[1])
                self.txt_price.set("")
                self.txt_price.set(values[2])
                self.txt_quantity.set("")
                self.txt_quantity.set(values[3])
                self.category_cb.set(values[4])
                
        def clear_inputs()
                 
            
    
       