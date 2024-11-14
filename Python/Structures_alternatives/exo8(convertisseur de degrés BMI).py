#ask user for weight
while True:
    try:
        weight = float(input("entrez votre poids en kg: "))
        height = float(input("entrez votre taille en m: "))
        break
    except:
        print('Entrez des valeurs valides')

#calculating bmi
bmi = weight/height**2
print(bmi)

if bmi < 18.5:
    print("vous êtes sous-poids")
elif bmi < 24.9:
    print("vous avez un poids normal")
elif bmi <29.9:
    print("vous êtes sur-poids")
else: 
    print("vous êtes obèse")

