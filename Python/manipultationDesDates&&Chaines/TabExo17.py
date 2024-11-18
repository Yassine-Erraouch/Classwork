# Écrivez une fonction replace_word(sentence, old_word, new_word) 
# qui remplace toutes les occurrences de old_word par new_word dans 
# une phrase sentence, en respectant la casse

def replace_word(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)


sentence = input("Entrez une phrase: ")
old_word = input("Entrez le mot à remplacer: ")
new_word = input("Entrez le nouveau mot: ")
print(replace_word(sentence, old_word, new_word))