from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Check Boxes for Netflix')
root.iconbitmap('/Users/faizhamid/PycharmProjects/PyTkinterGUI/images/netflix-icon16pixel.png')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()


# var = IntVar()
# c = Checkbutton(root, text="Check this Box!", variable=var)

var = StringVar()
c = Checkbutton(root, text="Check this Box!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
