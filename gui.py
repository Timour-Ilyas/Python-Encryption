import tkinter as tk

class TkView:
    def __init__(self):
        # setup tkinter
        self.root = tk.Tk()
        self.root.title("Encrypter")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # create the gui
        self.root.geometry("1280x720")
        title_label = tk.Label(self.root, text="Encrypter", font=('Arial', 35))
        title_label.pack()

    def start_interface(self):
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()
        print("End interface")