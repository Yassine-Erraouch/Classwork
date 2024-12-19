class Animal:
    
    def __init__(self, name):
        self.animal_name = name
    
    def parler(self):
        print("l'animal parle.")

class Chat(Animal):
    
    def parler(self):
        return f"{self.animal_name} says Meow!"
        
class Chien(Animal):
    
    def parler(self):
        return f'{self.animal_name} says Woof!'
        

cat = Chat("Charles")
dog = Chien("Gilbert")

print(cat.parler())
print(dog.parler())