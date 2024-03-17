"""
This file contains the Decryptor class, and every functions linked to the decryption process
"""
import FileFunctions as Folder

class Decryptor:
    """
    This class will be used to decrypt data.
    - decryption_key: str
    - encrypted_extensions: list
    - encryption_level: int
    - folder: str
    - recursive: bool (True)
    - files_to_decrypt: list
    """

    def __init__(
            self,
            decryption_key: str,
            encrypted_extensions: list,
            encryption_level: int,
            folder: str,
            recursive: bool = True
        ) -> None:
        self.decryption_key = decryption_key
        self.encryption_level = encryption_level
        self.encrypted_extensions = encrypted_extensions
        self.folder = folder
        self.recursive = recursive

        # check if folder exists before setting it
        if Folder.folder_exists(folder):
            self.folder = folder
        else:
            exit("The selected folder was not found, check path and permissions.")

        self.files_to_decrypt = Folder.grab_files(self.folder, self.encrypted_extensions)

    def decrypt_files(self):
        """
        This function decrypts encrypted files using the encryption key
        """
        index = 0
        max_index = self.encryption_level - 1
        for file in self.files_to_decrypt:
            try:
                with open(file, 'rb') as reading_file: # Read file as binary
                    data = reading_file.read()
                    with open(file, 'wb') as reading_file: # Write file as binary
                        for byte in data:
                            xor_byte = byte ^ ord(self.decryption_key[index]) # Decrypt any byte
                            reading_file.write(xor_byte.to_bytes(1, 'little')) # Write file
                            if index >= max_index:
                                index = 0
                            else:
                                index += 1
            except:
                print('Couldn\'t decrypt file \'' + file + '\'.')

        print('Files were decrypted successfully.\n')
