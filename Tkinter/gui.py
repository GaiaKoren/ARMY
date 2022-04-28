from tkinter import *

root = Tk()
root.title("Login page")
root.geometry("800x800")
root.configure(bg="black")
frame = Frame(root, bg="black")

frame.pack(expand=True)

label_username = Label(frame, width=50, borderwidth=5, text="username", bg="black", fg="green", font=(25))
label_username.grid(row=0, column=0, columnspan=3, padx=0, pady=10)

label_password = Label(frame, width=50, borderwidth=5, text="password", bg="black", fg="green", font=(25))
label_password.grid(row=2, column=0, columnspan=3, padx=0, pady=10)

e_username = Entry(frame, width=50, borderwidth=5, bg="black", fg="green", font=(25))
e_username.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

e_password = Entry(frame, width=50, borderwidth=5, bg="black", fg="green", font=(25))
e_password.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

def login():
    print("hey")
    print(e_username.get())
    print(e_password.get())



myButton = Button(frame, text="Sign in", bg="black", fg="green", font=(25), command=login)
myButton.grid(row=4, column=0, columnspan=3, padx=10, pady=10)



root.mainloop()