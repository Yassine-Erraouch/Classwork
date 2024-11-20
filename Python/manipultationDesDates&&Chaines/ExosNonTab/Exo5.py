import random
#creating the genreate key function
def generate_key():
    key = ""
    for i in range(8):
        key += chr(random.randint(97, 122))
    return key

#creating the encrypt function
def encrypt_substitution(text,key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            i = 0
            encrypted_char = chr((ord(char) - ord('a') + ord(key[i % len(key)])) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
        i += 1
    return encrypted_text

#creating the decrypt function
def decrypt_substitution(text,key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            i = 0
            decrypted_char = chr((ord(char) - ord('a') - ord(key[i % len(key)]) + 26) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
        i += 1
    return decrypted_text

#--------------------------Menu--------------------------
while True:
    print('-'*20)
    print("1.Encrypt a text")
    print("2.Decrypt a text")
    print("3.Generate a key")
    print("4.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        text = input("Enter the text to encrypt: ")
        key = input("Enter the key: ")
        encrypted_text = encrypt_substitution(text,key)
        print("Encrypted text:", encrypted_text)
    elif choice == "2":
        text = input("Enter the text to decrypt: ")
        key = input("Enter the key: ")
        decrypted_text = decrypt_substitution(text,key)
        print("Decrypted text:", decrypted_text)
    elif choice == "3":
        key = generate_key()
        print("Generated key:", key)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
