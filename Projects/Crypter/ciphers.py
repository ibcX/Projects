
# class
# constructor(key)
# cryt(msg) -> str msg criptat
## decrypt(msg) -> str msg decriptat

class Caesar:
    """Generate new alphabet shifted by key"""

    def __init__(self, key):
        self.__key = key
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyz"
        self.message_encrypted = ""
        self.message_decrypted = ""

    def crypt(self, message):
        """Crypt the message and return it"""

        for character in message:
            i = 0
            if character not in self.alphabet:
                self.message_encrypted = self.message_encrypted + character
            else:
                for letter in self.alphabet:
                    if character == letter:
                        if i + self.__key <= 25:
                            self.message_encrypted = self.message_encrypted + self.alphabet[i + self.__key]
                        else:
                            self.message_encrypted = self.message_encrypted + self.alphabet[i + self.__key - 26]
                    i += 1

        print(f"The encrypted message is: {self.message_encrypted}")
        return self.message_encrypted

    def decrypt(self, message):
        """Decrypt the message and return it"""

        for character in message:
            i = 0
            if character not in self.alphabet:
                self.message_decrypted = self.message_decrypted + character
            else:
                for letter in self.alphabet:
                    if character == letter:
                        if i - self.__key >= 0:
                            self.message_decrypted = self.message_decrypted + self.alphabet[i - self.__key]
                        else:
                            self.message_decrypted = self.message_decrypted + self.alphabet[i - self.__key + 26]
                    i += 1

        print(f"The decrypted message is: {self.message_decrypted}")
        return self.message_decrypted



class Shift:
    """Move letters in words by key"""

    def __init__(self, key):
        self.key = key

    def crypt(self, message):
        """Crypt the message and return it"""
        return message

    def decrypt(self, message):
        """Decrypt the message and return it"""
        return message
