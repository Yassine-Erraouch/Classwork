# Créer une fonction qui prend un mois et une année en entrée, puis 
# affiche toutes les dates de ce mois

import datetime

def showDates():
    #ask user for a month and a year
    while True:
        try:
            month, year = int(input("Entrez un mois (1-12): ")), int(input("Entrez une année: "))
            if month in list(range(1,13)) and year > 0:
                break
        except:
            print("entrez des valeurs valides")

    #convert month and date to datetime object
    date= datetime.datetime(year, month, 1)

    #display the dates of the month
    while date.month == month:
        print(date.strftime("%d/%m/%Y"))
        date += datetime.timedelta(days=1)
showDates()