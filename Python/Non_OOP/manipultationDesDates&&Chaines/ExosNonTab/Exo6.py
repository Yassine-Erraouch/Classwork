#Chiffrement de Vigenère
import string


def encrypt_vigenere(text, keyword):
    alphabet = list(string.ascii_lowercase)
    alphabetnum = list(range(26))
    alphabet_dict = dict(zip(alphabet, alphabetnum))
    keyword = keyword.lower()  # Convert keyword to lowercase
    keyword_index = 0  # Initialize keyword index
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            encrypted_text += alphabet[(alphabet.index(char) + alphabet_dict[keyword[keyword_index % len(keyword)]]) % 26]
            keyword_index += 1  # Increment keyword index
        else:
            encrypted_text += char
    return encrypted_text



def decrypt_vigenere(text, keyword):
    alphabet = list(string.ascii_lowercase)
    alphabetnum = list(range(26))
    alphabet_dict = dict(zip(alphabet, alphabetnum))
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            decrypted_text += alphabet[(alphabet.index(char) - alphabet_dict[keyword[alphabet_dict[char]]]) % 26]	
        else:
            decrypted_text += char
    return decrypted_text

#--------------------------Menu--------------------------
while True:
    print('-'*20)
    print("1.Encrypt a text")
    print("2.Decrypt a text")
    print("3.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        text = input("Enter the text to encrypt: ")
        keyword = input("Enter the keyword: ")
        encrypted_text = encrypt_vigenere(text, keyword)
        print("Encrypted text:", encrypted_text)
    elif choice == "2":
        text = input("Enter the text to decrypt: ")
        keyword = input("Enter the keyword: ")
        decrypted_text = decrypt_vigenere(text, keyword)
        print("Decrypted text:", decrypted_text)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")