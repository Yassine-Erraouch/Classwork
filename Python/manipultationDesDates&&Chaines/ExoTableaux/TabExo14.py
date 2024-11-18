# Écrivez une fonction is_palindrome(s) qui prend une chaîne de 
# caractères s et retourne True si la chaîne est un palindrome (c'est-à-
# dire qu'elle se lit de la même manière de gauche à droite et de droite 
# à gauche, en ignorant les espaces, la casse et la ponctuation), et False 
# sinon.



def is_palindrome(s):
    
    return s == s[::-1]

s = input("Entrez une chaîne de caractères: ")
print(is_palindrome(s))