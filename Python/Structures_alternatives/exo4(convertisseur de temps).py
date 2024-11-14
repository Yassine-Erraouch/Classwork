
    
def convertir_heure(heure_24):
    heure, minute = heure_24.split(":")
    heure = int(heure)
    minute = int(minute)

    if heure < 12:
        suffixe = "AM"
    else:
        suffixe = "PM"
        if heure != 12:
            heure -= 12

    if heure == 0:
        heure = 12

    return f"{heure}:{minute:02d} {suffixe}"

# Exemple d'utilisation
heure_24 = input("entrez l'heure selon le format HH:MM: ")
heure_12 = convertir_heure(heure_24)
print(heure_12)
    