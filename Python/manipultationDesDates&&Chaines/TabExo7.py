# Écrire une fonction qui prend une chaîne de caractères et vérifie si 
# elle correspond à un format de date valide (YYYY-MM-DD). Si la date 
# est valide, affichez-la sous forme de date Python, sinon indiquez que 
# la date est invalide.

import datetime

def formatChecker():
    try:
        date = input('Entrez une date au format yyyy-mm-dd: ')
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        print("La date est invalide.")
        return
    print(date.strftime("%Y-%m-%d"))

formatChecker()