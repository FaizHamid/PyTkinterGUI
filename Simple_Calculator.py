from tkinter import *

root = Tk()
root.title("Simple Calculator")

# Creating Display Widget
e = Entry(root, width=40, borderwidth=5, bg="grey", fg="white")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Creating Functions for Buttons
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "addition"
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "subtraction"
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "multiplication"
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "division"
    e.delete(0, END)


# Creating Button widgets and Shoving them to screen
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=4, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=4, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=4, column=2)

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=3, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=3, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=3, column=2)

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=2, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=2, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=2, column=2)

button_0 = Button(root, text="0", padx=86, pady=20, command=lambda: button_click(0)).grid(row=5, column=0, columnspan=2)
button_equal = Button(root, text="=", padx=86, pady=20, command=button_equal).grid(row=5, column=2,
                                                                                   columnspan=2)
button_clear = Button(root, text="AC", padx=38, pady=20, command=button_clear).grid(row=1, column=0)
button_memory = Button(root, text="M", padx=40, pady=20, command=lambda: button_click()).grid(row=1, column=1)
button_memory_recall = Button(root, text="MR", padx=38, pady=20, command=lambda: button_click()).grid(row=1, column=2)

button_add = Button(root, text="+", padx=40, pady=20, command=button_add).grid(row=4, column=3)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract).grid(row=3, column=3)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply).grid(row=2, column=3)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide).grid(row=1, column=3)

root.mainloop()
