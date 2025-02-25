from abc import ABC, abstractmethod


# Vehicule(ABC): abstract parent class
class Vehicule(ABC):
    def __init__(self, nomClient, matricule, capacité):
        try:
            if isinstance(int, capacité) and capacité >= 0:
                self.nomClient = nomClient
                self.matricule = matricule
                self.capacité = capacité
        except:
            raise ValueError('Capacité invalide')
        
    @abstractmethod
    def cacluclerEfficiency(self):
        pass
    
    def ajusterCapacity(self, valeur):
        try:
            if isinstance(int, valeur) and valeur >= 0:
                self.capacité = valeur
        except:
            raise ValueError('Capacité invalide')



# Voiture: child class of Vehicule
class Voiture(Vehicule):
    def __init__(self, nomClient, matricule, capacité, consommation):
        super().__init__(nomClient, matricule, capacité)
        try:
            if isinstance(float, consommation): 
                self.consommation = consommation
        except:
            raise ValueError('Consommation invalide.')
    
    def cacluclerEfficiency(self):
        pass