from tkinter import *
class chat_gui():
    def __init__(self, chat_name):
        self.chat_name = chat_name
        self.msgs = []
        root = Tk()
        root.geometry("1000x1000")
        root.configure(bg="black")
        root.title(chat_name)
        for i in range(3):
            root.columnconfigure(i, weight=1)
        MSGS_FRAME_WIDTH = 1500
        MSGS_FRAME_HEIGHT = 780
        self.LINES_NUM = 20
        self.start = 0


        root.bind("<MouseWheel>", self.mouse_wheel)
        info_frame = Frame(root, bg="black")
        info_frame.grid(row=0, column=1, sticky="N")
        self.info_button = Button(info_frame, width=60, activeforeground="green", activebackground="black", text=chat_name, bg="black", fg="green", font=("Helvetica", "30"))
        self.info_button.grid(row=0, column=1, sticky="N")
        self.exit_button = Button(info_frame, activeforeground="green", activebackground="black", text="exit", bg="black", fg="green", font=("Helvetica", "30"))
        self.exit_button.grid(row=0, column=0, sticky="N")
        self.settings_button = Button(info_frame, activeforeground="green", activebackground="black", text="settings", bg="black", fg="green", font=("Helvetica", "30"))
        self.settings_button.grid(row=0, column=3, sticky="N")
        self.mess_input = Entry(root, text='time', bg="black", fg="green", width=100, font=("Helvetica", "20"), borderwidth=20)
        self.mess_input.grid(row=2, column=1, sticky=S)
        self.mess_input.bind('<Return>', self.get_msg)

        main_frame = Frame(root, bg="black", height=MSGS_FRAME_HEIGHT, width=MSGS_FRAME_WIDTH, borderwidth=20)
        main_frame.grid(row=1, column=0, sticky=S, columnspan=3)

        my_canvas = Canvas(main_frame, highlightthickness=0, bg="black", height=MSGS_FRAME_HEIGHT, width=MSGS_FRAME_WIDTH)
        my_canvas.pack(sid=LEFT, fill=BOTH, expand=1)

        self.second_frame = Frame(my_canvas, bg="black", height=MSGS_FRAME_HEIGHT, width=MSGS_FRAME_WIDTH)
        my_canvas.create_window((0, 0), window=self.second_frame, anchor=NW)

        mainloop()

    def on_settings(self):
        pass

    def on_exit(self):
        pass
    def on_info(self):
        pass



    def place_labels(self, msg_labels):
        if self.start >= 1:
            self.ungrid_label(msg_labels, self.start-1)
        i = 0
        for msg_label in msg_labels[self.start:]:
            msg_label.grid(column=0, row=i, columnspan=3, sticky=W)
            i += 1

    def mouse_wheel(self, event):
        if len(self.msgs) > self.LINES_NUM:
            if event.delta == 120 and self.start > 0:
                self.start -= 1
            if event.delta == -120 and len(self.msgs) - self.start > self.LINES_NUM:
                self.start += 1
            self.place_labels(self.msgs)

    def ungrid_label(self, msg_labels, ind):
        to_ungrid = msg_labels[ind]
        txt = to_ungrid.cget("text")
        my_label = Label(self.second_frame, text=txt, bg="black", fg="green", anchor='w', justify=LEFT, font=("Helvetica", "20"))
        msg_labels[ind] = my_label
        to_ungrid.destroy()


    def get_msg(self, event):
        msg = self.mess_input.get()
        self.mess_input.delete(0, 'end')
        if msg != "":
            my_label = Label(self.second_frame, text=msg, bg="black", fg="green", anchor='w', justify=LEFT, font=("Helvetica", "20"))
            self.msgs.append(my_label)
            if len(self.msgs) > self.LINES_NUM:
                self.start = len(self.msgs) - self.LINES_NUM
            self.place_labels(self.msgs)



myTeam = chat_gui("hunteam")