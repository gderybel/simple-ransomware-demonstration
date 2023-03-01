class DecryptorRepository():
    
    def getDecryptor(self):
        return self.Decryptor
    
    def setDecryptor(self, Decryptor):
        self.Decryptor = Decryptor

    def DecryptFiles(self):
        index = 0
        max_index = self.getDecryptor().getEncryptionLevel() - 1
        for file in self.getDecryptor().getFilesToDecrypt():
            try:
                with open(file, 'rb') as reading_file: # Read file as binary
                    data = reading_file.read()
                    with open(file, 'wb') as reading_file: # Read file as binary
                        for byte in data:
                            xor_byte = byte ^ ord(self.getDecryptor().getEncryptionKey()[index]) # Decrypt any byte
                            reading_file.write(xor_byte.to_bytes(1, 'little')) # Write file
                            if index >= 16:
                                index = 0
                            else:
                                index += 1
            except:
                print('Couldn\'t decrypt file \'' + file + '\'.')

        print('Files were decrypted successfully.\n')