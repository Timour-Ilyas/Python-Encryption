import threading
import queue


class Encoder:
    def __init__(self):
        self.__encryption_options = ["caesar", "vigenere", "symmetric"]

    def caesar(self, message, key):
        que = queue.Queue()
        if len(message) < 10:  # 1 thread
            return self.__caesar_crypter(message, key, que)

        splitted_message = []
        threads_list = []
        secret_message = ""
        if len(message) < 25:  # 2 threads
            number_of_divisions = 2

        else:  # 3 threads
            number_of_divisions = 3

        division_sentinel = -(len(message) // -number_of_divisions)
        for index in range(number_of_divisions):
            splitted_message.append(message[0:division_sentinel])
            message = message[division_sentinel:]
            threads_list.append(
                threading.Thread(target=self.__caesar_crypter, args=(splitted_message[index], key, que)))
            threads_list[index].start()

        for index in range(len(splitted_message)):
            threads_list[index].join()
            secret_message += que.get()

        return secret_message

    @staticmethod
    def __caesar_crypter(message, key, que):
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

        que.put(secret_message)
        return secret_message

    def vigenere(self, message, key):
        que = queue.Queue()
        if len(message) < 10:  # 1 thread
            return self.__vigenere_crypter(message, key, que)

        splitted_message = []
        threads_list = []
        secret_message = ""
        if len(message) < 25:  # 2 threads
            number_of_divisions = 2

        else:  # 3 threads
            number_of_divisions = 3

        division_sentinel = -(len(message) // -number_of_divisions)
        for index in range(number_of_divisions):
            splitted_message.append(message[0:division_sentinel])
            message = message[division_sentinel:]
            threads_list.append(
                threading.Thread(target=self.__vigenere_crypter, args=(splitted_message[index], key, que)))
            key = key[division_sentinel % len(key):] + key[0:division_sentinel % len(key)]
            threads_list[index].start()

        for index in range(len(splitted_message)):
            threads_list[index].join()
            secret_message += que.get()

        return secret_message

    @staticmethod
    def __vigenere_crypter(message, key, que):
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

        que.put(secret_message)
        return secret_message

    def get_encryption_options(self, option=None):
        if option is not None:
            return self.__encryption_options[option]
        return self.__encryption_options
