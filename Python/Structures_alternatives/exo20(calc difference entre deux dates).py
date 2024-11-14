import datetime
#ask the user to enter a date in the format dd/mm/yyyy
from datetime import datetime

while True:
    date1 = input("Entrez une date selon le format jj/mm/aaaa: ")
    date2 = input("Entrez une date selon le format jj/mm/aaaa: ")
    try:
        datetime.strptime(date1, "%d/%m/%Y")
        datetime.strptime(date2, "%d/%m/%Y")
        break
    except ValueError:
        print("La date n'est pas au bon format. Veuillez réessayer.")  

date1 = datetime.strptime(date1, "%d/%m/%Y")
date2 = datetime.strptime(date2, "%d/%m/%Y")
#if date 2 is lower than date1 then return an error message
if date2 < date1:
    print("La deuxième date doit être postérieure à la première. Veuillez réessayer.")
    exit()
#calculate the difference between the two dates
difference = date2 - date1
print("La difference entre les deux dates est de", difference.days, "jours.")