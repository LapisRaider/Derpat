import tkinter as tk
import random
import monitor
import os

from tkinter.constants import CURRENT
from system import System
from pet import PetAnimState, PetState
from vector2 import Vector2
from make_notes import Notepad

class CustomWindow():
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
        self.window.geometry('+{x}+{y}'.format(x=str(round(self.pos.x)),y=str(round(self.pos.y))))
        #self.window.update()

    def close(self):
        self.closing = True

class OpenWindow(System):
    MOVEMENT_SPEED = 200

    def __init__(self, delay=0, action_state=PetState.DEFAULT, windows = []):
        self.windows = windows
        # State 0 = GOING TO CORNER
        # State 1 = MOVING WINDOW
        self.state = 0
        self.active_monitor = monitor.get_active_monitor(Vector2(0,0))
        super().__init__(delay=delay, action_state=action_state)

    def on_enter(self, pet):
        print("On Enter Open Window")
        self.state = 0
        self.screen_dir = random.randint(0,1) # 0 for left side, 1 for right side
        screenXPos = -100
        if self.screen_dir == 1:
            screenXPos = self.active_monitor.width + 100
        # Corner is where the dog runs to and where the window spawns
        self.corner = Vector2(screenXPos,random.randint(200,self.active_monitor.height-200))
        if self.screen_dir == 0:
            pet.set_anim_state(PetAnimState.WALK_LEFT)
        else:
            pet.set_anim_state(PetAnimState.WALK_RIGHT)
            pet.window.update()
            self.corner.x = self.corner.x - pet.window.winfo_width()
        return

    def action(self,pet,delta_time):
        # Going towards the corner.
        if self.state == 0:
            direction = self.corner - pet.pos
            normal = direction.normalised() * OpenWindow.MOVEMENT_SPEED * delta_time
            pet.translate(normal.x,normal.y)

            # Has reached destination.
            if direction.length() < 2:
                pet.pos = self.corner
                self.state = 1
                
                self.spawn_notepad = random.randint(0,1) # 0 for False, 1 for True
                if self.spawn_notepad == 0:
                    file_paths = os.listdir('assets/images')
                    randomPath = file_paths[random.randint(0,len(file_paths)-1)]
                    self.target_window = CustomWindow('assets/images/' + randomPath,0,0)
                    # update() is required to update the window width, otherwise it returns 1
                    self.target_window.window.update()
                else:
                    self.target_window = Notepad(width=300,height = 300)

                pet.window.lift()
                self.windows.append(self.target_window)
                
                # Spawning the window.
                if self.screen_dir == 0:
                    if self.spawn_notepad == 0:
                        self.target_window.pos = self.corner.__sub__(Vector2(self.target_window.window.winfo_width(),0))
                    else:
                        self.target_window.pos = self.corner.__sub__(Vector2(self.target_window.width,0))
                    pet.set_anim_state(PetAnimState.WALK_RIGHT)
                else:
                    self.target_window.pos = self.corner.__add__(Vector2(pet.window.winfo_width(),0))
                    pet.set_anim_state(PetAnimState.WALK_LEFT)

        # Pushing/Pulling the window.
        elif self.state == 1:
            direction = Vector2(0,0)
            if self.screen_dir == 0:
                direction.x = 1
            else:
                direction.x = -1

            direction = direction * OpenWindow.MOVEMENT_SPEED * delta_time
            pet.translate(direction.x,direction.y)
            self.target_window.pos = self.target_window.pos.__add__(direction)

            if self.screen_dir == 0:
                if pet.pos.x >= self.active_monitor.width/2:
                    pet.change_state(PetState.IDLE)
            else:
                if pet.pos.x <= self.active_monitor.width/2:
                    pet.change_state(PetState.IDLE)


    