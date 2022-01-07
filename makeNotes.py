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

class window():
    def __init__(self, x, y):
        self.window = tk.Toplevel()
        # Boolean to prevent the program from closing immediately
        self.closing = False
        # self.img = tk.PhotoImage(file=imagePath)
        self.window.attributes('-topmost',True)
        #newWindow.overrideredirect(True)
        self.pos = Vector2(x,y)
        self.window.geometry('+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
        self.label = tk.Label(self.window, image=self.img, bd=0, bg='black').pack()
        #self.window.mainloop()
        #self.window.after(0,self.update)
        self.window.protocol("WM_DELETE_WINDOW",self.close) # The X button now calls self.close
       
    def update(self):
        self.window.geometry('+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
        self.window.update()

    def close(self):
        self.closing = True

class OpenWindow(System):
    def __init__(self, delay=0, action_state=PetState.DEFAULT, windows=[]):
        self.windows = windows
        # State 0 = GOING TO CORNER
        # State 1 = MOVING WINDOW
        self.state = 0
        super().__init__(delay=delay, action_state=action_state)

    def on_enter(self, pet):
        pet.set_anim_state(PetAnimState.WALK_LEFT)
        print("Notepad")
        return

    def action(self,pet):
        corner = Vector2(0,0)

        # Going towards the corner
        if self.state == 0:
            direction = corner.__sub__(pet.pos)
            normal = direction.normalised()
            pet.translate(round(normal.x),round(normal.y))

            if direction.length() < 2:
                pet.pos = corner
                self.state = 1
                self.targetWindow = window(0, 0)
                print("width=",self.targetWindow.window.winfo_width())
                self.targetWindow.pos = corner.__sub__(Vector2(300,0))
                self.windows.append(self.targetWindow)
                pet.set_anim_state(PetAnimState.WALK_RIGHT)
        # Pushing/Pulling the window
        elif self.state == 1:
            # For now, let it move right
            direction = Vector2(1,0)
            pet.translate(direction.x,direction.y)
            self.targetWindow.pos = self.targetWindow.pos.__add__(direction)

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

    def run(self):
        # Run main application
        self.__root.mainloop()

notepad = Notepad(width=400, height=200)
notepad.run()

print(notepad)