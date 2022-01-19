import time
import random

from system import System
from mouse_controller import *
from pet import PetState
from pet import PetAnimState
from read_parameters import param_dict

class ChaseMouse(System):
    CHASE_FOLLOW_SPEED = float(param_dict["CHASE_FOLLOW_SPEED"])
    MOUSE_CATCH_DIST = float(param_dict["MOUSE_CATCH_DIST"])

    CHASE_MAX_TIME = float(param_dict["CHASE_MAX_TIME"]) # after a certain amt of time give up
    CHASE_MIN_TIME = float(param_dict["CHASE_MIN_TIME"])

    CATCH_OFFSET = Vector2(float(param_dict["CATCH_OFFSET_X"]),float(param_dict["CATCH_OFFSET_Y"]))

    #to be init at the start
    def on_enter(self, pet):
        pet.followStartTime = time.time()
        pet.followAmt = random.randrange(ChaseMouse.CHASE_MIN_TIME, ChaseMouse.CHASE_MAX_TIME)

    #pet follows the mouse ard
    def follow_mouse(self, pet, delta_time):
        mousePos = get_mouse_pos()
        dir = mousePos.__sub__(pet.pos.__add__(ChaseMouse.CATCH_OFFSET))
        dir = dir.normalised()
        pet.translate(round(dir.x) * ChaseMouse.CHASE_FOLLOW_SPEED * delta_time, round(dir.y) * ChaseMouse.CHASE_FOLLOW_SPEED * delta_time)

        if (dir.x < 0 and pet.get_anim_state() != PetAnimState.WALK_LEFT):
            pet.set_anim_state(PetAnimState.WALK_LEFT)
        elif (dir.x >= 0 and pet.get_anim_state() != PetAnimState.WALK_RIGHT):
            pet.set_anim_state(PetAnimState.WALK_RIGHT)

    #check if pet close enough to grab the mouse
    def check_get_mouse(self, pet):
        dir = get_mouse_pos().__sub__(pet.pos.__add__(ChaseMouse.CATCH_OFFSET))
        return dir.length() < ChaseMouse.MOUSE_CATCH_DIST

    # update snatching the mouse
    def action(self, pet, delta_time):
        #give up chasing
        if time.time() > pet.followStartTime + pet.followAmt:
            pet.change_state(PetState.IDLE)
            return

        self.follow_mouse(pet, delta_time) #follow the mouse

        #caught the mouse
        if self.check_get_mouse(pet):
            pet.change_state(PetState.GOT_MOUSE)
