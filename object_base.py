import tkinter as tk

from sprite_anim import SpriteAnim

class ObjectBase():
    def __init__(self, gif, num_frames, delay=0.1):
        # Create a window
        self.window = tk.Toplevel()
        # Make window draw over all others
        self.window.attributes('-topmost', True)
        # Make window borderless.
        self.window.overrideredirect(True)

        # WINDOWS ONLY
        # Set focushighlight to black when the window does not have focus.
        self.window.config(highlightbackground='black')
        # Turn black into transparency.
        self.window.wm_attributes('-transparentcolor', 'black')

        # Create animations.
        self.anim = SpriteAnim(gif, num_frames, delay)
        self.label = tk.Label(self.window, image = self.anim.get_frame(), bd=0, bg='black')
        self.label.pack()

        self.active = False

    def update(self):
        pass
