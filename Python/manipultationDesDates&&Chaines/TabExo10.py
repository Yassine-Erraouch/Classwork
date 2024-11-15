# Écrire une fonction qui prend deux heures au format HH:MM et 
# calcule la durée écoulée en heures et minutes entre ces deux heures.

import datetime

def transpiredTime():
    while True:
        try:
            time1, time2 = input("Entrez une heure au format hh:mm: "), input("Entrez une heure au format hh:mm: ")
            time1, time2 = datetime.datetime.strptime(time1, "%H:%M"), datetime.datetime.strptime(time2, "%H:%M")
            if time1 < time2:
                time1, time2 = time2, time1
            break
        except:
            print("La date n'est pas au bon format. Veuillez réessayer.")
            
    #calculate the difference between the two times
    diff = time1 - time2
    durationHr = diff.seconds // 60
    durationMin = diff.seconds % 60
    return durationHr, durationMin


print("La difference entre les deux heures est de", transpiredTime()[0], "heures et", transpiredTime()[1], "minutes.")