class Voiture:
    
    def __init__(self, brand, model, top_speed):
        self.__brand = brand
        self.__model = model
        self.__top_speed = top_speed
        
    def get_top_speed(self):
        return f"The top speed of the {self.__brand} {self.__model} is {self.__top_speed} km/h"
    
    def set_top_speed(self, new_top_speed):
        self.__top_speed = new_top_speed
    
    
#creation des objets voiture

v1 = Voiture("Porsche", "911 Carrera", 292)
v2 = Voiture("Ferrari", "F50", 325)

#affichage des informations de v1 et v2
print(v1.get_top_speed())
print(v2.get_top_speed())

#modification des vitesses de v1 et v2

v1.set_top_speed(300)
v2.set_top_speed(350)   

#affichage des informations de v1 et v2
print(v1.get_top_speed())
print(v2.get_top_speed())