import time

from object_base import ObjectBase

class Footprints(ObjectBase):
    NUM_FRAMES = 4
    ANIM_DELAY = 0.5
    STAY_TIME = 1

    FOOTPRINTS_LEFT = "assets/animations/footprints_Left.gif"
    FOOTPRINTS_RIGHT = "assets/animations/footprints_right.gif"

    def __init__(self, pos, move_left = True):
        file_path = Footprints.FOOTPRINTS_LEFT if move_left else Footprints.FOOTPRINTS_RIGHT
        super(Footprints, self).__init__(file_path, Footprints.NUM_FRAMES, Footprints.ANIM_DELAY, False)
        self.active = True
        self.stayTime = 0
        self.window.geometry('+{x}+{y}'.format(x=str(round(pos.x)), y=str((round(pos.y)))))

    def update(self):
        if time.time() < self.stayTime + Footprints.STAY_TIME:
            return

        self.anim.update()
        if self.anim.frame_index == 1:
            self.stayTime = time.time()

        if not self.anim.finished():
            self.label.configure(image=self.anim.get_frame())
        else:
            self.window.destroy
            self.active = False