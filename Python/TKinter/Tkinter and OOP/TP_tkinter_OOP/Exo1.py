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
    id= 0
    def __init__(self, name, price, quantity):
        self.id = id+1
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def Save_info(self):
        cursor.execute("INSERT INTO products (id, name, price, quantity) VALUES (?, ?, ?, ?)", (self.id, self.name, self.price, self.quantity))
        return
    
    def update_info(self):
        cursor.execute("UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?", (self.name, self.price, self.quantity, self.id))
        return
    
    def delete_info(self):
        cursor.execute("DELETE FROM products WHERE id = ?", (self.id,))
        return
    
    
    