import customtkinter as ctk
from customtkinter import CTkLabel, CTkTextbox, CTkButton, CTkEntry, CTkComboBox
import tkinter as tk
from encoder import Encoder
from decoder import Decoder
import pyperclip


class CtkView:
    def __init__(self, messages: dict):
        self.encoder = Encoder()
        self.decoder = Decoder()
        self.messages = messages
        self.state_on_encryption = False

        # setup CTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.resizable(False, False)
        self.root.geometry("1280x720")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        self.file_menu = tk.Menu(self.menubar, tearoff=False,
                                 background='black', foreground='white',
                                 activebackground='white', activeforeground='black')
        self.file_menu.add_command(label='Import CSV file', command=self.import_csv_file)
        self.file_menu.add_command(label='Import JSN file', command=self.import_jsn_file)
        self.file_menu.add_command(label='Import TXT file', command=self.import_txt_file)
        self.file_menu.add_command(label='Import PDF file', command=self.import_pdf_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Save', command=self.save)
        self.file_menu.add_command(label='Save as', command=self.save_as)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        # create the gui
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(padx=40, pady=20, fill="both", expand=True)

        self.title_text = tk.StringVar()
        self.title_label = CTkLabel(self.frame, textvariable=self.title_text, font=('Arial', 60), padx=60, pady=20)
        self.title_label.pack()

        self.text_box_frame = ctk.CTkFrame(self.frame)
        self.text_box_frame.columnconfigure(0, weight=3)
        self.text_box_frame.columnconfigure(1, weight=2)
        self.text_box_frame.columnconfigure(3, weight=3)
        self.text_box_frame.pack(padx=40, pady=20, fill="both")

        self.first_textbox = CTkTextbox(self.text_box_frame, height=100, width=400, padx=5, pady=5)
        self.first_textbox.bind("<KeyPress>", self.__textbox_shortcut)
        self.first_textbox.grid(column=0, row=0, pady=20)

        self.change_mode_button = CTkButton(self.text_box_frame, text="Change mode", command=self.change_mode,
                                            width=110, height=40)
        self.change_mode_button.grid(column=1, row=0, pady=20)

        self.text_of_second_box = tk.StringVar()
        self.text_of_second_box.set("")
        self.second_textbox = CTkTextbox(self.text_box_frame, height=100, width=400, state="disabled", padx=5, pady=5)
        self.second_textbox.grid(column=2, row=0, pady=20)

        self.lateral_buttons_frame = ctk.CTkFrame(self.text_box_frame)
        self.lateral_buttons_frame.grid(column=3, row=0)
        self.copy_second_textbox_button = CTkButton(self.lateral_buttons_frame, text="Copy", height=20, width=30,
                                                    command=self.copy_second_textbox)
        self.copy_second_textbox_button.grid(column=0, row=0, padx=5, pady=5)
        self.clean_second_textbox_button = CTkButton(self.lateral_buttons_frame, text="Clean", height=20, width=30,
                                                     command=self.clean_second_textbox)
        self.clean_second_textbox_button.grid(column=0, row=1, padx=5, pady=5)

        self.combobox_mode = CTkComboBox(self.frame, state="readonly", font=("Arial", 20), width=170, height=40)
        self.combobox_mode.configure(values=self.encoder.get_encryption_options())
        self.combobox_mode.set(self.encoder.get_encryption_options(0))
        self.combobox_mode.pack(pady=20)

        self.key_frame = ctk.CTkFrame(self.frame)
        self.key_frame.pack(padx=40, pady=20, ipady=10)
        self.key_label = CTkLabel(self.key_frame, text="Key", font=('Arial', 20), padx=10, pady=10)
        self.key_label.pack()
        self.key_entry = CTkEntry(self.key_frame, font=('Arial', 20), width=170, height=40)
        self.key_entry.pack(padx=20)

        self.btn_text = tk.StringVar()
        self.translation_button = CTkButton(self.frame, textvariable=self.btn_text, command=self.clicked_main_button,
                                            width=200, height=50, font=('Arial', 25))
        self.translation_button.pack(padx=20, pady=20)

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
        key = self.key_entry.get()

        if self.state_on_encryption:
            final_message = self.encoder.cipher(self.combobox_mode.get(), first_message, key)
        else:
            final_message = self.decoder.decipher(self.combobox_mode.get(), first_message, key)

        self.second_textbox.configure(state="normal")
        self.second_textbox.delete(1.0, "end")
        self.second_textbox.insert("end", final_message)
        self.second_textbox.configure(state="disabled")

        self.messages[first_message] = final_message

    def __textbox_shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.clicked_main_button()

    def copy_second_textbox(self):
        pyperclip.copy(self.second_textbox.get("1.0", "end-1c"))

    def clean_second_textbox(self):
        self.second_textbox.configure(state="normal")
        self.second_textbox.delete(1.0, "end")
        self.second_textbox.configure(state="disabled")

    def import_csv_file(self):
        pass

    def import_jsn_file(self):
        pass

    def import_txt_file(self):
        pass

    def import_pdf_file(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass
