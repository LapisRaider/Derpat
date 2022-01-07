import tkinter as tk

from window_objects import WindowObjects

class Footprints(WindowObjects):
    NUM_FRAMES = 4
    ANIM_DELAY = 0.5

    def __init__(self):
        super(Footprints, self).__init__('animations/footprints.gif', Footprints.NUM_FRAMES, Footprints.ANIM_DELAY)

    def update(self):
        if not self.active:
            return

        if self.anim.frame_index == Footprints.NUM_FRAMES - 1:
            self.active = False #stop the thing
            return

        self.anim.update()

        self.label.configure(image=self.anim.get_frame())
        self.window.update()

    #to start showing the footprints
    def startObj(self, pos):
        self.active = True
        self.anim.reset()
        self.window.geometry('+{x}+{y}'.format(x=str(pos.x), y=str(pos.y)))


        