import tkinter as tk
from tkinter import ttk, Menu
from tkinter import *
from PIL import ImageTk, Image

# Creating a main window
root = Tk()
root.geometry('900x750')
root.title("Netflix")
# Changing the window background
root.configure(bg="black")

# Creating Navigation Button Logo
label = Label(root, text="Netflix", fg="white", bg="black")
label.pack()

menu_bar = Menu(root)


# Creating do nothing function
def donothing():
    filewin = ttk.Toplevel(root)
    button = ttk.Button(filewin, text="Do Nothing Button")
    button.pack()


# Creating My List Menu fucntion
def MyList():
    top = tk.Toplevel()
    top.geometry('700x500')
    top.title("My List")


# Menu Items
home_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="My List", command=donothing)
home_menu.add_separator()



root.mainloop()
