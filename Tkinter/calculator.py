from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, coloumnspan=3, padx=10, pady=10)

def myClick():
    print("hey")
    print(e.get())


myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()



root.mainloop()