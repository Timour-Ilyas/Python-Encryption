import customtkinter as ctk
from customtkinter import CTkLabel, CTkTextbox, CTkButton, CTkEntry, CTkComboBox
import tkinter as tk
from encoder import Encoder
from decoder import Decoder


class CtkView:
    def __init__(self, messages_dict):
        self.encoder = Encoder()
        self.decoder = Decoder()
        self.messages_dict = messages_dict
        self.state_on_encryption = False

        # setup CTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.resizable(False, False)
        self.root.geometry("1280x720")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(
            label='Add CSV file',
            command=self.add_csv_file
        )
        file_menu.add_command(
            label='Add JSN file',
            command=self.add_jsn_file
        )
        menubar.add_cascade(
            label="File",
            menu=file_menu
        )

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(padx=40, pady=20, fill="both", expand=True)

        # create the gui
        self.title_text = tk.StringVar()
        self.title_label = CTkLabel(self.frame, textvariable=self.title_text, font=('Arial', 35), padx=60, pady=20)
        self.title_label.pack()

        self.first_textbox = CTkTextbox(self.frame, height=100, width=400, padx=5, pady=5)
        self.first_textbox.bind("<KeyPress>", self.textbox_shortcut)
        self.first_textbox.pack(pady=20)

        self.change_mode_button = CTkButton(self.frame, text="Change mode", command=self.change_mode)
        self.change_mode_button.pack(pady=20)

        self.text_of_second_box = tk.StringVar()
        self.text_of_second_box.set("")
        self.second_textbox = CTkTextbox(self.frame, height=100, width=400, state="disabled", padx=5, pady=5)
        self.second_textbox.pack(pady=20)

        self.combobox_mode = CTkComboBox(self.frame, state="readonly")
        self.combobox_mode.configure(values=self.encoder.get_encryption_options())
        self.combobox_mode.set(self.encoder.get_encryption_options(0))
        self.combobox_mode.pack(pady=20)

        self.title_label = CTkLabel(self.frame, text="Key", font=('Arial', 15))
        self.title_label.pack()
        self.key_entry = CTkEntry(self.frame)
        self.key_entry.pack(pady=20)

        self.btn_text = tk.StringVar()
        self.translation_button = CTkButton(self.frame, textvariable=self.btn_text, command=self.clicked_main_button)
        self.translation_button.pack()

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
            self.translation_button.configure(fg_color="red", border_color="black")
            self.state_on_encryption = not self.state_on_encryption
        else:
            self.root.title("Encrypter")
            self.title_text.set("Encrypter")
            self.btn_text.set("Encrypt")
            self.translation_button.configure(fg_color="green", border_color="black")
            self.state_on_encryption = not self.state_on_encryption

    def clicked_main_button(self):
        first_message = self.first_textbox.get("1.0", "end-1c")
        final_message = ""
        key = self.key_entry.get()

        if self.state_on_encryption:
            if self.combobox_mode.get() == self.encoder.get_encryption_options(0):
                final_message = self.encoder.caesar(first_message, key)
            elif self.combobox_mode.get() == self.encoder.get_encryption_options(1):
                final_message = self.encoder.vigenere(first_message, key)
            else:
                pass
        else:
            if self.combobox_mode.get() == self.decoder.get_decryption_options(0):
                final_message = self.decoder.caesar(first_message, key)
            elif self.combobox_mode.get() == self.decoder.get_decryption_options(1):
                final_message = self.decoder.vigenere(first_message, key)
            else:
                pass
        self.second_textbox.configure(state="normal")
        self.second_textbox.delete(1.0, "end")
        self.second_textbox.insert("end", final_message)
        self.second_textbox.configure(state="disabled")

        self.messages_dict[first_message] = final_message

    def textbox_shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.clicked_main_button()

    def add_csv_file(self):
        pass

    def add_jsn_file(self):
        pass
