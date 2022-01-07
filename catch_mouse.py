import time
import random

from system import System
from mouseController import *
from pet import PetState
from pet import PetAnimState

class CatchMouse(System):
    FOLLOW_SPEED = 1
    MOUSE_CATCH_OFFSET = 5

    MAX_FOLLOW_TIME_AMT = 5 # after a certain amt of time give up
    MIN_FOLLOW_TIME_AMT = 3

    CATCH_OFFSET = Vector2(64,64)

    #to be init at the start
    def on_enter(self, pet):
        pet.followStartTime = time.time()
        pet.followAmt = random.randrange(CatchMouse.MIN_FOLLOW_TIME_AMT, CatchMouse.MAX_FOLLOW_TIME_AMT)

    #pet follows the mouse ard
    def follow_mouse(self, pet):
        mousePos = getMousePos()
        dir = mousePos.__sub__(pet.pos.__add__(CatchMouse.CATCH_OFFSET))
        dir = dir.normalised()
        pet.translate(round(dir.x) * CatchMouse.FOLLOW_SPEED, round(dir.y) * CatchMouse.FOLLOW_SPEED)

        if (dir.x < 0 and pet.get_anim_state() != PetAnimState.WALK_LEFT):
            pet.set_anim_state(PetAnimState.WALK_LEFT)
        elif (dir.x >= 0 and pet.get_anim_state() != PetAnimState.WALK_RIGHT):
            pet.set_anim_state(PetAnimState.WALK_RIGHT)

    #check if pet close enough to grab the mouse
    def check_get_mouse(self, pet):
        dir = getMousePos().__sub__(pet.pos.__add__(CatchMouse.CATCH_OFFSET))
        return dir.length() < CatchMouse.MOUSE_CATCH_OFFSET

    # update snatching the mouse
    def action(self, pet):
        #give up chasing
        if time.time() > pet.followStartTime + pet.followAmt:
            pet.next_state = PetState.IDLE
            return

        self.follow_mouse(pet) #follow the mouse

        #caught the mouse
        if self.check_get_mouse(pet):
            pet.next_state = PetState.GOT_MOUSE
