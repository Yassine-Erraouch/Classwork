# from datetime import datetime, date

# # Demandez à l'utilisateur d'entrer sa date de naissance (jour et mois seulement)
# jour_naissance = int(input("Entrez le jour de votre naissance (1-31) : "))
# mois_naissance = int(input("Entrez le mois de votre naissance (1-12) : "))

# # Récupérez la date actuelle
# date_actuelle = date.today()

# # Calculez la date de l'anniversaire de cette année
# anniversaire_cette_annee = date(date_actuelle.year, mois_naissance, jour_naissance)

# # Calculez la date de l'anniversaire de l'année prochaine
# anniversaire_annee_prochaine = date(date_actuelle.year + 1, mois_naissance, jour_naissance)

# # Vérifiez si l'anniversaire est déjà passé pour cette année
# if anniversaire_cette_annee < date_actuelle:
#     # Si oui, utilisez la date de l'anniversaire de l'année prochaine
#     anniversaire_a_venir = anniversaire_annee_prochaine
# else:
#     # Sinon, utilisez la date de l'anniversaire de cette année
#     anniversaire_a_venir = anniversaire_cette_annee

# # Calculez le nombre de jours jusqu'à l'anniversaire à venir
# jours_jusqu_anniversaire = (anniversaire_a_venir - date_actuelle).days

# # Gérez le cas où l'anniversaire tombe aujourd'hui
# if jours_jusqu_anniversaire == 0:
#     print("Joyeux anniversaire !")
# else:
#     print(f"Il vous reste {jours_jusqu_anniversaire} jours jusqu'à votre prochain anniversaire.")

import datetime

#ask user for a day and a month
while True:
    try:
        birthDay, birthMonth = int(input("Entrez le jour de votre naissance (1-31) : ")), int(input("Entrez le mois de votre naissance (1-12) : "))
        if birthDay in list(range(1,32)) and birthMonth in list(range(1,13)):
            break
    except:
        print("entrez des valeurs valides")

