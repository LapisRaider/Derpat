import tkinter as tk

from object_base import ObjectBase

class Footprints(ObjectBase):
    NUM_FRAMES = 4
    ANIM_DELAY = 0.5

    def __init__(self, pos):
        super(Footprints, self).__init__('animations/footprintsLeft.gif', Footprints.NUM_FRAMES, Footprints.ANIM_DELAY)
        self.active = True

        self.window.geometry('+{x}+{y}'.format(x=str(round(pos.x)), y=str((round(pos.y)))))

    def update(self):
        if self.anim.frame_index == Footprints.NUM_FRAMES - 1:
            self.window.destroy
            self.active = False
            return

        self.anim.update()
        self.label.configure(image=self.anim.get_frame())



        