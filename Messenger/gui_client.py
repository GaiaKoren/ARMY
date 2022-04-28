from threading import Thread
from tkinter import *
from gui import LoginWin
import Network

client = Network.initial_connect()

def init_root():
    root = Tk()
    root.geometry("800x800")
    root.configure(bg="black")
    return root


def gui_thread():
    myLoginWin = LoginWin(client)

def start(client):
    thread_send = Thread(target=gui_thread, args=())
    thread_send.start()
    thread_send.join()
    print("hey")

    # thread_receive = Thread(target=Network.receive_message_thread, args=(client,))
    # thread_receive.start()


start(client)