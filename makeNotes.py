import tkinter as tk
import random
from vector2 import Vector2

class Notepad(): 
    def __init__(self, **kwargs):
        notes = ["STORE", "YOUR", "MEME", "MESSAGES", "HERE"]
        noteLen = len(notes)    
        note = notes[random.randint(0, noteLen - 1)]

        self.__root = tk.Toplevel()

        # default window width and height
        self.__thisWidth = 300
        self.__thisHeight = 300
        self.__thisTextArea = tk.Text(self.__root)
        self.__thisMenuBar = tk.Menu(self.__root)

        # To add scrollbar
        self.__thisScrollBar = tk.Scrollbar(self.__thisTextArea)
        
        self.__thisTextArea.insert(tk.END, note)

        # Set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (the default is 300x300)
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.__root.title("You have a note!")

        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.pos = Vector2(left,top)

        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=tk.N + tk.E + tk.S + tk.W)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=tk.RIGHT, fill=tk.Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def update(self):
        self.__root.geometry('+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
        self.__root.update()