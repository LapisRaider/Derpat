import tkinter as tk
import time
import random

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
        self.x = 0
        self.y = 0

        # self.state = 

        # Placeholder image.
        self.img = tk.PhotoImage(file='images/placeholder.png')
        self.frame_index = 0
        self.num_frames = 1

        # Create a label as a container for our image.
        self.label = tk.Label(self.window, image=self.img, bd=0, bg='black').pack()

    def set_position(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

    def translate(self, x_offset, y_offset):
        self.x += x_offset
        self.y += y_offset

    def update(self):
        self.window.geometry('+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        self.window.update()