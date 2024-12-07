import datetime
#ask user for date in the following format dd/mm/yyyy
while True:
    try:
        date = input("entrez une date au format dd/mm/yyyy: ")
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
        break
    except:
        print("entrez une date valide")

#get the day of the week
day = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
print("le jour est", day[date.weekday()])
