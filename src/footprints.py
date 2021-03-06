import time

from object_base import ObjectBase
from read_parameters import asset_param_dict

class Footprints(ObjectBase):
    NUM_FRAMES = int(asset_param_dict["FOOTPRINT_NUM_FRAME"])
    ANIM_DELAY = float(asset_param_dict["FOOTPRINT_ANIM_DELAY"])
    STAY_TIME = float(asset_param_dict["FOOTPRINT_STAY_TIME"])

    FOOTPRINTS_LEFT = asset_param_dict["FOOTPRINTS_LEFT"]
    FOOTPRINTS_RIGHT = asset_param_dict["FOOTPRINTS_RIGHT"]

    def __init__(self, pos, move_left = True):
        file_path = Footprints.FOOTPRINTS_LEFT if move_left else Footprints.FOOTPRINTS_RIGHT
        super(Footprints, self).__init__(file_path, Footprints.NUM_FRAMES, Footprints.ANIM_DELAY, False)
        self.active = True
        self.stay_time = 0
        self.window.geometry('+%d+%d' % (round(pos.x), round(pos.y)))

    def update(self):
        if time.time() < self.stay_time + Footprints.STAY_TIME:
            return

        self.anim.update()
        if self.anim.frame_index == 1:
            self.stay_time = time.time()

        if self.anim.finished():
            self.window.destroy()
            self.active = False
        else:
            self.label.configure(image=self.anim.get_frame())

    def is_active(self):
        return self.active