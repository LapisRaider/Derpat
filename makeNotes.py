import tkinter as tk
import time
import random
from tkinter.constants import CURRENT
from system import System
from pet import PetAnimState, PetState
from vector2 import Vector2
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad():
    notes = ["STORE", "YOUR", "MEME", "MESSAGES", "HERE"]
    noteLen = len(notes)    
    note = notes[random.randint(0, noteLen - 1)]

    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)

    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    
    __thisTextArea.insert(tk.END, note)
 
    def __init__(self, **kwargs):
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
        self.__thisTextArea.grid(sticky=N + E + S + W)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def update(self):
        self.__root.geometry('+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
        #self.window.update()

    # def run(self):
    #     # Run main application
    #     self.__root.mainloop()

#notepad.run()