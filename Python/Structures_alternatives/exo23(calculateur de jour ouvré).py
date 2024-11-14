import datetime

#ask the user for a date
while True:
    try:
        date = input("Entrez une date au format jj/mm/aaaa: ")
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
        break
    except:
        print("La date n'est pas au bon format. Veuillez réessayer.")

#check if date is a weekday or a weekend
days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
if date.weekday() < 5:
    print(f"la date {date.strftime('%d/%m/%Y')} est un jour Ouvré. Il est un {days[date.weekday()]}")
else:
    print(f"la date {date.strftime('%d/%m/%Y')} est un weekend. Il est un {days[date.weekday()]}")