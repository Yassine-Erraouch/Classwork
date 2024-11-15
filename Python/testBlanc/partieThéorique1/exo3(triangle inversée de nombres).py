try:
    n = int(input("Entrez un nombre : "))
    for i in range(n, 0, -1):
        print("10" * i)
except:
    print('valeur invalides')
    
