import time
import tkinter as tk

class SpriteAnim():
    def __init__(self, gif, num_frames, delay=0.1, loop=True):
        self.frame_index = 0
        self.num_frames = num_frames
        self.anim_frames = [tk.PhotoImage(file=gif, format='gif -index %i' % (i)) for i in range(num_frames)]
        self.delay = delay
        self.last_update = time.time()
        self.loop = loop
        self.is_finished = False

    def update(self):
        if self.is_finished:
            return

        if (self.last_update + self.delay < time.time()):
            self.frame_index = self.frame_index + 1
            
            if not self.loop and self.frame_index == self.num_frames:
                self.is_finished = True
                return

            self.frame_index = self.frame_index%self.num_frames
            self.last_update = time.time()

    def finished(self):
        return self.is_finished

    def reset(self):
        self.frame_index = 0

    def get_frame(self):
        return self.anim_frames[self.frame_index]

    def get_delay(self):
        return self.delay