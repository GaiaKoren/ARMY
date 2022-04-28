from tkinter import *

root = Tk()
root.title("Login page")
e = Entry(root, width=50)
e.pack()

def myClick():
    print("hey")
    print(e.get())


myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()



root.mainloop()