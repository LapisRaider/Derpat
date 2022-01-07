import time
import random

from system import System
from vector2 import Vector2
from mouseController import *
from pet import PetState
from pet import PetAnimState

class SnatchMouse(System):
    MAX_SNATCH_TIME_AMT = 5 # in seconds
    MIN_SNATCH_TIME_AMT = 3

    RUN_SPEED = 1

    MOUSE_OFFSET_RUN_LEFT = Vector2(10, 70)
    MOUSE_OFFSET_RUN_RIGHT = Vector2(110, 70)

    #to be init at the start
    def on_enter(self, pet):
        pet.snatchStartTime = time.time()
        pet.snatchTimeAmt = random.randrange(SnatchMouse.MIN_SNATCH_TIME_AMT, SnatchMouse.MAX_SNATCH_TIME_AMT)
        self.runDir = Vector2(random.randrange(-1, 1), random.uniform(-1, 1))
        self.mouseOffset = SnatchMouse.MOUSE_OFFSET_RUN_LEFT if pet.anim_state == PetAnimState.WALK_LEFT else SnatchMouse.MOUSE_OFFSET_RUN_RIGHT

    # update snatching the mouse
    def action(self, pet):
        #let go of mouse after a while
        if (time.time() > pet.snatchStartTime + SnatchMouse.MAX_SNATCH_TIME_AMT):
            pet.next_state = PetState.IDLE
            return

        #TODO:: able to run in a random direction and change
        pet.translate(round(self.runDir.x) * SnatchMouse.RUN_SPEED, round(self.runDir.y) * SnatchMouse.RUN_SPEED)

        #check if run out of a certain amt out of screen, come back

        #update animation
        if (self.runDir.x < 0 and pet.get_anim_state() != PetAnimState.WALK_LEFT):
            pet.set_anim_state(PetAnimState.WALK_LEFT)
            self.mouseOffset = SnatchMouse.MOUSE_OFFSET_RUN_LEFT
        elif (self.runDir.x >= 0 and pet.get_anim_state() != PetAnimState.WALK_RIGHT):
            pet.set_anim_state(PetAnimState.WALK_RIGHT)
            self.mouseOffset = SnatchMouse.MOUSE_OFFSET_RUN_RIGHT

        newMousePos = self.mouseOffset.__add__(pet.pos)
        setMousePos(newMousePos.x, newMousePos.y) #mouse attached to pet

