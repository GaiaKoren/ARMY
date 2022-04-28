from tkinter import *

root = Tk()

def myClick():
    print("hey")


myButton = Button(root, text="Click Me!", command=myClick)
myButton.grid(row=0, column=0)



root.mainloop()