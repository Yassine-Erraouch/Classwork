# Écrivez une fonction remplacer_voyelles(chaine: str, symbole: str) -> 
# str qui remplace toutes les voyelles d'une chaîne par un symbole 
# donné.

vowels = list('aieouy')
def remplacer_voyelles(str, symbol):
    for c in str:
        if c in vowels:
            str = str.replace(c,symbol)
    return str

str = input("Enter a string: ") 
while True:
    symbol = input('Enter 1 symbol: ')
    if len(symbol) == 1:
        break
    else:
        print('Enter only 1 symbol.')

print(f'The sentence after replacing the vowels with "{symbol}" is: "{remplacer_voyelles(str,symbol)}"')