import time
import random

from system import System
from vector2 import Vector2
from mouseController import *
from pet_states import PetState

class SnatchMouse(System):
    MAX_SNATCH_TIME_AMT = 5 # in seconds
    MIN_SNATCH_TIME_AMT = 2

    RUN_SPEED = 5

    #to be init at the start
    def on_enter(self, pet):
        pet.snatchStartTime = time.time()
        pet.snatchTimeAmt = random.randrange(SnatchMouse.MIN_SNATCH_TIME_AMT, SnatchMouse.MAX_SNATCH_TIME_AMT)
        self.runDir = Vector2(random.randrange(-1, 1), random.uniform(-1, 1))

    # update snatching the mouse
    def action(self, pet):
        #let go of mouse after a while
        if (time.time() > pet.snatchStartTime + SnatchMouse.MAX_SNATCH_TIME_AMT):
            pet.curr_state = PetState.IDLE
            return

        #TODO:: able to run in a random direction and change
        pet.translate(round(self.runDir.x) * SnatchMouse.RUN_SPEED, round(self.runDir.y) * SnatchMouse.RUN_SPEED)

        #check if run out of a certain amt out of screen, come back


        setMousePos(pet.pos.x, pet.pos.y) #mouse attached to pet

