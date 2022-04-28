from tkinter import *
from tkinter import ttk
import tkinter as tk


chat_name = "Hunteam"
root = tk.Tk()
root.resizable(True, True)
root.title(chat_name)
root.geometry("800x800")
root.configure(bg="black")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

curr_mess_row = 1



def get_msg(event):
    msg = mess_input.get()
    mess_input.delete(0, 'end')
    msgs_list.append(msg)
    msgs.configure(text="\n".join(msgs_list))
    print(curr_mess_row)

msgs_list = []
txt = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
Label(root, text=chat_name, bg="black", fg="green", font=("Helvetica", "30")).pack()
# Create a main frame
msgs = Label(root, text=txt, bg="black", fg="green", font=("Helvetica", "20"))
msgs.pack(side=LEFT)
mess_input = tk.Entry(root, text='time', bg="black", fg="green", width=100, font=("Helvetica", "20"), borderwidth=20)
mess_input.pack()
mess_input.bind('<Return>', get_msg)



"""
for i in range(100):
    Label(second_frame, text="hey", bg="black", fg="green", font=("Helvetica", "20")).grid(row=i, column=0, pady=10, padx=10)


"""

mainloop()