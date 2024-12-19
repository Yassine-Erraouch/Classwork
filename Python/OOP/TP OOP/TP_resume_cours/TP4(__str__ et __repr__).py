class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def afficher_informations(self):
        return f"Nom: {self.nom}, Age: {self.age}"
    
    def __str__(self):
        return f"Nom: {self.nom}, Age: {self.age}"
    
    def __repr__(self):
        return f"Personne('{self.nom}', {self.age})"
    
    
#creation des objets personne

p1 = Personne("Yassine", 21)
p2 = Personne("Said", 56)
        
#affichage des informations de p1 et p2 aver afficher_informations
print(Personne.afficher_informations(p1))
print(Personne.afficher_informations(p2))

#affichage des informations de p1 et p2 aver __str__
print(p1)
print(p2)

#affichage des informations de p1 et p2 aver __repr__
print(repr(p1))
print(repr(p2))
