# Écrivez une fonction mot_le_plus_long(phrase: str) -> str qui prend 
# une phrase en entrée et retourne le mot le plus long de cette phrase. 
# S'il y a plusieurs mots avec la même longueur maximale, retournez le 
# premier rencontré

def mot_le_plus_long(phrase):
    phrase = phrase.split()
    sorted_phrase = sorted(phrase, key= len, reverse = True)
    return sorted_phrase[0]

phrase = input("Enter a sentence: ")
print(f"the longest word in your sentence is: '{mot_le_plus_long(phrase)}'")