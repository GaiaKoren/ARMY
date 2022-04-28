from tkinter import *
from tkinter import messagebox

chat_name = "Hunteam"
root = Tk()
root.title(chat_name)
root.geometry("1200x1200")
root.configure(bg="black")


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)


root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

frame = Frame(root, bg="black", height=400, width=400)


def print_entry(event):
    print(mess_input.get())


label_title = Label(root, width=50, borderwidth=0, text=chat_name, bg="black", fg="green", font=100)
label_title.grid(row=0, column=1)
frame.grid(row=1, column=1)
#mess1 = Label(frame, text="message!", bg="black", fg="green", font=50)
#mess1.pack()
mess_input = Entry(frame, width=100, borderwidth=5, bg="black", fg="green", font=50)
mess_input.grid(row=2, column=1)
mess_input.bind('<Return>', print_entry)
#mess2 = Label(frame, text="message!", bg="black", fg="green", font=50)
#mess2.pack()
root.mainloop()