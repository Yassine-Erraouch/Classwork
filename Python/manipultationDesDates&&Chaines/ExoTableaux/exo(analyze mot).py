import string

letters = list(string.ascii_lowercase)
vowels = list('aeiouy')
 

def anaylyze_word(word):
    dict_letters = dict()
    word = list(word)
    for letter in word:
        dict_letters[letter] = word.count(letter)
    wordLen = len(word)
    frequentLetter = max(dict_letters, key=dict_letters.get)
    return {"len": wordLen, "most_used": frequentLetter}

word = input("Entrez un mot: ")
print(anaylyze_word(word))
    
            
    