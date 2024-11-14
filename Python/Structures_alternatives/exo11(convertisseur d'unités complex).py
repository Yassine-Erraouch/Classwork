while True:
    try: 
        value= float(input("entrez une valeur: "))
        unit = input("entrez une unité (cm, m, km, in, ft): ")
        if unit in ['cm', 'm', 'km', 'in', 'ft'] :
            break
    except:
        print("Entrez des valeurs valides")

if unit == 'cm':
    print('valeur en m: ', value/100)
    print('valeur en km: ', value/100000)
    print('valeur en in: ', value*0.3937)
    print('valeur en ft: ', value*0.0328)

elif unit == 'm':
    print('valeur en cm: ', value*100)
    print('valeur en km: ', value/1000)
    print('valeur en in: ', value*39.37)
    print('valeur en ft: ', value*3.28)

elif unit == 'km':
    print('valeur en cm: ', value*100000)
    print('valeur en m: ', value*1000)
    print('valeur en in: ', value*39370)
    print('valeur en ft: ', value*3280.84)

elif unit == 'in':
    print('valeur en cm: ', value*2.54)
    print('valeur en m: ', value*0.0254)
    print('valeur en km: ', value*0.0000254)
    print('valeur en ft: ', value*12)

elif unit == 'ft':
    print('valeur en cm: ', value*30.48)
    print('valeur en m: ', value*0.3048)
    print('valeur en km: ', value*0.0003048)
    print('valeur en in: ', value*12)
    

    