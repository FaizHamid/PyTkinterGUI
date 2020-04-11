from tkinter import *

root = Tk()

# Creating entry widget
e = Entry(root, width=50, borderwidth=5, bg="blue", fg="white")
e.pack()
e.insert(0, "Enter your Name: ")


# Creating function
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


# Creating Button widgets and Shoving them to screen
myButton = Button(root, text="Enter Your Name!", command=myClick, fg="blue",
                  bg="#ffffff")  # Hex color code for black #000000
myButton.pack()

root.mainloop()
