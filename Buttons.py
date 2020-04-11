from tkinter import *

root = Tk()


# Creating function
def myClick():
    myLabel = Label(root, text="Look I clicked a button!!!")
    myLabel.pack()


# Creating Button widgets and Shoving them to screen
myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="#ffffff")  # Hex color code for black #000000
myButton.pack()

root.mainloop()
