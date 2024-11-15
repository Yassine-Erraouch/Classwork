# Demander à l'utilisateur de saisir une date au format YYYY-MM-DD et 
# afficher quel jour de la semaine correspond à cette date.

import datetime

#ask user for a date
while True:
    try:
        date = input("Entrez une date au format jj/mm/aaaa: ")
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
        break
    except:
        print("La date n'est pas au bon format. Veuillez réessayer.")

#find out what day of the week it is
day = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
print("La date correspond au", day[date.weekday()])




