class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            self.surface = self.largeur * self.longueur
            other.surface = other.largeur * other.longueur
            return self.surface == other.surface
        return False
    
class Circle:
    def __init__(self, rayon):
        self.rayon = rayon
        

#creation des instance rectangle

r1 = Rectangle(10, 20)
r2 = Rectangle(20, 10)
r3 = Rectangle(10, 10)


c1 = Circle(10)

print(r1 == r2)
print(r1 == r3)

print(r1 == c1)