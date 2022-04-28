import socket
from threading import Thread, Event
from queue import Queue
import pickle
from Message import Message
from Conversation import Conversation, ConversationManager
from User import UserManager, User
from Network import send
from Group import GroupManager, Group

myUserManager = UserManager()
myConversationManager = ConversationManager()
myGroupManager = GroupManager()


PORT = 5050
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)




def handle_client(conn, addr, my_queue):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            msg = pickle.loads(msg)
            cmd = msg.get_cmd()
            source = msg.get_source()
            content = msg.get_content()
            if cmd == "disconnect":
                myUserManager.user_logout(source)
                send(conn, Message("sm", None, "You have successfully disconnected"))
                print(f"[LOGIN] {source} has disconnected.")
                connected = False
            elif cmd == "register":
                username, password = content[0], content[1]
                if myUserManager.add_user(username, password):
                    send(conn, Message("sm", None, "You have successfully registered."))
                    print(f"[REGISTER] {username} has registered with password: {password}.")
                else:
                    print(f"[REGISTER] {username} has failed to register.")
                    send(conn, Message("sm", None, "This username is already in use..."))
            elif cmd == "login":
                username, password = content[0], content[1]
                if myUserManager.is_password(username, password):
                    myUserManager.user_login(username, password, my_queue)
                    send(conn, Message("sm", None, "You have successfully logged in."))
                    print(f"[LOGIN] {username} has logged in with password {password}.")
                else:
                    send(conn, Message("sm", None, "User credentials are incorrect."))
                    print(f"[LOGIN] {username} has failed to log in with password {password}.")
            elif source is None or not myUserManager.is_logged_in(source):
                send(conn, Message("sm", None, "You must be logged in to perform this action."))
                print(f"[PM] user not logged in.")
            else:
                if cmd == "unregister":
                    if myUserManager.remove_user(source):
                        send(conn, Message("sm", None, "You have successfully unregistered."))
                        print(f"[UNREGISTER] {source} has unregistered.")
                    else:
                        send(conn, Message("sm", None, "You must be registered and logged in to unregister."))
                        print(f"[UNREGISTER] failed unregistration attempt.")
                elif cmd == "logout":
                    if myUserManager.user_logout(source):
                        send(conn, Message("sm", None, "You have successfully logged out."))
                        print(f"[LOGOUT] {source} has logged out.")
                    else:
                        send(conn, Message("sm", None, "You must be logged in to log out"))
                        print(f"[LOGOUT] {source} has failed to log out.")
                elif cmd == "enter":
                    if myUserManager.user_exists(content):
                        myConversationManager.add_conversation(source, content)
                        myUserManager.set_user_conv(source, content)
                        send(conn, Message("sm", None, "You have entered a conversation with: " + content))
                        myConversationManager.send_conv_db(source, content, myUserManager.get_user_by_name(source))
                    else:
                        send(conn, Message("sm", None, "This user does not exist."))
                elif cmd == "exit":
                    if myUserManager.get_user_conv(source) is not None:
                        myUserManager.set_user_conv(source, None)
                        send(conn, Message("sm", None, "You have exited this conversation."))

                    else:
                        send(conn, Message("sm", None, "You must be in a conversation to exit one."))
                elif cmd == "group":
                    if myGroupManager.is_exists(content) and myGroupManager.is_group_member(content, source):
                        myUserManager.set_user_conv(source, content)
                        send(conn, Message("sm", None, "You have entered the group: " + content))
                        myGroupManager.send_group_db(content, source, myUserManager)
                    else:
                        send(conn, Message("sm", None, "You are not a member of this group."))
                elif cmd == "add" or cmd == "remove" or cmd == "members" or cmd == "admins" or cmd == "add_admin" or cmd == "quit":
                    group_name = myUserManager.get_user_conv(source)
                    if group_name is None or not myGroupManager.is_exists(group_name):
                        send(conn, Message("sm", None, "You must be in a group to perform this action."))
                        print(f"[PM] {source} has failed to preform action.")
                    elif cmd == "members":
                        members = myGroupManager.get_group_members(group_name)
                        send(conn, Message("sm", None, "This group's members: " + str(members)))
                        print(f"[PM] group members have been sent to: {source}.")
                    elif cmd == "admins":
                        admins = myGroupManager.get_group_admins(group_name)
                        print("admins", admins)
                        send(conn, Message("sm", None, "This group's admins: " + str(admins)))
                        print(f"[PM] group members have been sent to: {source}.")
                    elif cmd == "quit" and myGroupManager.remove_group_member(group_name, source):
                        myGroupManager.send_group_message(group_name, Message("sm", None, source + " has left the group."), myUserManager)
                        myUserManager.set_user_conv(source, None)
                        send(conn, Message("sm", None, "You have left this group."))
                        print(f"[PM] {source} has removed {content} from group {group_name}.")
                    elif myUserManager.user_exists(content) and myGroupManager.is_group_admin(group_name, source):
                        if cmd == "add" and myGroupManager.add_group_member(group_name, content):
                            myGroupManager.send_group_message(group_name, Message("sm", None, content + " has been added by " + source + "."), myUserManager)
                            myUserManager.send_system_message(content, Message("sm", None, "You have been added to " + group_name + " by " + source + "."))
                            print(f"[PM] {source} has added {content} to group {group_name}.")
                        elif cmd == "remove" and myGroupManager.remove_group_member(group_name, content):
                            myGroupManager.send_group_message(group_name, Message("sm", None, content + " has been removed by " + source + "."), myUserManager)
                            myUserManager.set_user_conv(content, None)
                            myUserManager.send_system_message(content, Message("sm", None, "You have been removed from " + group_name + " by " + source + "."))
                            print(f"[PM] {source} has removed {content} from group {group_name}.")
                        elif cmd == "add_admin" and myGroupManager.add_group_admin(group_name, content):
                            myGroupManager.send_group_message(group_name, Message("sm", None, content + " has been made admin by " + source + "."), myUserManager)
                            print(f"[PM] {source} has made {content} admin in group {group_name}.")
                    else:
                        send(conn, Message("sm", None, "You have failed to preform this action."))
                        print(f"[PM] {source} has failed to preform this group action.")
                elif cmd == "create":
                    parts = content.split(": ")
                    name = parts[0]
                    members = parts[1].split(", ")
                    for member in members:
                        if not myUserManager.user_exists(member):
                            members.remove(member)
                    if myGroupManager.add_group(name, source, members):
                        for mem in members:
                            myUserManager.send_system_message(mem, Message("sm", None, "You have been added to " + name + " by " + source + "."))
                        send(conn, Message("sm", None, "You have created the group: " + name))
                        print(f"[PM] {source} has created the group {name} with members: {members}.")
                elif cmd == "pm":
                    if myUserManager.get_user_by_name(source).get_conv() is None:
                        send(conn, Message("sm", None, "You must be in a conversation to send a message."))
                        print(f"[PM] {source} failed to send a message.")
                    else:
                        to_conv = myUserManager.get_user_by_name(source).get_conv()
                        if myGroupManager.is_exists(to_conv):
                            myGroupManager.send_group_message(to_conv, Message("pm", source, content), myUserManager)
                        else:
                            myConversationManager.send_conv_message(source, to_conv, Message("pm", source, content), myUserManager.get_user_by_name(to_conv))

                        print(f"[PM] {source} sent message to {to_conv}")
    conn.close()



def handle_msg_queue(conn, queue):
    while True:
        if not queue.empty():
            msg = queue.get()
            send(conn, msg)

def handle_server_cmd():
    while True:
        cmd = input("")
        if cmd == "users":
            print(myUserManager.get_users_creds())
        elif cmd == "groups":
            print(myGroupManager.get_group_names())

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    thread3 = Thread(target=handle_server_cmd)
    thread3.start()
    while True:
        queue = Queue()
        conn, addr = server.accept()
        thread1 = Thread(target=handle_client, args=(conn, addr, queue))
        thread1.start()
        thread2 = Thread(target=handle_msg_queue, args=(conn, queue))
        thread2.start()


print("[STARTING] server is starting...")
start()