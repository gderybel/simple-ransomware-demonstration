class Decryptor:

    def getFilesToDecrypt(self):
        return self.FilesToDecrypt

    def setFilesToDecrypt(self, FilesToDecrypt):
        self.FilesToDecrypt = FilesToDecrypt

    def getEncryptionLevel(self):
        return self.EncryptionLevel

    def setEncryptionLevel(self, EncryptionLevel):
        self.EncryptionLevel = EncryptionLevel

    def getEncryptionKey(self):
        return self.EncryptionKey

    def setEncryptionKey(self, EncryptionKey):
        self.EncryptionKey = EncryptionKey