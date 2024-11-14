import datetime

#ask user for a date (dd/mm/yyyy)
while True:
    try:
        date, nDays = input("Entrez une date au format jj/mm/aaaa: "), int(input("Entrez un nombre de jours: "))
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
        break
    except:
        print("La date n'est pas au bon format. Veuillez réessayer.")

#calculate the date in the past
pastDate = date - datetime.timedelta(days=nDays)
print("La date dans le passe est", pastDate.strftime("%d/%m/%Y"))