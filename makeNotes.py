import tkinter as tk
import random
from vector2 import Vector2

class Notepad(): 
    def __init__(self, **kwargs):
        notes = ["Your CAP cannot even afford mentos.", "KEITH WAS HERE WOOOO.", "I couldn't think of anything to write.",
         "Your life is like poopoo.", "HEHEXD.", "Am I a Dog? A Cat? You'll never find out ;)", "Bark Bark Meow Meow", "Your mouse looking real good right now", "Doing work? Not when I'm here."]
        noteLen = len(notes)    
        note = notes[random.randint(0, noteLen - 1)]

        self.window = tk.Toplevel()
        self.closing = False

        # default window width and height
        self.thisWidth = 300
        self.hisHeight = 300
        self.thisTextArea = tk.Text(self.window)
        self.thisMenuBar = tk.Menu(self.window)

        # To add scrollbar
        self.thisScrollBar = tk.Scrollbar(self.thisTextArea)
        
        self.thisTextArea.insert(tk.END, note)

        # Set icon
        try:
            self.window.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (the default is 300x300)
        try:
            self.thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.window.title("You have a note!")

        # Center the window
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.thisHeight / 2)

        self.pos = Vector2(left,top)

        # For top and bottom
        self.window.geometry('%dx%d+%d+%d' % (self.thisWidth,
                                              self.thisHeight,
                                              left, top))

        # To make the textarea auto resizable
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.thisTextArea.grid(sticky=tk.N + tk.E + tk.S + tk.W)

        self.window.config(menu=self.thisMenuBar)

        self.thisScrollBar.pack(side=tk.RIGHT, fill=tk.Y)

        # Scrollbar will adjust automatically according to the content
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)
        self.window.protocol("WM_DELETE_WINDOW",self.close)

    def update(self):
        self.window.geometry('+{x}+{y}'.format(x=str(round(self.pos.x)),y=str(round(self.pos.y))))
        self.window.update()

    def close(self):
        self.closing = True