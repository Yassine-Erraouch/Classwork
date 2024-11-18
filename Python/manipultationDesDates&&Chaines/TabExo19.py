# Écrivez une fonction word_frequency(sentence) qui prend une 
# phrase sentence et retourne un dictionnaire contenant la fréquence 
# de chaque mot (insensible à la casse). Ignorez la ponctuation. 

def word_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    frequency = {}
    for word in words:
        frequency[word] = words.count(word)
    return frequency

sentence = input("Entrez une phrase: ")
print(word_frequency(sentence))