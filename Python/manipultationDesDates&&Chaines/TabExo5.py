# Écrire un programme qui prend la date actuelle et calcule le nombre 
# de jours restants jusqu'à la fin de l'année. 


import datetime

today = datetime.date.today()

endOfYear = datetime.date(today.year, 12, 31)

daysLeft = (endOfYear - today).days

print("Il reste", daysLeft, "jours jusqu'a la fin de l'annee")