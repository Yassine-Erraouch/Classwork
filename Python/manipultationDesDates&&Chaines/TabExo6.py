# Créer une fonction qui prend une date au format DD-MM-YYYY et la 
# convertit en format YYYY/MM/DD

import datetime

def dateFormatConverter():
    while True:
        try:
            date = input("Entrez une date au format jj-mm-aaaa: ")
            date = datetime.datetime.strptime(date, "%d-%m-%Y")
            break
        except:
            print("La date n'est pas au bon format. Veuillez réessayer.")
    return date.strftime("%Y-%m-%d")

print(f'la date en format yyyy-mm-dd est {dateFormatConverter()}')