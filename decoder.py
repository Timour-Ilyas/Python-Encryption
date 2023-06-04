import threading

class Decoder:

    def caesar(self, secret_message, key):
        message = ""
        for character in secret_message:
            if 'A' <= character <= 'Z':
                delta = ord(character) - ord('A') - int(key)
                delta = delta % 26
                message = message + chr(delta + ord('A'))
            elif 'a' <= character <= 'z':
                delta = ord(character) - ord('a') - int(key)
                delta = delta % 26
                message = message + chr(delta + ord('a'))
            elif character > chr(0):
                message += character

        return message

    def vigenere(self, secret_message, key):
        message = ""
        key = list(key)
        for i, character in enumerate(secret_message):
            if 'A' <= character <= 'Z':
                delta = ord(character) - ord('A') - (ord(key[i % len(key)]) - ord('A') + 1)
                delta = delta % 26
                message = message + chr(delta + ord('A'))
            elif 'a' <= character <= 'z':
                delta = ord(character) - ord('a') - (ord(key[i % len(key)]) - ord('a') + 1)
                delta = delta % 26
                message += chr(delta + ord('a'))
            elif character > chr(0):
                message += character

        return message
