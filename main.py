from gui import CtkView
import console
import threading


def main():
    gui_interface = CtkView(messages)
    console_thread = threading.Thread(target=lambda: console.console_using(messages))

    console_thread.start()
    gui_interface.start_interface()

    console_thread.join()
    print("End program")


if __name__ == '__main__':
    messages = {}
    main()
