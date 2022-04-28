from tkinter import *
import Message
import Network
from threading import Thread


from tkinter import *
class chat_gui():
    def __init__(self, chat_name):
        self.chat_name = chat_name
        self.convos = []
        root = Tk()
        root.geometry("1000x1000")
        root.configure(bg="black")
        root.title("Cyber Threats")
        for i in range(3):
            root.columnconfigure(i, weight=1)
        self.MSGS_FRAME_WIDTH = 1630
        self.BUTTON_WIDTH = 100
        MSGS_FRAME_HEIGHT = 780
        self.LINES_NUM = 14
        self.start = 0


        root.bind("<MouseWheel>", self.mouse_wheel)
        info_frame = Frame(root, bg="black")
        info_frame.grid(row=0, column=1, sticky="N")
        self.info_button = Button(info_frame, width=60, activeforeground="green", activebackground="black", text="Cyber Threats", bg="black", fg="green", font=("Helvetica", "30"))
        self.info_button.grid(row=0, column=1, sticky="N")
        self.exit_button = Button(info_frame, activeforeground="green", activebackground="black", text="exit", bg="black", fg="green", font=("Helvetica", "30"))
        self.exit_button.grid(row=0, column=0, sticky="N")
        self.settings_button = Button(info_frame, activeforeground="green", activebackground="black", text="settings", bg="black", fg="green", font=("Helvetica", "30"))
        self.settings_button.grid(row=0, column=3, sticky="N")

        main_frame = Frame(root, bg="black", height=MSGS_FRAME_HEIGHT, width=self.MSGS_FRAME_WIDTH, borderwidth=20)
        main_frame.grid(row=1, column=0, sticky=S, columnspan=3)

        my_canvas = Canvas(main_frame, highlightthickness=0, bg="black", height=MSGS_FRAME_HEIGHT, width=self.MSGS_FRAME_WIDTH)
        my_canvas.pack(sid=LEFT, fill=BOTH, expand=1)

        self.second_frame = Frame(my_canvas, bg="black", height=MSGS_FRAME_HEIGHT, width=self.MSGS_FRAME_WIDTH)
        my_canvas.create_window((0, 0), window=self.second_frame, anchor=NW)
        thread_send = Thread(target=self.user_input_thread, args=())
        thread_send.start()

        mainloop()




    def user_input_thread(self):
        while True:
            cmd = input("enter: ")
            self.add_convo(cmd)

    def on_settings(self):
        pass

    def on_exit(self):
        pass
    def on_info(self):
        pass



    def place_buttons(self, buttons):
        if self.start >= 1:
            self.ungrid_button(buttons, self.start-1)
        i = 0
        for button in buttons[self.start:]:
            button.pack()
            i += 1

    def mouse_wheel(self, event):
        if len(self.convos) > self.LINES_NUM:
            if event.delta == 120 and self.start > 0:
                self.start -= 1
            if event.delta == -120 and len(self.convos) - self.start > self.LINES_NUM:
                self.start += 1
            self.place_buttons(self.convos)

    def ungrid_button(self, buttons, ind):
        to_ungrid = buttons[ind]
        txt = to_ungrid.cget("text")
        my_button = Button(self.second_frame, width=self.BUTTON_WIDTH, text=txt, bg="black", fg="green", anchor='w', justify=LEFT, font=("Helvetica", "20"))
        buttons[ind] = my_button
        to_ungrid.destroy()

    def add_convo(self, group_name):
        if group_name != "":
            my_button = Button(self.second_frame, text=group_name, width=self.BUTTON_WIDTH, bg="black", fg="green", anchor='w', justify=LEFT, font=("Helvetica", "20"))
            self.convos.append(my_button)
            if len(self.convos) > self.LINES_NUM:
                self.start = len(self.convos) - self.LINES_NUM
            self.place_buttons(self.convos)




myTeam = chat_gui("hunteam")