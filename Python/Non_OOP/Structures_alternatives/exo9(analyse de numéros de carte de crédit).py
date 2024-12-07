#ask user to input their credit card number
while True: 
    try:
        ccn = int(input("entrez votre numéro de carte de crédit: "))
        if len(str(ccn)) == 16:
            break
    except:
        print("entrez une valeur valide")

if list(str(ccn))[0] == "4":
    print("c'est une carte visa")
elif list(str(ccn))[0] == "5":
    print("c'est une carte mastercard")

