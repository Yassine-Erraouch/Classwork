#creation de classe
class CompteBancaire:
    #creation d'attribut de classe
    taux_interet = 0.05
    
    #creation de methode d'instance
    def __init__(self, solde):
        self.solde = solde
    def __str__(self):
        return f"Solde: {self.solde}, Taux d'interet: {self.taux_interet}"
    #creation de method pour modifier le taux d'interet
    @classmethod
    def modifier_taux(cls, taux):
        cls.taux_interet = taux
        
#creations des instance de CompteBancaire

c1 = CompteBancaire(1000)
c2 = CompteBancaire(2000)
c3 = CompteBancaire(3000)

print(c1)
print(c2)
print(c3)

CompteBancaire.modifier_taux(0.2)

print(c1)
print(c2)
print(c3)


