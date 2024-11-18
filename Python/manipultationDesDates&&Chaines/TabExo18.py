# Créez une fonction reverse_words(sentence) qui prend une chaîne  
# sentence et renvoie la phrase avec l'ordre des mots inversé, tout en 
# gardant chaque mot dans sa forme originale.

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

sentence = input("Entrez une phrase: ")
print(reverse_words(sentence))