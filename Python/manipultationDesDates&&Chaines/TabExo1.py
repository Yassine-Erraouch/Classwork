#Exercice 1
# Écrire une fonction qui prend une date de naissance au format YYYY-
# MM-DD en entrée et renvoie l'âge actuel de la personne. 



import datetime

#ask user for a date
while True: 
    try:
        birthdate = input("Entrez une date au format aaaa/mm/jj: ")  #2005/05/16
        birthdate = datetime.datetime.strptime(birthdate, "%Y/%m/%d")
        break
    except:
        print("La date n'est pas au bon format. Veuillez réessayer.")
#check if birthdate is in the past
if birthdate > datetime.datetime.now():
    print("Error:Entrez une date de naissance valide")
else: 
    #calculate and return the user's age
    age = datetime.datetime.now() - birthdate 
    age = age.days // 365	
    print(f'vous avez {age} ans')
        

