import pickle
from User import User, UserManager
import os
from queue import Queue

from Message import Message

from User import User, UserManager

class Conversation:
    def __init__(self, user1,  user2):
        users = sorted([user1, user2])

        self.user1 = users[0]
        self.user2 = users[1]
        self.messages = []

    def get_users(self):
        return self.user1, self.user2

    def set_users(self, user1, user2):
        self.user1 = user1
        self.user2 = user2

    def get_messages(self):
        return self.messages

    def add_message(self, message):
        self.messages.append(message)

    def add_messages(self, messages):
        self.messages = self.messages + messages

    def send_message(self, message, user):
        self.messages.append(message)
        source = message.get_source()
        if user.get_conv() == source:
            queue = user.get_queue()
            queue.put(message)
            return True
        return False

    def send_db(self, dest, user):
        queue = user.get_queue()
        for message in self.get_messages():
            queue.put(message)


class ConversationManager:
    def __init__(self):
        self.conversations = []
        self.PATH = os.getcwd() + "/db_conversations.txt"
        if os.path.exists(self.PATH):
            db = open(self.PATH, "rb")
            db = pickle.load(db)
            self.conversations = db.get_conversations()

    def get_conversations_info(self):
        conv_info = []
        for conv in self.conversations:
            users = [conv.get_users()]
            messages = conv.get_messages()
            info = [users, messages]
            conv_info.append(info)
        return conv_info

    def save(self):
        db = open(self.PATH, "wb")
        pickle.dump(self, db)
        db.close()

    def get_conversations(self):
        return self.conversations

    def get_conv(self, user1, user2):
        users = sorted([user1, user2])
        for conv in self.conversations:
            if users == list(conv.get_users()):
                return conv
        return False

    def is_exists(self, user1, user2):
        users = sorted([user1, user2])
        for conv in self.conversations:
            if users == list(conv.get_users()):
                return True
        return False

    def add_conversation(self, user1, user2):
        if self.is_exists(user1, user2):
            return False
        conv = Conversation(user1, user2)
        self.conversations.append(conv)
        self.save()
        return True

    def send_conv_db(self, entree, entered, user):
        conv = self.get_conv(entree, entered)
        conv.send_db(entree, user)
        self.save()

    def send_conv_message(self, source, dest, message, user):
        conv = self.get_conv(source, dest)
        conv.send_message(message, user)
        self.save()
