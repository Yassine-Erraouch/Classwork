#----------------------Classes----------------------

class Voiture:
    nombre_voitures = 0 #Exo2 Q1
    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        Voiture.nombre_voitures += 1
    
    def __str__(self):
        return f"{self.__marque} | {self.__modele} | {self.__annee} | {self.__km}"
    def demarrer(self):
        return f"la {self.__marque} {self.__modele} demarre"
    def rouler(self,km):
        self.__km += km 
        
    def __eq__(car1, car2):
        return car1.__modele == car2.__modele, car1.__marque == car2.__marque
        
#Exo4. Q1
class Camion(Voiture):
    def __init__(self, marque, modele, annee, km, charge_max):
        super().__init__(marque, modele, annee, km)
        self.__charge_max = charge_max
        self.charge = 0
        
    def charger(self, charge):
            self.charge = charge
            return self.charge > self.__charge_max

#Exo 5. Q1
class Moto(Voiture):
    def __init__(self, marque, modele, annee, km):
        super().__init__(marque, modele, annee, km)
        
    def faire_wheelie(self):
        return f"la {self.__marque} {self.__modele} fait wheelie"


#----------------------Programme----------------------

car = Voiture("Porsche", "911" , 1980, 100000)
print(car)
print(car.demarrer())
car.rouler(100)
print(car)
cars = [
    Voiture("Ford", "Mustang", 2010, 20000),
    Voiture("Toyota", "Corolla", 2015, 50000),
    Voiture("Honda", "Civic", 2012, 150000),
]
for car in cars:
    print(car)

print(Voiture.nombre_voitures)

#Exo3. Q2
print(Voiture.__eq__(cars[0], cars[1]))

#Exo4. Q2
camion = Camion("Mercedes", "Actros", 2018, 5000, 1000)
print(camion.charger(3000))

#Exo5. Q2