# Créer une fonction qui prend un mois et une année et affiche toutes 
# les dates de weekend (samedi et dimanche) de ce mois. 
from datetime import datetime
try:
    month, year  = int(input("Entrez le mois (1-12): ")), int(input("Entrez l'année: "))
    startDate = datetime(year, month, 1)
    endDate = datetime(year, month + 1, 1)

    while startDate < endDate:
        if startDate.weekday() in [5, 6]:
            print(startDate.strftime("%d/%m/%Y"))
        startDate += datetime.timedelta(days=1)
    
except:
    print("entrez des valeurs valides")

