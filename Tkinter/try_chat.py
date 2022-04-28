from tkinter import *
from tkinter import ttk
import tkinter as tk

msgs = []
chat_name = "Hunteam"
root = tk.Tk()
root.resizable(True, True)
root.title(chat_name)
root.geometry("800x800")
root.configure(bg="black")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

total_lines = 0

start = 0
end = 0

def place_labels(msgs):
    labels = []
    i = 0
    for msg in msgs:
        my_label = Label(second_frame, text=msg, bg="black", fg="green", anchor=NW, font=("Helvetica", "20"))
        my_label.grid(column=0, row=i, sticky=NW)
        labels.append(my_label)
        i += 1
    return labels

def destroy_labels(labels):
    for label in labels:
        label.destroy()

def mouse_wheel(event):
    global start
    # respond to Linux or Windows wheel event
    if len(msgs) > 21:
        if event.num == 5 or event.delta == -120:
            start -= 1
        if event.num == 4 or event.delta == 120:
            start += 1
    global curr_labels
    destroy_labels(curr_labels)
    curr_labels = place_labels(msgs[start:])

# with Windows OS
root.bind("<MouseWheel>", mouse_wheel)


frame = tk.Frame(root, bg="black", borderwidth=20)
frame.grid(row=1, column=0, sticky='nsew')

for i in range(3):
    print(i)
    frame.columnconfigure(i, weight=1)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=10)
frame.rowconfigure(2, weight=1)


def get_msg(event):
    msg = mess_input.get()
    mess_input.delete(0, 'end')
    global msgs
    msgs.append(msg)
    global start
    if len(msgs) > 21:
        start = len(msgs) - 21
    global curr_labels
    destroy_labels(curr_labels)
    print(msgs)
    print(len(msgs))
    print(msgs[start:])
    curr_labels = place_labels(msgs[start:])



tk.Label(frame, text=chat_name, bg="black", fg="green", font=("Helvetica", "30")).grid(row=0, column=1, sticky="N")

mess_input = tk.Entry(frame, text='time', bg="black", fg="green", width=100, font=("Helvetica", "20"), borderwidth=20)
mess_input.grid(row=7, column=1, sticky=tk.S)
mess_input.bind('<Return>', get_msg)

# Create a main frame
main_frame = Frame(frame, bg="black", height=900, width=1500)
main_frame.grid(row=1, column=0, sticky=S, columnspan=3)

# Create a canvas
my_canvas = Canvas(main_frame, bg="black", height=900, width=1500)
my_canvas.pack(sid=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to the canvas

# Configure the canvas
# create another frame inside the canvas
second_frame = Frame(my_canvas, bg="black", height=900, width=1500)
# Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor=NW)




curr_labels = place_labels(msgs)



mainloop()