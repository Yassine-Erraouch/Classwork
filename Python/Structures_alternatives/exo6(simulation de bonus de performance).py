#ask the user to input their tenure in years and their performance score
while True:
    try:
        tenure = int(input("entrez votre ancinneté en année: "))
        performance = int(input("entrez votre performance: (1-5)"))
        salaire = float(input("entrez votre salaire: "))
        if performance <= 5 :
            break
    except:
        print("entrez une valeur valide")
    
#calculating bonus according to tenure and performance score
if tenure > 5 and performance >= 4:
    bonus = "20%"
    totalSalaire= salaire * 1.2
elif tenure <= 5 and performance >= 4:
    bonus = "10%"
    totalSalaire= salaire * 1.1
else: 
    bonus = "0%"
    totalSalaire= salaire

print("vous avez un bonus de", bonus,"de votre salaire")
print("votre salaire avec bonus est:", totalSalaire)