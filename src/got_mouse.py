import time
import random
import monitor

from system import System
from vector2 import Vector2
from mouse_controller import *
from pet import PetState
from pet import PetAnimState
from read_parameters import state_param_dict

class GotMouse(System):
    GOT_MIN_DURATION = float(state_param_dict["GOT_MIN_DURATION"]) # In seconds.
    GOT_MAX_DURATION = float(state_param_dict["GOT_MAX_DURATION"])
    GOT_RUN_SPEED = float(state_param_dict["GOT_RUN_SPEED"])
    MOUSE_OFFSET_RUN_LEFT = Vector2(float(state_param_dict["MOUSE_OFFSET_RUN_LEFT_X"]), float(state_param_dict["MOUSE_OFFSET_RUN_LEFT_Y"]))
    MOUSE_OFFSET_RUN_RIGHT = Vector2(float(state_param_dict["MOUSE_OFFSET_RUN_RIGHT_X"]), float(state_param_dict["MOUSE_OFFSET_RUN_RIGHT_Y"]))

    # to be init at the start
    def on_enter(self, pet):
        print("On Enter Got Mouse")
        self.start_time = time.time()
        self.duration = random.randrange(GotMouse.GOT_MIN_DURATION, GotMouse.GOT_MAX_DURATION)
        self.mouse_offset = GotMouse.MOUSE_OFFSET_RUN_LEFT if pet.anim_state == PetAnimState.WALK_LEFT else GotMouse.MOUSE_OFFSET_RUN_RIGHT
        self.randomise_dir(pet)

    # update snatching the mouse
    def action(self, pet, delta_time):
        #let go of mouse after a while
        if (time.time() > self.start_time + self.duration):
            pet.change_state(PetState.IDLE)
            return

        # check if out of screen and change direction
        if monitor.outside_bounds_x(pet.pos) or monitor.outside_bounds_y(pet.pos):
            self.randomise_dir(pet)

        pet.translate(round(self.run_dir.x) * GotMouse.GOT_RUN_SPEED * delta_time, round(self.run_dir.y) * GotMouse.GOT_RUN_SPEED * delta_time)

        # update animation
        if (self.run_dir.x < 0 and pet.get_anim_state() != PetAnimState.WALK_LEFT):
            pet.set_anim_state(PetAnimState.WALK_LEFT)
            self.mouse_offset = GotMouse.MOUSE_OFFSET_RUN_LEFT
        elif (self.run_dir.x >= 0 and pet.get_anim_state() != PetAnimState.WALK_RIGHT):
            pet.set_anim_state(PetAnimState.WALK_RIGHT)
            self.mouse_offset = GotMouse.MOUSE_OFFSET_RUN_RIGHT

        # update mouse pos
        newMousePos = self.mouse_offset.__add__(pet.pos)
        set_mouse_pos(newMousePos.x, newMousePos.y) # mouse attached to pet

    def randomise_dir(self, pet):
        active_monitor = monitor.get_active_monitor(pet.get_position())
        min_size = Vector2(active_monitor.x, active_monitor.y)
        max_size = Vector2(active_monitor.x + active_monitor.width, active_monitor.y + active_monitor.height)
        next_random_pos = Vector2(random.randrange(min_size.x, max_size.x), random.randrange(min_size.y, max_size.y))
        self.run_dir =(next_random_pos.__sub__(pet.pos)).normalised()

