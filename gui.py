import tkinter as tk
from tkinter import ttk
from encoder import Encoder
from decoder import Decoder


class TkView:
    def __init__(self):
        # setup tkinter
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # create the gui
        self.root.geometry("1280x720")
        self.title_text = tk.StringVar()
        self.title_label = tk.Label(self.root, textvariable=self.title_text, font=('Arial', 35))
        self.title_label.pack()

        self.first_textbox = tk.Entry(self.root)
        self.first_textbox.pack()

        self.change_mode_button = tk.Button(self.root, text="Change mode", command=self.change_mode)
        self.change_mode_button.pack()

        self.text_of_second_box = tk.StringVar()
        self.text_of_second_box.set("")
        self.second_textbox = tk.Entry(self.root, textvariable=self.text_of_second_box, state="disabled")
        self.second_textbox.pack()

        self.combobox_mode = ttk.Combobox(self.root, state="readonly")
        self.combobox_mode["values"] = ("Caesar", "Vigenère", "Symmetric")
        self.combobox_mode.current(0)
        self.combobox_mode.pack()

        self.title_label = tk.Label(self.root, text="Key", font=('Arial', 10))
        self.title_label.pack()
        self.key_textbox = tk.Entry(self.root)
        self.key_textbox.pack()

        self.btn_text = tk.StringVar()
        self.translation_button = tk.Button(self.root, textvariable=self.btn_text, command=self.clicked_main_button)
        self.translation_button.pack()

        self.encoder = Encoder()
        self.decoder = Decoder()
        self.state_on_encryption = False
        self.change_mode()

    def start_interface(self):
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()
        print("End interface")

    def change_mode(self):
        if self.state_on_encryption:
            self.root.title("Decrypter")
            self.title_text.set("Decrypter")
            self.btn_text.set("Decrypt")
            self.translation_button.config(fg="red", bg="black")
            self.state_on_encryption = not self.state_on_encryption
        else:
            self.root.title("Encrypter")
            self.title_text.set("Encrypter")
            self.btn_text.set("Encrypt")
            self.translation_button.config(fg="green", bg="black")
            self.state_on_encryption = not self.state_on_encryption

    def clicked_main_button(self):
        if self.state_on_encryption:
            message = self.first_textbox.get()
            key = self.key_textbox.get()
            if not self.combobox_mode.current():
                secret_message = self.encoder.caesar(message, key)
                self.text_of_second_box.set(secret_message)
            if self.combobox_mode.current() == 1:
                secret_message = self.encoder.vigenere(message, key)
                self.text_of_second_box.set(secret_message)
            if self.combobox_mode.current() == 2:
                pass
        else:
            secret_message = self.first_textbox.get()
            key = self.key_textbox.get()
            if not self.combobox_mode.current():
                message = self.decoder.caesar(secret_message, key)
                self.text_of_second_box.set(message)
            if self.combobox_mode.current() == 1:
                message = self.decoder.vigenere(secret_message, key)
                self.text_of_second_box.set(message)
            if self.combobox_mode.current() == 2:
                pass
