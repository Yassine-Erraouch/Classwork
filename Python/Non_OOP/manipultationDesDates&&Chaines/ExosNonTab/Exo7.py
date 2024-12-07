from cryptography.fernet import Fernet

def get_key():
    key = Fernet.generate_key()
    return key


key = Fernet(get_key())
def encrypt_message(message, key):
    cipher_text = key.encrypt(message)
    return cipher_text


def decrypt_message(cipher_text, key):
    message = f.decrypt(cipher_text)
    return message


#--------------------------Menu--------------------------
while True:
    print('-'*20)
    print("1.Encrypt a text")
    print("2.Decrypt a text")
    print("3.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        message = input("Enter the message to encrypt: ")
        key = Fernet(get_key())
        encrypted_message = encrypt_message(message, key)
        print("Encrypted message:", encrypted_message.decode('utf-8'))
    elif choice == "2":
        cipher_text = input("Enter the cipher text to decrypt: ")
        key = Fernet(get_key())
        decrypted_message = decrypt_message(cipher_text, key)
        print("Decrypted message:", decrypted_message.decode('utf-8'))
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

