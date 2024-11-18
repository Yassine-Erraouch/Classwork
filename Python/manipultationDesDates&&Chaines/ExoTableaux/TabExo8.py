# Écrire une fonction qui prend deux dates en entrée et calcule le 
# nombre de jours ouvrés (lundi à vendredi) entre ces deux dates.


import datetime

def jourOubvrés():
    #ask user for two dates
    while True:
        try:
            date1, date2= input("Entrez une date au format jj/mm/aaaa: "), input("Entrez une date au format jj/mm/aaaa: ")
            date1, date2 = datetime.datetime.strptime(date1, "%d/%m/%Y"),  datetime.datetime.strptime(date2, "%d/%m/%Y")
            break
        except:
            print("La date n'est pas au bon format. Veuillez réessayer.")
    #calculating the number of days between the two dates
    diff = date1 - date2
    if diff.days < 0:
        diff = -diff

    #counting the number of weekdays
    nbrJours = 0
    for days in range(diff.days+1):
        if days.weekday() < 5:
            nbrJours += 1

    return nbrJours

print(f'le nombres de jours ouvrés entre les deux dates est de {jourOubvrés()}')


