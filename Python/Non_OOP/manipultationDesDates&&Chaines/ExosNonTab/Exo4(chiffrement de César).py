import string

# #Q1
# def encrypt_ceasar(text, shift):
#     alphabet = string.ascii_lowercase
#     encrypted_text = ""
#     for char in text:
#         if char in alphabet:
#             encrypted_text += alphabet[(alphabet.index(char) + shift) % 26]
#         else:
#             encrypted_text += char
#     return encrypted_text


# #Q2
# def decrypt_ceasar(text, shift):
#     alphabet = string.ascii_lowercase
#     decrypted_text = ""
#     for char in text:
#         if char in alphabet:
#             decrypted_text += alphabet[(alphabet.index(char) - shift) % 26]
#         else:
#             decrypted_text += char
#     return decrypted_text


import string

#Q1
def encrypt_ceasar(text, shift):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    encrypted_text = ""
    for char in text:
        if char in alphabet_lower:
            encrypted_text += alphabet_lower[(alphabet_lower.index(char) + shift) % 26]
        elif char in alphabet_upper:
            encrypted_text += alphabet_upper[(alphabet_upper.index(char) + shift) % 26]
        else:
            encrypted_text += char
    return encrypted_text


#Q2
def decrypt_ceasar(text, shift):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    decrypted_text = ""
    for char in text:
        if char in alphabet_lower:
            decrypted_text += alphabet_lower[(alphabet_lower.index(char) - shift) % 26]
        elif char in alphabet_upper:
            decrypted_text += alphabet_upper[(alphabet_upper.index(char) - shift) % 26]
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
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            exit()
        encrypted_text = encrypt_ceasar(text, shift)
        print("Encrypted text:", encrypted_text)
    elif choice == "2":
        text = input("Enter the text to decrypt: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        decrypted_text = decrypt_ceasar(text,shift)
        print("Decrypted text:", decrypted_text)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    
