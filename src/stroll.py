import random
import monitor

from system import System
from vector2 import Vector2
from pet import PetState
from pet import PetAnimState
from read_parameters import state_param_dict

class Stroll(System):
    STROLL_SPEED = float(state_param_dict["STROLL_SPEED"])

    def on_enter(self, pet):
        print("On Enter Stroll")
        active_monitor = monitor.get_active_monitor(pet.get_position())
        minX = active_monitor.x
        maxX = active_monitor.x + active_monitor.width
        minY = active_monitor.y
        maxY = active_monitor.y + active_monitor.height
        self.target_pos = Vector2(random.randrange(minX, maxX), random.randrange(minY, maxY))

    def on_exit(self, pet):
        pass

    def action(self, pet, delta_time):
        dir = self.target_pos - pet.get_position()
        
        if (dir.x < 0 and pet.get_anim_state() != PetAnimState.WALK_LEFT):
            pet.set_anim_state(PetAnimState.WALK_LEFT)
        elif (dir.x >= 0 and pet.get_anim_state() != PetAnimState.WALK_RIGHT):
            pet.set_anim_state(PetAnimState.WALK_RIGHT)

        if (dir.length_squared() > 3):
            pet.translate_vec2(dir.normalised() * Stroll.STROLL_SPEED * delta_time)
        else:
            pet.change_state(PetState.IDLE)