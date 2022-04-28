import socket
from threading import Thread
import pickle
import Message
import Network

client = Network.initial_connect()




def send_message_thread():
    username = None
    password = None
    while True:
        message = input("")
        if "/" not in message:
            Network.send(client, Message.Message("pm", username, message))
            continue
        parsed_msg = message.split("/")
        cmd = parsed_msg[1]
        if cmd == "login":
            username = parsed_msg[2]
            password = parsed_msg[3]
            Network.send(client, Message.Message("login", None, [username, password]))
        elif cmd == "logout":
            Network.send(client, Message.Message("logout", username, None))
        elif cmd == "register":
            Network.send(client, Message.Message("register", None, [parsed_msg[2], parsed_msg[3]]))
        elif cmd == "unregister":
            Network.send(client, Message.Message("unregister", username, None))
        elif cmd == "enter":
            Network.send(client, Message.Message("enter", username, parsed_msg[2]))
        elif cmd == "exit":
            Network.send(client, Message.Message("exit", username, None))
        elif cmd == "disconnect":
            Network.send(client, Message.Message("disconnect", username, None))
            break
        elif cmd == "create":
            group = parsed_msg[2]
            Network.send(client, Message.Message("create", username, group))
        elif cmd == "group":
            name = parsed_msg[2]
            Network.send(client, Message.Message("group", username, name))
        elif cmd == "members":
            Network.send(client, Message.Message("members", username, None))
        elif cmd == "admins":
            Network.send(client, Message.Message("admins", username, None))
        elif cmd == "add_admin":
            name = parsed_msg[2]
            Network.send(client, Message.Message("add_admin", username, name))
        elif cmd == "quit":
            Network.send(client, Message.Message("quit", username, None))
        elif cmd == "add":
            name = parsed_msg[2]
            Network.send(client, Message.Message("add", username, name))
        elif cmd == "remove":
            name = parsed_msg[2]
            Network.send(client, Message.Message("remove", username, name))

def start(client):
    thread_send = Thread(target=send_message_thread, args=())
    thread_send.start()
    thread_receive = Thread(target=Network.receive_message_thread, args=(client,))
    thread_receive.start()


start(client)
