import datetime

#ask user for a date
while True:
    try:
        date = input("Entrez une date au format jj/mm/aaaa: ")
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
        break
    except:
        print("La date n'est pas au bon format. Veuillez réessayer.")

#check if date is at the end of the year
if date + datetime.timedelta(days=1) == datetime.datetime(date.year + 1, 1, 1):
    print(f"La date tombe en fin d'année {date.year}.")
else:
    print(f"La date ne tombe pas en fin d'année {date.year}.")