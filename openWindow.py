import tkinter as tk
import time
import random
from tkinter.constants import CURRENT
from system import System
from pet import PetAnimState, PetState
from vector2 import Vector2
import monitor
import os
#from makeNotes import *

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
        self.window.title('Meme')
        #self.window.mainloop()
        #self.window.after(0,self.update)
        self.window.protocol("WM_DELETE_WINDOW",self.close) # The X button now calls self.close
       

    def update(self):
        self.window.geometry('+{x}+{y}'.format(x=str(self.pos.x),y=str(self.pos.y)))
        #self.window.update()

    def close(self):
        self.closing = True


class OpenWindow(System):
    def __init__(self, delay=0, action_state=PetState.DEFAULT, windows=[]):
        self.windows = windows
        # State 0 = GOING TO CORNER
        # State 1 = MOVING WINDOW
        self.state = 0

        self.tempMonitor = monitor.getMonitorOnScrPos(Vector2(0,0))
        super().__init__(delay=delay, action_state=action_state)

    def on_enter(self, pet):
        self.state = 0
        self.screenDir = random.randint(0,1) # 0 for left side, 1 for right side
        screenXPos = -100
        if self.screenDir == 1:
            screenXPos = self.tempMonitor.width + 100
        # Corner is where the dog runs to and where the window spawns
        self.corner = Vector2(screenXPos,random.randint(200,self.tempMonitor.height-200))
        if self.screenDir == 0:
            pet.set_anim_state(PetAnimState.WALK_LEFT)
        else:
            pet.set_anim_state(PetAnimState.WALK_RIGHT)
            pet.window.update()
            self.corner.x = self.corner.x - pet.window.winfo_width()
        return

    def action(self,pet):
        #print("Monitor height = ",monitor.getMonitorOnScrPos(Vector2(0,0)).height)
        
        # Going towards the corner
        if self.state == 0:
            #print("IT'S RUNNING in state 0")
            direction = self.corner.__sub__(pet.pos)
            normal = direction.normalised()
            pet.translate(round(normal.x),round(normal.y))
            # Has reached destination
            
            if direction.length() < 1:
                pet.pos = self.corner
                self.state = 1
                filePaths = os.listdir('images')
                randomPath = filePaths[random.randint(0,len(filePaths)-1)]
                self.targetWindow = window('images/' + randomPath,0,0)
                # update() is required to update the window width, otherwise it returns 1
                self.targetWindow.window.update()
                #self.targetWindow = Notepad()
                self.windows.append(self.targetWindow)
                # Spawning the window
                if self.screenDir == 0:
                    self.targetWindow.pos = self.corner.__sub__(Vector2(self.targetWindow.window.winfo_width(),0))
                    pet.set_anim_state(PetAnimState.WALK_RIGHT)
                else:
                    self.targetWindow.pos = self.corner.__add__(Vector2(pet.window.winfo_width(),0))
                    pet.set_anim_state(PetAnimState.WALK_LEFT)
        # Pushing/Pulling the window
        elif self.state == 1:
            direction = Vector2(0,0)
            if self.screenDir == 0:
                direction.x = 1
            else:
                direction.x = -1
            #print("IT'S RUNNING in state 1")
            pet.translate(direction.x,direction.y)
            self.targetWindow.pos = self.targetWindow.pos.__add__(direction)
            #print("Monitor width = ", self.tempMonitor.width)
            if self.screenDir == 0:
                if pet.pos.x >= self.tempMonitor.width/2:
                    #pet.set_anim_state(PetAnimState.IDLE)
                    pet.change_state(PetState.IDLE)
            else:
                if pet.pos.x <= self.tempMonitor.width/2:
                    #pet.set_anim_state(PetAnimState.IDLE)
                    pet.change_state(PetState.IDLE)


    