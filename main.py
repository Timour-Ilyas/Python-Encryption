from encoder import Encoder
from decoder import Decoder
from gui import TkView

def main():
    option = 0
    messages_dict = {}
    secret_message = ""
    original_message = ""

    gui_interface = TkView()
    gui_interface.root.mainloop()

    while option > 3 or option < 1:
        option = int(input("Choose the cipher:\n1. Caesar\n2. Vigenère\n3. Symmetric\n"))
        if option > 3 or option < 1:
            print("Incorrect value")

    message = input("Write the message: ")
    key = input("Enter the key: ")
    encoder = Encoder()
    decoder = Decoder()

    if option == 1:
        secret_message = encoder.caesar(message, key)
        print(f"{secret_message}")
        original_message = decoder.caesar(secret_message, key)
        print(original_message)

    elif option == 2:
        secret_message = encoder.vigenere(message, key)
        print(f"{secret_message}")
        original_message = decoder.vigenere(secret_message, key)
        print(original_message)

    elif option == 3:
        print("Symmetric cipher")

    messages_dict[secret_message] = original_message

if __name__ == '__main__':
    main()
