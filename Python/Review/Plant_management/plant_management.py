from abc import ABC, abstractmethod
from datetime import datetime
import re

class CustomError(Exception): # error template
    def __init__(self, message, code):
        self.message = message
        self.code = code

class Plante(ABC):
    def __init__(self, nom=str, type=str, derniere_irrigation=str, besoin_irrigation=bool):
        if datetime.strptime(derniere_irrigation, '%Y-%m-%d') :
            self.nom = nom
            self.type = type
            self.derniere_irrigation = derniere_irrigation
            self.besoin_irrigation = besoin_irrigation
        else:
            raise CustomError('Date incorrecte', 400)    
    @abstractmethod
    def detecter_besoin_irrigation(self):
        pass
    
    def __str__(self):
        return f"Nom: {self.nom}, Type: {self.type}, Derniere irrigations: {self.derniere_irrigation}, Besoin irrigations: {self.besoin_irrigation}"
    

class Fleur(Plante):
    def __init__(self, nom, type, derniere_irrigation, besoin_irrigation):
        super().__init__(nom, type, derniere_irrigation, besoin_irrigation)
    def detecter_besoin_irrigation(self):
        derniere_irrigation_date = datetime.strptime(self.derniere_irrigation, '%Y-%m-%d')
        if derniere_irrigation_date - datetime.now() > datetime.timedelta(days=7):
            self.besoin_irrigation = True
        else: 
            self.besoin_irrigation = False
    
    def __str__(self):
        return super().__str__()
        

class Arbre(Plante):
    def __init__(self, nom, type, derniere_irrigation, besoin_irrigation, hauteur):
        super().__init__(nom, type, derniere_irrigation, besoin_irrigation)
        self.hauteur = hauteur
    
    def detecter_besoin_irrigation(self):
        dernier_irrigation_date = datetime.strptime(self.derniere_irrigation, '%Y-%m-%d')
        if self.hauteur in range(1,5) and dernier_irrigation_date - datetime.now() > datetime.timedelta(days=15):
            self.besoin_irrigation = True
        elif self.hauteur in range(5,11) and dernier_irrigation_date - datetime.now() > datetime.timedelta(days=30):
            self.besoin_irrigation = True
        else:
            self.besoin_irrigation = False
    
    def __str__(self):
        return super().__str__() + f", Hauteur: {self.hauteur}"
    
class Cactus(Plante):
    def __init__(self, nom, type, derniere_irrigation, besoin_irrigation, resistance_secheresse=int):
        super().__init__(nom, type, derniere_irrigation, besoin_irrigation)
        if resistance_secheresse not in range(1, 11):
            raise CustomError("la resistance de secheresse doit être comprise entre 1 et 10", 400)
        else:
            self.resistance_secheresse = resistance_secheresse
        
            
    def detecter_besoin_irrigation(self):
        derniere_irrigation_date = datetime.strptime(self.derniere_irrigation, '%Y-%m-%d')
        if (self.resistance_sechresse in range(1,4) and derniere_irrigation_date - datetime.now() > datetime.timedelta(days=30))or (self.resistance_secheresse in range(4,8) and derniere_irrigation_date - datetime.now() > datetime.timedelta(days=45)) or (self.resistance_secheresse in range(8,11) and derniere_irrigation_date - datetime.now() > datetime.timedelta(days=60)):
            self.besoin_irrigation = True
        else:
            self.besoin_irrigation = False
            
    def __str__(self):
        return super().__str__() + f", Resistance secheresse: {self.resistance_secheresse}"
    
class Pépinière:
    def __init__(self):
        self.plantes = []

    def ajouter_plante(self, plante):
        if plante not in self.plantes:
            self.plantes.append(plante)
            return f"La plante {plante} a bien ete ajoute"
        else:
            raise CustomError('La plante existe deja', 400)

    def supprimer_plante(self, plante):
        if plante in self.plantes:
            self.plantes.remove(plante)
            return f"La plante {plante} a bien ete supprime"
        else:
            raise CustomError('La plante n\'existe pas', 400)
    
    def modifier_plante(self, plante, nom=None, type=None, derniere_irrigation=None, besoin_irrigation=None):
        if plante in self.plantes:
            plante.nom = nom
            plante.type = type
            plante.derniere_irrigation = derniere_irrigation
            plante.besoin_irrigation = besoin_irrigation
            return f"La plante {plante} a bien ete modifie"
        else:
            raise CustomError('La plante n\'existe pas', 400)
    
    def rechercher_plante(self, critere):
        for plante in self.plantes:
            if plante.critere == critere:
                return plante
        return f"La plante n'existe pas"
        
    
    def verifier_irrigation(self):
        besoin_irrigation = []
        for plante in self.plantes:
            if not plante.besoin_irrigation:
                besoin_irrigation.append(plante)
        return besoin_irrigation

    def __str__(self):
        return f"{self.plantes}"




fleur1 = Fleur("Tulipe", "Fleur", "2025-01-01", False)
fleur2 = Fleur("Jonquille", "Fleur", "2025-01-13", False)
fleur3 = Fleur("Tournesol", "Fleur", "2025-01-17", False)

arbre1 = Arbre("Pin", "Arbre", "2024-12-15", False, 3)
arbre2 = Arbre("Eucalyptus", "Arbre", "2024-12-07", False, 7)
arbre3 = Arbre("Olivier", "Arbre", "2024-12-01", False, 11)

cactus1 = Cactus("Saguaro   ", "Cactus", "2024-11-30", False, 3)
cactus2 = Cactus("Echinopsis", "Cactus", "2024-11-20", False, 7)
cactus3 = Cactus("Poire de cactus", "Cactus", "2024-11-10", False, 10)

pep = Pépinière()
pep.ajouter_plante(fleur1)
pep.ajouter_plante(fleur2)
pep.ajouter_plante(fleur3)
pep.ajouter_plante(arbre1)
pep.ajouter_plante(arbre2)
pep.ajouter_plante(arbre3)
pep.ajouter_plante(cactus1)
pep.ajouter_plante(cactus2)
pep.ajouter_plante(cactus3)

print(pep.plantes)
