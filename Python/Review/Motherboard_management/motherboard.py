from abc import ABC, abstractmethod


# Classe abstraite Composant
class Composant(ABC):
    def __init__(self, id, nom, marque, prix):
        if id <= 0:
            raise ValueError("L'identifiant doit être supérieur à 0.")
        if not nom:
            raise ValueError("Le nom ne peut pas être vide.")
        if prix <= 0:
            raise ValueError("Le prix doit être positif.")
        
        self.id = id
        self.nom = nom
        self.marque = marque
        self.prix = prix

    @abstractmethod
    def afficher_details(self):
        pass

    def modifier_details(self, nom=None, marque=None, prix=None):
        if nom:
            self.nom = nom
        if marque:
            self.marque = marque
        if prix and prix > 0:
            self.prix = prix

    def __str__(self):
        return f"{self.nom} ({self.marque}), Prix: {self.prix} €"


# Classe Processeur
class Processeur(Composant):
    def __init__(self, id, nom, marque, prix, frequence, nombre_coeurs):
        super().__init__(id, nom, marque, prix)
        if frequence <= 0:
            raise ValueError("La fréquence doit être supérieure à 0.")
        if nombre_coeurs < 1:
            raise ValueError("Le nombre de cœurs doit être au moins 1.")
        
        self.frequence = frequence
        self.nombre_coeurs = nombre_coeurs

    def afficher_details(self):
        print(f"Processeur: {self.nom}, Marque: {self.marque}, Prix: {self.prix} €, "
              f"Fréquence: {self.frequence} GHz, Cœurs: {self.nombre_coeurs}")


# Classe Mémoire
class Memoire(Composant):
    def __init__(self, id, nom, marque, prix, capacite, type_memoire):
        super().__init__(id, nom, marque, prix)
        if capacite <= 0:
            raise ValueError("La capacité doit être supérieure à 0.")
        
        self.capacite = capacite
        self.type_memoire = type_memoire

    def afficher_details(self):
        print(f"Mémoire: {self.nom}, Marque: {self.marque}, Prix: {self.prix} €, "
              f"Capacité: {self.capacite} Go, Type: {self.type_memoire}")


# Classe CarteMere
class CarteMere:
    def __init__(self):
        self.composants = []

    def ajouter_composant(self, composant):
        if any(c.id == composant.id for c in self.composants):
            raise ValueError("Un composant avec cet ID existe déjà.")
        self.composants.append(composant)

    def afficher_composants(self):
        for composant in self.composants:
            print(composant)

    def calculer_valeur_totale(self):
        return sum(c.prix for c in self.composants)


# Exemple d'utilisation
if __name__ == "__main__":
    # Création de composants
    proc = Processeur(1, "Ryzen 5", "AMD", 200, 3.5, 6)
    ram = Memoire(2, "HyperX Fury", "Kingston", 80, 16, "DDR4")
    
    # Création de la carte mère et ajout des composants
    carte_mere = CarteMere()
    carte_mere.ajouter_composant(proc)
    carte_mere.ajouter_composant(ram)

    # Affichage des composants
    print("Composants sur la carte mère:")
    carte_mere.afficher_composants()

    # Calcul de la valeur totale
    print(f"Valeur totale des composants: {carte_mere.calculer_valeur_totale()} €")
