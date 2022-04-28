import socket

import pickle

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050


def initial_connect():
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(conn, message):
    message = pickle.dumps(message)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)


def receive_message(client):
    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length)
            msg = pickle.loads(msg)
            return msg


def receive_message_thread(client):
    while True:
        msg = receive_message(client)
        if msg.get_cmd() == "sm":
            print(msg.get_content())
        elif msg.get_cmd() == "pm":
            print(msg.get_source() + ": " + msg.get_content())
        elif msg.get_cmd() == "db":
            print(msg.get_content())