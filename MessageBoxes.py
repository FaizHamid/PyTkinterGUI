from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Boxes for Netflix')
root.iconbitmap('/Users/faizhamid/PycharmProjects/PyTkinterGUI/images/Netflix.ico')


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


# function of showinfo
def popup():
    response = messagebox.showinfo("This is my Popup", "Hello World!")
    Label(root, text=response).pack()


# # function of showwarning
# def popup():
#     response = messagebox.showwarning("This is my Popup", "Hello World!")
#     Label(root, text=response).pack()


# # function of showerror
# def popup():
#     response = messagebox.showerror("This is my Popup", "Hello World!")
#     Label(root, text=response).pack()


# # function of askquestion
# def popup():
#     response = messagebox.askquestion("This is my Popup", "Hello World!")
#     Label(root, text=response).pack()
#     if response == YES:
#         Label(root, text="You clicked Yes!").pack()
#     else:
#         Label(root, text="You clicked No!").pack()


# function of askyokcancel
# def popup():
#     response = messagebox.askokcancel("This is my Popup", "Hello World!")
#     Label(root, text=response).pack()


# function of askyesno
# def popup():
#     response = messagebox.askyesno("This is my Popup", "Hello World!")
# Label(root, text=response).pack()
# if response == 1:
#     Label(root, text="You clicked Yes!").pack()
# else:
#     Label(root, text="You clicked No!").pack()


Button(root, text="Popup", command=popup).pack()

mainloop()
