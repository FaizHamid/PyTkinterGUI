from tkinter import *

root = Tk()

# Creating a Label widget and Shoving it onto screen
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My Name is John Doe").grid(row=1, column=3)
myLabel3 = Label(root, text="                   ").grid(row=1, column=2)

# Shoving it onto the screen in separate step to keep the code look clean
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=3)
# myLabel3.grid(row=1, column=2)


root.mainloop()
