class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def afficher_informations(self):
        return f"Nom: {self.nom}, Age: {self.age}"
    
    
#creation des objets personne

p1 = Personne("Yassine", 21)
p2 = Personne("Said", 56)
        
#affichage des informations de p1 et p2
print(Personne.afficher_informations(p1))
print(Personne.afficher_informations(p2))