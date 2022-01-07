import time
import random

from system import System
from vector2 import Vector2
from mouseController import *
from pet_states import PetState

class SnatchMouse(System):
    MAX_SNATCH_TIME_AMT = 5 # in seconds
    MIN_SNATCH_TIME_AMT = 2

    #to be init at the start
    def on_enter(self, pet):
        pet.snatchStartTime = time.time()
        pet.snatchTimeAmt = random.randrange(SnatchMouse.MIN_SNATCH_TIME_AMT, SnatchMouse.MAX_SNATCH_TIME_AMT)

    # update snatching the mouse
    def action(self, pet):
        self.take_mouse(pet)

    #behavior for taking the mouse and running away
    def take_mouse(self, pet):
        #let go of mouse after a while
        if (time.time() > pet.snatchStartTime + SnatchMouse.MAX_SNATCH_TIME_AMT):
            return False

        #set random directions
        setMousePos(pet.pos.x, pet.pos.y) #mouse attached to pet
        #pet.state = PetState.IDLE #TODO:: TEMP CODE REMOVE THIS

        return True
