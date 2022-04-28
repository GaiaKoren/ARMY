import Message

import json

import os

import pickle

PATH = os.getcwd() + "/db_group_members.txt"

MSG_PATH = os.getcwd() + "/groups"

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'


class Group:
    def __init__(self, name, admins):
        self.name = name
        self.admin = []
        self.members = []
        self.messages = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


    def get_members(self):
        return self.members

    def set_members(self, members):
        self.members = members

    def is_member(self, user):
        if user in self.members:
            return True
        return False

    def add_member(self, name):
        if self.is_member(name):
            return False
        self.members.append(name)
        return True

    def remove_member(self, name):
        if self.is_member(name):
            self.members.remove(name)
            if len(self.members) == 0:
                return "bad"
            if self.is_admin(name):
                self.admins.remove(name)
            if len(self.admins) == 0:
                self.admins.append(self.members[0])
            return True
        return False

    def get_admins(self):
        return self.admins

    def set_admins(self, admins):
        self.admins = admins

    def is_admin(self, admin):
        if admin in self.admins:
            return True
        return False

    def add_admin(self, admin):
        if self.is_admin(admin) or not self.is_member(admin):
            return False
        self.admins.append(admin)
        return True

    def remove_admin(self, admin):
        if self.is_admin(admin):
            self.admins.remove(admin)
            return True
        return False

    def get_messages(self):
        return self.messages

    def add_message(self, message):
        self.messages.append(message)

    def add_messages(self, messages):
        self.messages = self.messages + messages

    def send_message(self, message, userManager):
        self.messages.append(message)
        source = message.get_source()
        for member in self.members:
            print(member)
            if member != source:
                user = userManager.get_user_by_name(member)
                if user.get_conv() == self.name:
                    queue = user.get_queue()
                    queue.put(message)
        return False

    def send_db(self, user_name, userManager):
        queue = userManager.get_user_queue(user_name)
        for message in self.get_messages():
            queue.put(message)

class GroupManager:
    def __init__(self):
        self.groups = []
        self.PATH = os.getcwd() + "/db_groups.txt"
        if os.path.exists(self.PATH):
            db = open(self.PATH, "rb")
            db = pickle.load(db)
            self.groups = db.get_groups()

    def save(self):
        db = open(self.PATH, "wb")
        pickle.dump(self, db)
        db.close()

    def set_groups(self):
        return self.groups

    def get_group(self, name):
        for group in self.groups:
            if name == group.get_name():
                return group
        return False

    def get_groups(self):
        return self.groups

    def get_group_names(self):
        groups = []
        for group in self.groups:
            groups.append(group.get_name())
        return groups

    def is_exists(self, name):
        for group in self.groups:
            if name == group.get_name():
                return True
        return False

    def add_group(self, name, admin, members):
        if self.is_exists(name):
            return False
        group = Group(name, admin)
        members.append(admin)
        group.set_members(members)
        group.set_admins([admin])
        self.groups.append(group)
        self.save()
        return True

    def get_group_admins(self, name):
        group = self.get_group(name)
        return group.get_admins()

    def set_group_admins(self, name, admins):
        group = self.get_group(name)
        group.set_admins(admins)

    def add_group_admin(self, name, admin):
        group = self.get_group(name)
        return group.add_admin(admin)

    def remove_group_admin(self, name, admin):
        group = self.get_group(name)
        return group.remove_admin(admin)

    def is_group_admin(self, name, user):
        if user in self.get_group_admins(name):
            return True
        return False

    def is_group_member(self, name, user):
        if user in self.get_group_members(name):
            return True
        return False

    def get_group_members(self, name):
        group = self.get_group(name)
        return group.get_members()

    def set_group_members(self, name, members):
        group = self.get_group(name)
        group.set_members(members)

    def add_group_member(self, name, member):
        group = self.get_group(name)
        return group.add_member(member)

    def remove_group_member(self, name, member):
        group = self.get_group(name)
        return group.remove_member(member)

    def send_group_db(self, name, user_name, userManager):
        conv = self.get_group(name)
        conv.send_db(user_name, userManager)
        self.save()

    def send_group_message(self, group_name, message, userManager):
        conv = self.get_group(group_name)
        conv.send_message(message, userManager)
        self.save()
