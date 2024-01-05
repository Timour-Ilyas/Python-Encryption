import tkinter as tk
from tkinter import ttk
from encoder import Encoder
from decoder import Decoder


class TkView:
    option = 0
    secret_message = ""
    original_message = ""
    encoder = Encoder()
    decoder = Decoder()

    def __init__(self):
        # setup tkinter
        self.root = tk.Tk()
        self.root.title("Encrypter")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # create the gui
        self.root.geometry("1280x720")
        self.title_text = tk.StringVar()
        self.title_text.set("Encrypter")
        self.title_label = tk.Label(self.root, textvariable=self.title_text, font=('Arial', 35))
        self.title_label.pack()

        self.first_textbox = tk.Entry(self.root)
        self.first_textbox.pack()

        self.change_mode = tk.Button(self.root, text="Change mode", command=self.change_mode)
        self.change_mode.pack()

        self.second_textbox = tk.Entry(self.root, state="disabled")
        self.second_textbox.pack()

        self.combobox_mode = ttk.Combobox(self.root, state="readonly")
        self.combobox_mode["values"] = ("Caesar", "Vigenère", "Symmetric")
        self.combobox_mode.current(0)
        self.combobox_mode.pack()

        self.btn_text = tk.StringVar()
        self.btn_text.set("Encrypt")
        self.translation_button = tk.Button(self.root, textvariable=self.btn_text, fg="green", bg="black",
                                            command=self.clicked_main_button)
        self.translation_button.pack()

    def start_interface(self):
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()
        print("End interface")

    def change_mode(self):
        if self.btn_text.get() == "Encrypt":
            self.root.title("Decrypter")
            self.title_text.set("Decrypter")
            self.btn_text.set("Decrypt")
            self.translation_button.config(fg="red", bg="black")
        else:
            self.root.title("Encrypter")
            self.title_text.set("Encrypter")
            self.btn_text.set("Encrypt")
            self.translation_button.config(fg="green", bg="black")

    def clicked_main_button(self):
        if self.btn_text.get() == "Encrypt":
            message = self.first_textbox.get()
            if True:
                pass
        else:
            pass
