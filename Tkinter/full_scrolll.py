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

frame = tk.Frame(root, bg="black", borderwidth=20)
frame.grid(row=1, column=0, sticky='nsew')

for i in range(3):
    print(i)
    frame.columnconfigure(i, weight=1)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=10)
frame.rowconfigure(2, weight=1)


def get_msg(event):
    mess = mess_input.get()
    mess_input.delete(0, 'end')
    global curr_mess_row
    Label(second_frame, text="hry", bg="black", fg="green", font=("Helvetica", "20")).grid(row=curr_mess_row, column=0, pady=10, padx=10)
    curr_mess_row += 1



tk.Label(frame, text=chat_name, bg="black", fg="green", font=("Helvetica", "30")).grid(row=0, column=1, sticky="N")

mess_input = tk.Entry(frame, text='time', bg="black", fg="green", width=100, font=("Helvetica", "20"), borderwidth=20)
mess_input.grid(row=7, column=1, sticky=tk.S)
mess_input.bind('<Return>', get_msg)

# Create a main frame
main_frame = Frame(frame, bg="black", height=900, width=1500)
main_frame.grid(row=1, column=0, sticky=tk.S, columnspan=3)

# Create a canvas
my_canvas = Canvas(main_frame, bg="black", height=900, width=1500)
my_canvas.pack(sid=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
# create another frame inside the canvas
msgs_label = Label(my_canvas, bg="black", height=900, width=1500)
# Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=msgs_label, anchor="nw")


mainloop()