import time

from object_base import ObjectBase

class Footprints(ObjectBase):
    NUM_FRAMES = 4
    ANIM_DELAY = 0.5
    STAY_TIME = 1

    def __init__(self, pos, moveLeft = True):
        FOOTPRINTS_LEFT = "src/assets/animations/footprintsLeft.gif"
        FOOTPRINTS_RIGHT = "src/assets/animations/footprintsRight.gif"

        filePath = FOOTPRINTS_LEFT if moveLeft else FOOTPRINTS_RIGHT

        super(Footprints, self).__init__(filePath, Footprints.NUM_FRAMES, Footprints.ANIM_DELAY, False)
        self.active = True
        self.stayTime = 0

        self.window.geometry('+{x}+{y}'.format(x=str(round(pos.x)), y=str((round(pos.y)))))

    def update(self):
        if time.time() < self.stayTime + Footprints.STAY_TIME:
            return

        self.anim.update()

        if self.anim.frame_index == 1:
            self.stayTime = time.time()

        if not self.anim.is_finished:
            self.label.configure(image=self.anim.get_frame())
        else:
            self.window.destroy
            self.active = False
            return

        