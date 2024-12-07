import datetime

#ask user to enter a date in the future
while True: 
    try:
        date = input("Entrez une date au format jj/mm/aaaa: ")
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
        if date > datetime.datetime.now():
            break
        else: 
            print("La date doitêtre postérieure à aujourd'hui. Veuillez réessayer.")
            continue
    except:
        print("La date n'est pas au bon format. Veuillez réessayer.")

#calculate the number of days remaining
daysRemaining = (date - datetime.datetime.now()).days
print("Il reste", daysRemaining, "jours jusqu'au", date.strftime("%d/%m/%Y"))