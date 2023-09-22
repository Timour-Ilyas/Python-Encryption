import threading
import queue


class Decoder:
    def caesar(self, secret_message, key):
        que = queue.Queue()
        if len(secret_message) < 10:  # 1 thread
            return self.__caesar_decrypter(secret_message, key, que)

        splitted_secret_message = []
        threads_list = []
        message = ""
        if len(secret_message) < 25:  # 2 threads
            number_of_divisions = 2

        else:  # 3 threads
            number_of_divisions = 3

        division_sentinel = -(len(secret_message) // -number_of_divisions)
        for index in range(number_of_divisions):
            splitted_secret_message.append(secret_message[0:division_sentinel])
            secret_message = secret_message[division_sentinel:]
            threads_list.append(
                threading.Thread(target=self.__caesar_decrypter, args=(splitted_secret_message[index], key, que)))
            threads_list[index].start()

        for index in range(len(splitted_secret_message)):
            threads_list[index].join()
            message += que.get()

        return message

    @staticmethod
    def __caesar_decrypter(secret_message, key, que):
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

        que.put(message)
        return message

    def vigenere(self, secret_message, key):
        que = queue.Queue()
        if len(secret_message) < 10:  # 1 thread
            return self.__vigenere_decrypter(secret_message, key, que)

        splitted_message = []
        threads_list = []
        message = ""
        if len(secret_message) < 25:  # 2 threads
            number_of_divisions = 2

        else:  # 3 threads
            number_of_divisions = 3

        division_sentinel = -(len(secret_message) // -number_of_divisions)
        for index in range(number_of_divisions):
            splitted_message.append(secret_message[0:division_sentinel])
            secret_message = secret_message[division_sentinel:]
            threads_list.append(
                threading.Thread(target=self.__vigenere_decrypter, args=(splitted_message[index], key, que)))
            key = key[division_sentinel % len(key):] + key[0:division_sentinel % len(key)]
            threads_list[index].start()

        for index in range(len(splitted_message)):
            threads_list[index].join()
            message += que.get()

        return message

    @staticmethod
    def __vigenere_decrypter(secret_message, key, que):
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

        que.put(message)
        return message
