from tkinter import *

msgs = []
chat_name = "Hunteam"
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
widget_width = 250
root.title(chat_name)
root.geometry(str(width) + "x" + str(height - 100))
root.configure(bg="black")

prev_labels = []

total_lines = 0

start = 0
end = 0
labels = []


def place_labels(msgs, ind):
    if start > 0:
        ungrid_label(ind)
    curr_labels = []
    i = 0
    for msg_label in msgs:
        msg_label.grid(column=0, row=i, columnspan=3, sticky=W)
        labels.append(msg_label)
        curr_labels.append(msg_label)
        i += 1
    return curr_labels


def mouse_wheel(event):
    global start
    if len(msgs) > 21:
        if event.delta == 120 and start > 0:
            start -= 1
        if event.delta == -120 and len(msgs) - start > 21:
            start += 1
        global prev_labels
        place_labels(msgs[start:], start - 1)


root.bind("<MouseWheel>", mouse_wheel)

frame = Frame(root, bg="black", borderwidth=20)
frame.grid(row=1, column=0, sticky='nsew')

for i in range(3):
    frame.columnconfigure(i, weight=1)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=10)
frame.rowconfigure(2, weight=1)


def ungrid_label(ind):
    global msgs
    to_ungrid = msgs[ind]
    txt = to_ungrid.cget("text")
    my_label = Label(second_frame, text=txt, bg="black", fg="green", anchor='w', justify=LEFT, font=("Helvetica", "20"))
    msgs[ind] = my_label
    to_ungrid.destroy()


def get_msg(event):
    msg = mess_input.get()
    mess_input.delete(0, 'end')
    if msg != "":
        global msgs
        my_label = Label(second_frame, text=msg, bg="black", fg="green", anchor='w', justify=LEFT,
                         font=("Helvetica", "20"))
        msgs.append(my_label)
        global start
        if len(msgs) > 21:
            start = len(msgs) - 21
        place_labels(msgs[start:], start - 1)
    update_sizes()


def update_sizes():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(screen_height, screen_width)

    """
    name_label.configure(width=screen_width, height=int(screen_height/7))
    main_frame.configure(width=screen_width, height=int(screen_height*6/7))
    my_canvas.configure(width=screen_width, height=int(screen_height*6/7))
    name_label.configure(width=screen_width, height=int(screen_height*6/7))
    mess_input.configure(width=screen_width)

    """


name_label = Label(frame, text=chat_name, bg="black", fg="green", width=widget_width, font=("Helvetica", "30"))
name_label.grid(row=0, column=1, sticky="N")
mess_input = Entry(frame, text='time', bg="black", fg="green", width=widget_width, font=("Helvetica", "20"),
                   borderwidth=20)
mess_input.grid(row=7, column=1, sticky=S)
mess_input.bind('<Return>', get_msg)

# Create a main frame
main_frame = Frame(frame, bg="black", height=800, width=width)
main_frame.grid(row=1, column=0, sticky=S, columnspan=3)

# Create a canvas
my_canvas = Canvas(main_frame, highlightthickness=0, bg="black", height=800, width=width)
my_canvas.pack(sid=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to the canvas

# Configure the canvas
# create another frame inside the canvas
second_frame = Frame(my_canvas, bg="black", height=800, width=width)
# Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor=NW)

mainloop()