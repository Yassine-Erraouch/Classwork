from abc import ABC, abstractmethod
import json, csv


# custom error
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

class Component(ABC):
    def __init__(self, id=int, name=str, brand=str, price=float):
        if  isinstance(id, int) and isinstance(name, str) and isinstance(brand, str) and isinstance(price, float):
            self.id = id
            self.name = name
            self.brand = brand
            self.price = price
        else:
            raise CustomError("Invalid type for id, name, brand or price")
        
    def show_details(self):
        pass
    
    def edit_details(self, nom=None, marque=None, prix=None):
        if nom:
            self.nom = nom
        if marque:
            self.marque = marque
        if prix:
            self.prix = prix
    

    def __str__(self):
        return f"{self.id}, {self.name},  {self.brand}, {self.price} $"   
    

class CPU(Component):
    def __init__(self, id, name, brand, price, frequency=float, cores=int):
        super().__init__(id, name, brand, price)
        if isinstance(cores, int) and isinstance(frequency, float):
            if frequency <= 0 or cores <1:
                raise ValueError("CPU frequency must be greater than 0 and cores must be at least 1.")
            else:
                self.frequency = frequency
                self.cores = cores
        else:
            raise ValueError("Invalid type for cores or frequency.")
        

    def show_details(self):
        return f"CPU: {self.name}\nBrand: {self.brand}\nPrice: {self.price} $\nFrequency: {self.frequency} GHz\nCores: {self.cores}"
    
    def __str__(self):
        return super().__str__() + f", {self.frequency} Ghz , {self.cores} Cores"
    

class Memory(Component):
    def __init__(self, id, name, brand, price, capacity=int, type=str):
        super().__init__(id, name, brand, price)
        if isinstance(capacity, int) and isinstance(type, str) and type in ["DDR3", "DDR4", "DDR5"]:
            if capacity > 0:
                self.capacity = capacity
                self.type = type
            else: 
                raise ValueError("Memory capacity must be greater than 0 GB.")
        else: 
            raise CustomError("Invalid type for capacity or type. Type must be 'DDR3', 'DDR4' or 'DDR5'.")
        
    def show_details(self):
        return f"Memory: {self.name}\nBrand: {self.brand}\nPrice: {self.price} $\nCapacity: {self.capacity} GB\nType: {self.type}"
    
    def __str__(self):
        return super().__str__() + f", {self.capacity} GB, {self.type}"
    

class Motherboard:
    def __init__(self):
        self.components = []
    
    def add_component(self, component):
        if isinstance(component, Component) and component.id not in [c.id for c in self.components]:
            self.components.append(component)
        else:
            raise CustomError("Invalid component type or component already exists.")
        
    def remove_component(self, id):
        if isinstance(id, int):
            for c in self.components:
                if c.id == id:
                    self.components.remove(c)
                    return 
            return f"Component with id {id} not found."
        else:
            raise CustomError("Invalid type for id.")
        
    def update_component(self, id, name=None, brand=None, price=None, frequency=None, cores=None, capacity=None, type=None):
        if isinstance(id, int): 
            for c in self.components:
                if c.id == id:
                    if isinstance(c, CPU):
                        c.edit_details(name, brand, price)
                    if frequency is not None and cores is not None:
                        c.frequency, c.cores = frequency, cores
                    elif isinstance(c, Memory):
                        c.edit_details(name, brand, price)
                        if capacity is not None and type is not None:
                            c.capacity, c.type = capacity, type
        else:
            raise CustomError("Invalid type for id, name, brand, price, frequency, cores, capacity or memory type.")
        
    def show_components(self):
        for c in self.components:
            print(c.show_details())
    
    # finish this method
    def filter_components(self, criteria, value):
        if criteria == "price":
            return [c for c in self.components if c.price == value]
        elif criteria == "brand":
            return [c for c in self.components if c.brand == value]
        else:
            return f"Invalid criteria: {criteria}"
    
    
    def total_value(self):
        value = 0
        if not self.components:
            return f"There are no components on the motherboard."
        else:
            for c in self.components:
                value += c.price
            return f"The total value of the motherboard is {value} $."
        

    def find_component_by_name(self, name):
        if isinstance(name, str):
            if not self.components:
                return f"There are no components on the motherboard."
            else:
                for c in self.components:
                    if c.name == name:
                        return c
                return f"Component with name {name} not found."
            
    def save_to_json(self, filename):
        data = []
        for c in self.components:
            data.append({"id": c.id, "name": c.name, "brand": c.brand, "price": c.price})
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Motherboard saved to {filename}")
    
    def load_from_json(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        for c in data:
            self.add_component(Component(c["id"], c["name"], c["brand"], c["price"]))
        print(f"Motherboard loaded from {filename}")
        
    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "brand", "price"])
            for c in self.components:
                writer.writerow([c.id, c.name, c.brand, c.price])
        print(f"Motherboard saved to {filename}")
        
    
    def __str__(self):
        if not self.components:
            return f"Motherboard with no components."
        else:
            mb_str = ""
            for c in self.components:
                mb_str += f"{c.show_details()}\n "
            return f"Motherboard:\n{mb_str}"
        
        
        
        
        
# creating some cpu and memory objects
# Create a few CPU objects
cpu1 = CPU(id=1, name="Intel i7", brand="Intel", price=300.0, frequency=3.5, cores=8)
cpu2 = CPU(id=2, name="AMD Ryzen 5", brand="AMD", price=250.0, frequency=4.0, cores=6)

# Create a few Memory objects
memory1 = Memory(id=3, name="Corsair Vengeance", brand="Corsair", price=80.0, capacity=16, type="DDR4")
memory2 = Memory(id=4, name="Kingston HyperX", brand="Kingston", price=75.0, capacity=8, type="DDR4")

# Test the methods of CPU class
print(cpu1.show_details())  # Show details of the first CPU
print("_"*50)
print(cpu2)  # Print the second CPU using __str__ method
print("_"*50)
# Test the methods of Memory class
print(memory1.show_details())  # Show details of the first Memory
print("_"*50)
print(memory2)  # Print the second Memory using __str__ method
print("_"*50)


# Create a motherboard object
motherboard = Motherboard()

# Add components to the motherboard
motherboard.add_component(cpu1)
motherboard.add_component(cpu2)
motherboard.add_component(memory1)
motherboard.add_component(memory2)

# Show details of all components on the motherboard
print("All components on the motherboard:")
motherboard.show_components()
print("_"*50)
# Remove a component (e.g., remove memory2)
motherboard.remove_component(4)  # remove memory2

# Show details after removal
print("\nAfter removing Memory2:")
motherboard.show_components()
print("_"*50)
# Update a component (e.g., update cpu1's price)
motherboard.update_component(1, price=320.0)

# Show details after update
print("\nAfter updating CPU1's price:")
motherboard.show_components()
print("_"*50)
# Filter components by price (e.g., filter for components priced 80.0)
filtered_by_price = motherboard.filter_components("price", 80.0)
print("\nFiltered components by price 80.0:")
for component in filtered_by_price:
    print(component)
print("_"*50)
# Save components to a JSON file
motherboard.save_to_json("motherboard.json")

# Save components to a CSV file
motherboard.save_to_csv("motherboard.csv")
