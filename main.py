from gui import TkView
import console
import threading


def main():
    gui_interface = TkView()
    console_thread = threading.Thread(target=lambda: console.console_using(messages_dict))

    console_thread.start()
    gui_interface.start_interface()

    console_thread.join()
    print("End program")


if __name__ == '__main__':
    messages_dict = {}
    main()
