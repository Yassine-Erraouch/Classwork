# Écrire une fonction qui prend une date et un nombre de jours comme 
# paramètres et renvoie la date après avoir ajouté le nombre de jours 
# spécifié

import datetime

#ask user for a date and a number of days
while True:
    try:
        date, days = input("Entrez une date au format jj/mm/aaaa: "), int(input("Entrez un nombre de jours: "))
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
        if days >= 0: 
            break
    except:
        print("La date n'est pas au bon format. Veuillez réessayer.")

#calculate the date in the future
def getFutureDate(date, days):
    futureDate = date + datetime.timedelta(days=days)
    return("La date dans le futur est", futureDate.strftime("%d/%m/%Y"))

print(getFutureDate(date, days))