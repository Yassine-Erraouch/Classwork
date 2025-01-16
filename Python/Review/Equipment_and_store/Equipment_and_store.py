import json 






class QuantityExceptionError (Exception):
    def __init__(self):
        self.message= "Initial quantity must be greater than 10"
    


class Equipment:
    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity
        if self.quantity < 10:
            raise QuantityExceptionError
        
        
    def __str__(self):
        return f"{self.code} | {self.name} | {self.price} | {self.quantity}"
    
    def __eq__(self, other):
        return self.code == other.code
        
        
class Store:
    def __init__(self):
        self.eqpt_list=[]
    
    def __str__(self):
        store_str = "Code\t|Product Name\t|Price\t|Quantity\n"
        for eqpt in self.eqpt_list:
            store_str += f"{eqpt.code}\t|{eqpt.name}\t\t|{eqpt.price}\t|{eqpt.quantity} \n"
        return store_str
    
    def __eq__(self, other):
        return self.eqpt_list == other.eqpt.list
    
    def add_eqpt(self, eqpt):
        if eqpt not in self.eqpt_list:
            self.eqpt_list.append(eqpt)
        else:
            print("This product already exists in the store.")
    
    def remove_eqpt(self, eqpt):
        if eqpt in self.eqpt_list:
            self.eqpt_list.remove(eqpt)
        else:
            print("This product does not exist in the store.")
        
    def edit_eqpt_qte(self, eqpt, new_qte):
        if eqpt in self.eqpt_list:
            eqpt.quantity = new_qte
        else:
            print("This product does not exist in the store.")
            
    def search_eqpt(self, code):
        for eqpt in self.eqpt_list:
            if eqpt.code == code:
                print(eqpt)
                return
        raise ValueError("Equipment not found")
            
    def save_to_json(self, filename):
        data = []
        for eqpt in self.eqpt_list:
            data.append({"code": eqpt.code, "name": eqpt.name, "price": eqpt.price, "quantity": eqpt.quantity})
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Store saved to {filename}")


e1 = Equipment("1234", "Hammer", 10, 10)
e2 = Equipment("5678", "Saw", 20, 12)
e3 = Equipment("9012", "Drill", 50, 15)
e4 = Equipment("3456", "Tape measure", 5, 25)
e5 = Equipment("7890", "Wrench", 15, 20)


s = Store()
s.add_eqpt(e1)
s.add_eqpt(e2)
s.add_eqpt(e3)
s.add_eqpt(e4)
s.add_eqpt(e5)

print(s)
s.remove_eqpt(e5)
print(s)
s.edit_eqpt_qte(e3, 20)
print(s)
s.search_eqpt("9012")
s.save_to_json("store.json")
