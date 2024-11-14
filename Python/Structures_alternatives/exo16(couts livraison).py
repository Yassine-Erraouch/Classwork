#ask for delivery weight and distance in kg and km respectively
while True:
    try:
        weight, distance = float(input("entrez votre poids en kg: ")), float(input("entrez votre distance en km: "))
        break
    except:
        print('Entrez des valeurs valides')
        
#calculating delivery cost
if distance < 100:
    cost = weight*5
elif distance < 500:
    cost = weight*4
elif distance > 500:
    cost = weight*3
else:
    cost = weight*2
    
if weight >20:
    cost += 10

print("le cout de livraison est:", cost,"€")