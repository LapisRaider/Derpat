import tkinter as tk
import time
import random
from tkinter.constants import CURRENT
from system import System
from pet import PetAnimState, PetState
from vector2 import Vector2

class window():

    def __init__(self, imagePath,x,y):
        self.window = tk.Toplevel()
        # Boolean to prevent the program from closing immediately
        self.closing = False
        self.img = tk.PhotoImage(file=imagePath)
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
        print("I HAVE ENTERED")
        return

    def action(self,pet):
        corner = Vector2(0,0)
        # Going towards the corner
        if self.state == 0:
            #print("IT'S RUNNING in state 0")
            direction = corner.__sub__(pet.pos)
            normal = direction.normalised()
            pet.translate(round(normal.x),round(normal.y))
            if direction.length() < 2:
                pet.pos = corner
                self.state = 1
                self.targetWindow = window('images/panik.png',0,0)
                print("width=",self.targetWindow.window.winfo_width())
                self.targetWindow.pos = corner.__sub__(Vector2(300,0))
                self.windows.append(self.targetWindow)
                pet.set_anim_state(PetAnimState.WALK_RIGHT)
        # Pushing/Pulling the window
        elif self.state == 1:
            # For now, let it move right
            direction = Vector2(1,0)
            #print("IT'S RUNNING in state 1")
            pet.translate(direction.x,direction.y)
            self.targetWindow.pos = self.targetWindow.pos.__add__(direction)


    