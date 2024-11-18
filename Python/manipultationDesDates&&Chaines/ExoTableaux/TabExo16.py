# Écrivez une fonction longest_word(sentence) qui prend une chaîne 
# sentence et renvoie le mot le plus long dans la chaîne. En cas 
# d'égalité, renvoyez le premier mot le plus long trouvé. 

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

sentence = input("Entrez une phrase: ")
print(longest_word(sentence))