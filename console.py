from encoder import Encoder
from decoder import Decoder


def console_using(messages_dict):
    option = 0
    secret_message = ""
    original_message = ""

    while option > 4 or option < 1:
        option = int(input("Choose the cipher:\n1. Caesar\n2. Vigenère\n3. Symmetric\n4. End program\n"))
        if option > 4 or option < 1:
            print("Incorrect value")

    if option == 4:
        print("End console")
        return

    message = input("Write the message: ")
    key = input("Enter the key: ")
    encoder = Encoder()
    decoder = Decoder()

    if option == 1:
        secret_message = encoder.caesar(message, key)
        original_message = decoder.caesar(secret_message, key)
    elif option == 2:
        secret_message = encoder.vigenere(message, key)
        original_message = decoder.vigenere(secret_message, key)
    elif option == 3:
        print("Symmetric cipher")

    print(f"{secret_message}")
    print(original_message)

    messages_dict[secret_message] = original_message
