import tkinter as tk
import time
import random

from vector2 import Vector2

class window():

    def __init__(self, imagePath,x,y):
        self.window = tk.Toplevel()
        self.closing = False
        self.img = tk.PhotoImage(file=imagePath)
        self.window.attributes('-topmost',True)
        #newWindow.overrideredirect(True)
        self.pos = Vector2(x,y)
        self.window.geometry('+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
        self.label = tk.Label(self.window, image=self.img, bd=0, bg='black').pack()
        #self.window.mainloop()
        #self.window.after(0,self.update)
        self.window.protocol("WM_DELETE_WINDOW",self.close)
       

    def update(self):
        self.window.geometry('+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
        self.window.update()

    def close(self):
        self.closing = True

    