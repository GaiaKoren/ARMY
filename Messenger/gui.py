from tkinter import *

import Message
import Network


class LoginWin():
    def __init__(self, client):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.configure(bg="black")

        self.client = client
        self.root.title("Login page")
        self.frame = Frame(self.root, bg="black")

        self.frame.pack(expand=True)

        label_username = Label(self.frame, width=50, borderwidth=5, text="username", bg="black", fg="green", font=("Helvetica", "15"))
        label_username.grid(row=0, column=0, columnspan=3, padx=0, pady=10)

        label_password = Label(self.frame, width=50, borderwidth=5, text="password", bg="black", fg="green", font=("Helvetica", "15"))
        label_password.grid(row=2, column=0, columnspan=3, padx=0, pady=10)

        self.e_username = Entry(self.frame, width=50, borderwidth=5, bg="black", fg="green", font=("Helvetica", "15"))
        self.e_username.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.e_password = Entry(self.frame, width=50, borderwidth=5, bg="black", fg="green", font=("Helvetica", "15"))
        self.e_password.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.login_button = Button(self.frame, text="Sign in", bg="black", fg="green", font=("Helvetica", "15"), command=self.login)
        self.login_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.register_button = Button(self.frame, text="Don't have a user yet?", bg="green", fg="black", font=("Helvetica", "12"), command=self.set_up_register)
        self.register_button.grid(row=5, column=0, columnspan=3, padx=10, pady=20)
        self.msg_label = Label(self.frame, width=50, borderwidth=40, text="   ", bg="black", fg="green", font=("Helvetica","40"))
        self.msg_label.grid(row=6, column=0, columnspan=3, padx=10, pady=20)
        self.root.mainloop()

    def login(self):
        username = self.e_username.get()
        password = self.e_password.get()
        if username != "" and password != "":
            Network.send(self.client, Message.Message("login", None, [username, password]))
        msg = Network.receive_message(self.client).get_content()
        if msg == "You have successfully logged in.":
            self.root.destroy()
        elif msg == "User credentials are incorrect.":
            self.msg_label.configure(text="User credentials are incorrect.")

    def register(self):
        username = self.e_username.get()
        password = self.e_password.get()
        if username != "" and password != "":
            Network.send(self.client, Message.Message("register", None, [username, password]))
        msg = Network.receive_message(self.client).get_content()
        if msg == "You have successfully registered.":
            self.root.destroy()
        elif msg == "This username is already in use...":
            self.msg_label.configure(text="This username is already in use...")

    def set_up_login(self):
        self.login_button.configure(text="Sign in", command=self.login, font=("Helvetica", "15"), bg="black", fg="green")
        self.register_button.configure(text="Don't have a user yet?", command=self.set_up_register, font=("Helvetica", "12"), bg="green", fg="black")
        self.login_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        self.register_button.grid(row=5, column=0, columnspan=3, padx=10, pady=20)
        self.msg_label.configure(text=" ")
    def set_up_register(self):
        self.login_button.configure(text="Already have a user?", command=self.set_up_login, font=("Helvetica", "12"), bg="green", fg="black")
        self.register_button.configure(text="Register", command=self.register, font=("Helvetica", "15"), bg="black", fg="green")
        self.login_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        self.register_button.grid(row=4, column=0, columnspan=3, padx=10, pady=20)
        self.msg_label.configure(text=" ")

