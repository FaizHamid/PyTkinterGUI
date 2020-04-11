from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Netflix')
root.iconbitmap('/Users/faizhamid/PycharmProjects/PyTkinterGUI/imges/netflix-icon.png')


my_img = ImageTk.PhotoImage(Image.open("imges/howItEnds.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
