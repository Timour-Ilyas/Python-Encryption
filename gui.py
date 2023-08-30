import tkinter as tk
import sys

def on_closing():
    sys.exit()

class TkView:
    # setup tkinter
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Encrypter")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # create the gui
    title_label = tk.Label(root, text="Encrypter", font=('Arial', 35))
    title_label.pack()
