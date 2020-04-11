from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Buttons for Netflix')
root.iconbitmap('/Users/faizhamid/PycharmProjects/PyTkinterGUI/images/Netflix.ico')

r = IntVar()
r.set("2")


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()

mainloop()
