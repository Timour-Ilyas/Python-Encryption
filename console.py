from encoder import Encoder
from decoder import Decoder


def console_using(messages_dict):
    option = 0
    secret_message = ""
    original_message = ""
    encoder = Encoder()
    decoder = Decoder()

    console_text_options = "Choose the cipher:\n"
    console_text_options += "".join(str(index) + ". " + value + "\n"
                                    for index, value in enumerate(encoder.get_encryption_options(), start=1))
    console_text_options += str(len(encoder.get_encryption_options()) + 1) + ". Exit console\n"

    while option > len(encoder.get_encryption_options()) + 1 or option < 1:
        option = int(input(console_text_options))
        if option > len(encoder.get_encryption_options()) + 1 or option < 1:
            print("Incorrect value")

    if option == len(encoder.get_encryption_options()) + 1:
        print("End console")
        return

    message = input("Write the message: ")
    key = input("Enter the key: ")

    if option == 1:
        secret_message = encoder.caesar(message, key)
        original_message = decoder.caesar(secret_message, key)
    elif option == 2:
        secret_message = encoder.vigenere(message, key)
        original_message = decoder.vigenere(secret_message, key)
    elif option == 3:
        print("Symmetric cipher")

    print(f"{secret_message}")
    print(f"{original_message}")

    messages_dict[secret_message] = original_message
