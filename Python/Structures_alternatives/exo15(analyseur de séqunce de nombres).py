#ask the user for 5 numbers
while True:
    try:
        a,b,c,d,e = int(input("entrez le premier nombre: ")), int(input("entrez le deuxième nombre: ")), int(input("entrez le troisième nombre: ")), int(input("entrez le quatrième nombre: ")), int(input("entrez le cinquième nombre: "))
        break
    except:
        print("entrez des valeurs valides")

if a < b and b < c and c < d and d < e:
    print("la séquence est croissante")

    
if a > b and b > c and c > d and d > e:
    print("la séquence est décroissante")

    
if a == b and b == c and c == d and d == e:
    print("la séquence est identique")
