from datetime import datetime

def date_difference(date1, date2):
    diff = (abs(date1 - date2)).days
    return diff
    
date1 = datetime.strptime(input("Entrez une date au format jj/mm/aaaa: "), '%d/%m/%Y')
date2 = datetime.strptime(input("Entrez une date au format jj/mm/aaaa: "), '%d/%m/%Y')

print("La difference entre les deux dates est de", date_difference(date1, date2), "jours.")