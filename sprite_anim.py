import tkinter as tk

class SpriteAnim():
    def __init__(self, gif, num_frames, delay=10):
        self.num_frames = num_frames
        self.frame_index = 0
        self.anim_frames = [tk.PhotoImage(file=gif, format='gif -index %i' % (i)) for i in range(num_frames)]
        self.curr_frame = anim_frames[0]
        self.delay = delay
        self.last_update = time.time()

    def update():
        if (self.last_update + delay < time.time()):
            self.frame_index = (self.frame_index + 1)%self.num_frames
            self.curr_frame = anim_frames[frame_index]
            self.last_update = time.time()

    def reset():
        self.frame_index = 0
        self.curr_frame = anim_frames[0]