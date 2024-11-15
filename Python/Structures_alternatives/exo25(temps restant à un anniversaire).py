import datetime

#ask user for a day and a month
while True:
    try:
        birthDay, birthMonth = int(input("Entrez le jour de votre naissance (1-31) : ")), int(input("Entrez le mois de votre naissance (1-12) : "))
        if birthDay in list(range(1,32)) and birthMonth in list(range(1,13)):
            break
    except:
        print("entrez des valeurs valides")

#get current date
currentDate = datetime.date.today()

#calculate the birthday date this year
bDayThisYear = datetime.date(currentDate.year, birthMonth, birthDay)

#calculate the birthday date next year
bDayNextYear = datetime.date(currentDate.year + 1, birthMonth, birthDay)

#check if the birthday is already passed this year
if bDayThisYear < currentDate:
    bDay = bDayNextYear
else:
    bDay = bDayThisYear

#calculate the number of days until the birthday
daysUntilBirthday = (bDay - currentDate).days

#display the result
if daysUntilBirthday == 0:
    print("Joyeux anniversaire !")
else:
    print(f"Il vous reste {daysUntilBirthday} jours jusqu à votre prochain anniversaire.")