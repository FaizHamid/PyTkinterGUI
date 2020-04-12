from tkinter import *

root = Tk()
root.title('Menu Bar for Netflix')
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)


# Creating donothing function
def our_command():
    my_label = Label(root, text="You clicked a Dropdown Menu!").pack()


# Creating Home Menu Item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New..", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Creating Edit Menu Items
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=root.quit)

# Creating Options Menu Items
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_separator()
option_menu.add_command(label="Find Next", command=root.quit)

root.mainloop()
