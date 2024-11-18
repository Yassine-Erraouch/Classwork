# Créez une fonction find_anagrams(word, word_list) qui prend un mot 
# word et une liste de mots word_list, et retourne une liste de tous les 
# mots de la liste qui sont des anagrammes de word. 

def find_anagrams(word, word_list):
    letters = set(word)
    anagram_words = [w for  w in word_list if set(w)== letters]
    for w in anagram_words:
        print(w)


#getting the word list from txt file
with open('D:\!Coding\Repos\Classwork\Python\manipultationDesDates&&Chaines\AllEnglishWords.txt', 'r') as f:
    word_list = [line.strip().lower() for line in f.readlines()]

#asking user for a word then calling the function:
word = input("Please enter an English word: ")
print(f'Here all the words that are anagrams of {word}: ')
find_anagrams(word, word_list)