import pickle

import os

class User:
    def __init__(self, name,  password, queue, conv):
        self.name = name
        self.password = password
        self.queue = queue
        self.conv = conv
        self.convo = []
        self.system_messages = []

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_queue(self):
        return self.queue

    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password

    def set_queue(self, queue):
        self.queue = queue

    def get_conv(self):
        return self.conv

    def set_conv(self, conv):
        self.conv = conv

    def get_sms(self):
        return self.system_messages

    def set_sms(self, sms):
        self.system_messages = sms

    def add_sm(self, sm):
        self.system_messages.append(sm)

    def remove_sm(self, sm):
        self.system_messages.remove(sm)

    def get_convos(self):
        return self.system_messages

    def set_convos(self, convos):
        self.convos = convos

    def add_convos(self, convo):
        self.convos.append(convo)

    def remove_convos(self, convo):
        self.system_messages.remove(convo)



class UserManager:
    def __init__(self):
        self.users = []
        self.PATH = os.getcwd() + "/db_users.txt"
        if os.path.exists(self.PATH):
            db = open(self.PATH, "rb")
            users_list = pickle.load(db)
            for u in users_list:
                newUser = User(u[0], u[1], None, None)
                newUser.set_sms(u[2])
                newUser.set_convos(u[3])
                self.users.append(newUser)

    def save(self):
        users_list = self.get_users_save()
        db = open(self.PATH, "wb")
        pickle.dump(users_list, db)
        db.close()

    def delete(self):
        db = open(self.PATH, "w")
        db.write("")
        db.close()

    def get_users(self):
        return self.users

    def get_user_names(self):
        names = []
        for user in self.users:
            names.append(user.get_name())
        return names

    def get_user_password(self, name):
        for user in self.users:
            if user.get_name() == name:
                return user.get_password()

    def get_user_conv(self, name):
        if self.is_logged_in(name):
            return self.get_user_by_name(name).get_conv()
        return False

    def set_user_conv(self, name, conv):
        if self.is_logged_in(name):
            self.get_user_by_name(name).set_conv(conv)
            return True
        return False

    def get_users_info(self):
        us = []
        for user in self.users:
            us.append([user.get_name(), user.get_password(), user.get_queue(), user.get_conv()])
        return us

    def get_users_save(self):
        us = []
        for user in self.users:
            us.append([user.get_name(), user.get_password(), user.get_sms(), user.get_convos()])
        return us

    def get_users_creds(self):
        us = []
        for user in self.users:
            us.append([user.get_name(), user.get_password()])
        return us

    def get_user_queue(self, name):
        for user in self.users:
            if user.get_name() == name:
                return user.get_queue()

    def is_logged_in(self, name):
        for user in self.users:
            if user.get_name() == name:
                if user.get_queue() is not None:
                    return True
        return False

    def set_user_queue(self, name, queue):
        for user in self.users:
            if user.get_name() == name:
                user.set_queue(queue)
                return True
        return False

    def is_password(self, name, password):
        return password == self.get_user_password(name)

    def user_login(self, name, password, queue):
        if self.is_password(name, password):
            user = self.get_user_by_name(name)
            user.set_queue(queue)
            for m in user.get_sms():
                queue.put(m)
            user.set_sms([])
            return True
        return False

    def user_logout(self, name):
        if self.is_logged_in(name):
            self.set_user_queue(name, None)
            self.set_user_conv(name, None)
            return True
        return False

    def user_exists(self, username):
        if username in self.get_user_names():
            return True
        return False

    def get_user_by_name(self, name):
        for user in self.users:
            if user.get_name() == name:
                return user

    def add_user(self, username, password):
        if self.user_exists(username):
            return False
        self.users.append(User(username, password, None, None))
        self.save()
        return True

    def remove_user(self, username):
        if not self.user_exists(username):
            return False
        user = self.get_user_by_name(username)
        self.users.remove(user)
        self.save()
        return True

    def change_password(self, username, password):
        user = self.get_user_by_name(username)
        if not self.user_exists(user.get_name()):
            return False
        user.set_password(password)
        self.save()
        return True

    def change_username(self, username, new_username):
        user = self.get_user_by_name(username)
        if not self.user_exists(user.get_name()):
            return False
        user.set_name(new_username)
        self.save()
        return True

    def send_system_message(self, name, message):
        queue = self.get_user_queue(name)
        if queue is not None:
            queue.put(message)
        else:
            self.get_user_by_name(name).add_sm(message)
