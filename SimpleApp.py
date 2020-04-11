import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.mondialLabel = tk.Label(self, text='Hello World')
        self.mondialLabel.config(bg="#00ffff")
        self.mondialLabel.grid()
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()


app = Application()
app.master.title('Sample application')
app.mainloop()

# line 1: Hashbang directive to the program launcher, allowing the selection of an appropriate interpreter executable, when self-executing.
# line 2: This line imports the tkinter module into your program's namespace, but renames it as tk.
# line 4: The application class inherits from Tkinter's Frame class.
# line 6: Defines the function that sets up the Frame
# line 7: Calls the constructor for the parent class, Frame.
# line 11: Defining the widgets
# line 12: Creates a label, named MondialLabel with the text "Hello World"
# line 13: Sets the MondialLabel background colour to cyan
# line 14: Places the label on the application so it is visible using the grid geometry manager method
# line 15: Creates a button labeled “Quit”.
# line 16: Places the button on the application. Grid, place and pack are all methods of making the widget visible
# line 18: The main program starts here by instantiating the Application class.
# line 19: This method call sets the title of the window to “Sample application”.
# line 20: Starts the application's main loop, waiting for mouse and keyboard events.
