# Créez une fonction count_vowels_consonants(s) qui prend une 
# chaîne s et renvoie un dictionnaire contenant le nombre de voyelles 
# et de consonnes
import string

letter_dict = []
def count_vowels_consonants(s):
    letters = list(string.ascii_lowercase)
    for letter in letters:
        letter_count = s.count(letter)
        letter_dict.append((letter, letter_count))
    return letter_dict
        
s = input('Entrez une chaîne de caractères: ')
print(count_vowels_consonants(s))