import datetime
#ask user for a date
date = input("Entrez une date au format jj/mm/aaaa: ")
#check if the date is valid
try:
    datetime.datetime.strptime(date, "%d/%m/%Y")
    print("La date est valide.")
except ValueError:
    print("La date n'est pas valide.")
date = datetime.datetime.strptime(date, "%d/%m/%Y")
#check if the date is at the end of the month
if date + datetime.timedelta(days=1) == datetime.datetime(date.year, date.month + 1, 1):
    print("La date tombe en fin du mois.")
else:
    print("La date ne tombe pas en fin du mois.")
