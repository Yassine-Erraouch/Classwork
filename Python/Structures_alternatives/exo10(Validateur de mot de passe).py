import re
#ask user for password
passWord = input("entrez votre mot de passe: ")

#setting a valid password pattern
validPW = r'^([A-Za-z])(\d)([!@#$%^&*()]).{8,}$'

if re.match(validPW, passWord):
    print("mot de passe valide")
else:
    print("mot de passe non valide")
