# Écrivez une fonction compter_mots(phrase: str) -> int qui prend une 
# phrase en entrée et retourne le nombre de mots qu'elle contient. Les 
# mots sont séparés par des espaces

def compter_mots(phrase):
    phrase = phrase.split()
    return len(phrase)

phrase = input('Enter a sentence: ')
print(f'the number of words in your sentence is: {compter_mots(phrase)} words')