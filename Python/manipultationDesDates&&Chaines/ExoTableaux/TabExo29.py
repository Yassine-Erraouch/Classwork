# Écrivez une fonction extraire_chiffres(chaine: str) -> str qui prend une 
# chaîne de caractères et retourne une chaîne composée uniquement 
# des chiffres présents dans la chaîne d’origine. 
 


def extraire_chiffres(str):
    return ''.join([c for c in str if c.isdigit()])

str = input("Enter a string: ")

print(extraire_chiffres(str))