from encoder import Encoder
from decoder import Decoder


def console_using(messages: dict):
    option = 0
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

    secret_message = encoder.cipher(encoder.get_encryption_options(option-1), message, key)
    original_message = decoder.decipher(decoder.get_decryption_options(option-1), secret_message, key)

    print(f"{secret_message}")
    print(f"{original_message}")

    messages[secret_message] = original_message
