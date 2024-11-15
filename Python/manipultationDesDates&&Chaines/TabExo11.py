# Écrire un programme qui génère une liste de 10 dates aléatoires dans 
# une plage spécifiée (par exemple, entre 01-01-2000 et 31-12-2023).


from datetime import datetime
from random import randint

def RandomDates(startDate, endDate):
    dateList = []
    for i in range(10):
        date = datetime(randint(startDate.year, endDate.year), randint(startDate.month, endDate.month), randint(startDate.day, endDate.day))
        dateList.append(date.strftime("%d/%m/%Y"))
    for i in dateList:
        print(i)

try:
    startDate = datetime.strptime(input("Entrez la date de début au format jj/mm/aaaa: "), "%d/%m/%Y")
    endDate = datetime.strptime(input('Entrez la date de fin au format jj/mm/aaaa: '), "%d/%m/%Y")
except:
    print('format de date incorrect')

RandomDates(startDate, endDate)