class Encryptor():

    def getEncryptedExtensions(self):
        return self.EncryptedExtensions

    def setEncryptedExtensions(self, EncryptedExtensions):
        self.EncryptedExtensions = EncryptedExtensions
        # It has to be a tuple

    def getFilesToEncrypt(self):
        return self.FilesToEncrypt

    def setFilesToEncrypt(self, FilesToEncrypt):
        self.FilesToEncrypt = FilesToEncrypt
        # It has to be a list

    def getEncryptionKey(self):
        return self.EncryptionKey

    def setEncryptionKey(self, EncryptionKey):
        self.EncryptionKey = EncryptionKey

    def getComputerName(self):
        return self.ComputerName

    def setComputerName(self, ComputerName):
        self.ComputerName = ComputerName

    def getEncryptionLevel(self):
        return self.EncryptionLevel

    def setEncryptionLevel(self, EncryptionLevel):
        self.EncryptionLevel = EncryptionLevel
        # It has to be an integer