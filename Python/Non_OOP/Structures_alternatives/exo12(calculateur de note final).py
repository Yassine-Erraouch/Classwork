#demander des notes
while True: 
    try:
        note1 = int(input('entrez la 1ère note: '))
        note2 = int(input('entrez la 2ème note: '))
        note3 = int(input('entrez la 3ème note: '))
        if (note1 >= 0 and note1 <= 100) and (note2 >= 0 and note2 <= 100) and (note3 >= 0 and note3 <= 100):
            break
    except:
        print('entrez des valeurs valides')
        
moy = (note1+note2+note3)/3
print(f"votre moyenne est {moy}")

if note1 > 80 and note2 >80 and note3 > 80:
    moy += 5

if moy >= 50:
    print('vous avez réussi')
else: 
    print("vous avez échoue")
    
if moy > 90:
    print('félicitations!!')