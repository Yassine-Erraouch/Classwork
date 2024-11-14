import datetime
#ask user for birthdate in the following format dd/mm/yyyy
while True:
    try:
        birthdate = datetime.datetime.strptime(input("Entrez votre date de naissance au format dd/mm/yyyy: "), "%d/%m/%Y")
        break
    except:
        print("Entrez une date valide")

# check if the user is older than 18 years
if datetime.datetime.now().year - birthdate.year >= 18:
    print("Accés Autorisé")
else: 
    print("Accés Refusé")
