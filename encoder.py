class Encoder:

    def caesar(self, message, key):
        secret_message = ""
        for character in message:
            if 'A' <= character <= 'Z':
                delta = ord(character) - ord('A') + int(key)
                delta = delta % 26
                secret_message = secret_message + chr(delta + ord('A'))
            elif 'a' <= character <= 'z':
                delta = ord(character) - ord('a') + int(key)
                delta = delta % 26
                secret_message = secret_message + chr(delta + ord('a'))
            elif character > chr(0):
                secret_message += character

        return secret_message

    def vigenere(self, message, key):
        secret_message = ""
        key = list(key)
        for i, character in enumerate(message):
            if 'A' <= character <= 'Z':
                delta = ord(character) - ord('A') + (ord(key[i % len(key)]) - ord('A') + 1)
                delta = delta % 26
                secret_message = secret_message + chr(delta + ord('A'))
            elif 'a' <= character <= 'z':
                delta = ord(character) - ord('a') + (ord(key[i % len(key)]) - ord('a') + 1)
                delta = delta % 26
                secret_message += chr(delta + ord('a'))
            elif character > chr(0):
                secret_message += character

        return secret_message
