import tkinter as tk
import time
import random

from vector2 import Vector2
from petStates import PetState

class pet():
    def __init__(self):
        # Create a window
        self.window = tk.Tk()
        # Make window draw over all others
        self.window.attributes('-topmost', True)
        # Make window frameless.
        # self.window.overrideredirect(True)

        # Timestamp to check whether to advance frame.
        self.timestamp = time.time()

        # X & Y Coordinates of our window.
        self.pos = Vector2(0, 0)

        #set default state
        self.state = PetState.IDLE

        # Placeholder image.
        self.img = tk.PhotoImage(file='images/placeholder.png')
        self.frame_index = 0
        self.num_frames = 1

        # Create a label as a container for our image.
        self.label = tk.Label(self.window, image=self.img).pack()

        # Run self.update() after 0ms when mainloop starts.
        self.window.after(0, self.update)

    def set_position(self, x_pos, y_pos):
        self.pos.x = x_pos
        self.pos.y = y_pos

    def translate(self, x_offset, y_offset):
        self.pos.x += x_offset
        self.pos.y += y_offset

    def update(self):
        # Update if 50ms have passed.
        if time.time() < self.timestamp + 0.05:
            return
        self.timestamp = time.time()

        # Update goes here.

    def updateRender(self):
        self.window.geometry('+{x}+{y}'.format(x=str(self.pos.x), y=str(self.pos.y)))
        self.window.update()
        