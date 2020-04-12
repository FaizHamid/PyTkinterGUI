from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Drop Down Boxes for Netflix')
root.iconbitmap('/Users/faizhamid/PycharmProjects/PyTkinterGUI/images/netflix-icon16pixel.png')
root.geometry("400x400")


# Drop Down Boxes

def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
# clicked.set("Day")
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
