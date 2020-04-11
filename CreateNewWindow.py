from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Create Message Boxes for Netflix')
root.iconbitmap('/Users/faizhamid/PycharmProjects/PyTkinterGUI/images/Netflix.ico')


# top = Toplevel()
# # lbl = Label(top, text="Hello World").pack()
# top.title('Create Message Boxes for Netflix')
# top.iconbitmap('/Users/faizhamid/PycharmProjects/PyTkinterGUI/images/Netflix.ico')
# my_img = ImageTk.PhotoImage(Image.open("images/sherlock.png"))
# my_label = Label(top, image=my_img).pack()

def open():
    global my_img
    top = Toplevel()
    top.title('My Second Window')
    top.iconbitmap('/Users/faizhamid/PycharmProjects/PyTkinterGUI/images/Netflix.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/sherlock.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()
