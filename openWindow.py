import tkinter as tk
import time
import random

from vector2 import Vector2

class window():
    def __init__(self, imagePath):
        self.window = tk.Toplevel()

        img = tk.PhotoImage(file=imagePath)
        self.window.attributes('-topmost',True)
        #newWindow.overrideredirect(True)
        self.window.geometry('+0+0')

        self.label = tk.Label(self.window, bd=0, bg='black')
        self.label.configure(image=img)
        self.label.pack()

        self.window.after(0,self.update)
       

    def update(self):
        return None

    def updateRender(self):
        self.window.geometry('+0+0')
        self.window.update()

    