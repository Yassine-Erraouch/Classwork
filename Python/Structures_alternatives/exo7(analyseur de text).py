#ask the user for a sentence.
phrase = input("entrez une phrase: ")

#check if the sentence has at least 1 vowel
if 'a' or 'e' or 'i' or 'o' or 'u' in phrase.lower():
    print("la phrase contient au moins une voyelle")
else:
    print("la phrase ne contient aucune voyelle")
    
#check if the length of the sentence is a multiple of 3
sentenceWithNoSpaces= phrase.replace(" ","")
if len(sentenceWithNoSpaces)%3 == 0:
    print(f"la longuer de la phrase est : {len(sentenceWithNoSpaces)}")
    print("la longuer de la phrase est un multiple de 3")
else: 
    print(f"la longuer de la phrase est : {len(sentenceWithNoSpaces)}")
    print("la longuer de la phrase n'est pas un multiple de 3")