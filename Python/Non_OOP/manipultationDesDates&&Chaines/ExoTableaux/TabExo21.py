# Écrivez une fonction clean_string(s) qui prend une chaîne s et 
# retourne une nouvelle chaîne avec toutes les ponctuations enlevées 
# et les espaces multiples remplacés par un seul espace
import string

punctuation = list(string.punctuation)

def clean_string(s):
    for c in s:
        if c in punctuation :
            s = s.replace(c,'')
        s = ' '.join(s.split())
    return s
#ask user for a sentence
s = input("Enter a sentence :")

print('the sentence without punctuation and multiple spaces is: ')
print(clean_string(s))
