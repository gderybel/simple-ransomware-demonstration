import os
from Encryptor import Encryptor
from Decryptor import Decryptor

choice = input("Would you like to encrypt or decrypt your files ? (e/d) : ")

if choice == "e":
    # Encrypt
    folder = input("Path to encrypt (only files within this folder will be encrypted) : ")
    extensions = []
    while True:
        extension = input("Which extensions would you like to encrypt (enter them one by one) : ")
        if extension == "":
            break
        else:
            if not extension.startswith('.'):
                extension = "." + extension
            extensions.append(extension)
    encryptor = Encryptor(
        encrypted_extensions=extensions,
        encryption_level=16,
        computer_name=os.getenv('COMPUTERNAME'),
        folder=folder
    )
    encryptor.encrypt_files()
    # Send the key to a web server for example, to decrypt file later
    print(encryptor.encryption_key)
elif choice == "d":
    # Decrypt
    encryption_key = input("The encryption key used in encryption process : ")
    folder = input("Path to encrypt (only files within this folder will be encrypted) : ")
    extensions = []
    while True:
        extension = input("Which extensions would you like to encrypt (enter them one by one) : ")
        if extension == "":
            break
        else:
            if not extension.startswith('.'):
                extension = "." + extension
            extensions.append(extension)
    decryptor = Decryptor(
        decryption_key=encryption_key,
        encrypted_extensions=extensions,
        encryption_level=16,
        folder=folder,
    )
    decryptor.decrypt_files()
else:
    exit("This isn't an known option.")
