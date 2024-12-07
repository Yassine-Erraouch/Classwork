# Écrivez une fonction acronym(phrase) qui prend une phrase et 
# renvoie l'acronyme correspondant en majuscules. 
# Exemple :  
# acronym("As Soon As Possible") # "ASAP" 
# acronym("National Aeronautics and Space Administration") # "NASA"

def acronym(phrase):
    phrase = phrase.upper()
    words = phrase.split()
    acronym_list = list()
    for w in words:
        acronym_list.append(list(w)[0])
    acronym = ''.join(acronym_list)
    return acronym


phrase = input('Enter a sentence: ')


print(f'the acronym for {phrase} is: ')
print(acronym(phrase))