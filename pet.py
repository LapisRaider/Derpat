import tkinter as tk
import time
import random

from pet_states import PetState
from vector2 import *

class Pet():
    def __init__(self):
        # Create a window
        self.window = tk.Tk()
        # Make window draw over all others
        self.window.attributes('-topmost', True)
        # Make window borderless.
        self.window.overrideredirect(True)

        # WINDOWS ONLY
        # Set focushighlight to black when the window does not have focus.
        self.window.config(highlightbackground='black')
        # Turn black into transparency.
        self.window.wm_attributes('-transparentcolor', 'black')

        # X & Y Coordinates of our window.
        self.pos = Vector2(0, 0)

        #set default state
        self.curr_state = PetState.IDLE
        self.prev_state = PetState.DEFAULT

        #variables for snatching the mouse
        self.snatchStartTime = 0

        # Placeholder image.
        self.img = tk.PhotoImage(file='images/placeholder.png')
        self.frame_index = 0
        self.num_frames = 1

        # Create a label as a container for our image.
        self.label = tk.Label(self.window, image=self.img, bd=0, bg='black').pack()

    def set_position(self, x_pos, y_pos):
        self.pos.x = x_pos
        self.pos.y = y_pos

    def translate(self, x_offset, y_offset):
        self.pos.x += x_offset
        self.pos.y += y_offset

    def update(self):
        self.window.geometry('+{x}+{y}'.format(x=str(self.pos.x), y=str(self.pos.y)))
        self.window.update()

    def change_state(self, state):
        self.prev_state = self.curr_state
        self.curr_state = state
