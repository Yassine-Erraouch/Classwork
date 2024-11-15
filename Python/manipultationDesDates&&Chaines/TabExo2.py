# Demandez à l'utilisateur de saisir deux dates au format DD-MM-YYYY 
# et calculez la différence en jours entre les deux dates.

import datetime

#ask user for two dates in the format dd/mm/yyyy
while True:
    try:
        date1, date2= input("Entrez une date au format jj/mm/aaaa: "), input("Entrez une date au format jj/mm/aaaa: ")
        date1, date2 = datetime.datetime.strptime(date1, "%d/%m/%Y"),  datetime.datetime.strptime(date2, "%d/%m/%Y")
        break
    except:
        print("La date n'est pas au bon format. Veuillez réessayer.")

#calculate the difference between the two dates
difference = date1 - date2
if difference.days < 0:
    difference = -difference
print("La difference entre les deux dates est de", difference.days, "jours.")