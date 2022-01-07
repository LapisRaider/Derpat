import time
import random
import monitor

from system import System
from vector2 import Vector2
from pet import PetState
from pet import PetAnimState

class Stroll(System):
    STROLL_SPEED = 1

    def on_enter(self, pet):
        active_monitor = monitor.getMonitorOnScrPos(pet.get_position())
        minX = active_monitor.x
        maxX = active_monitor.x + active_monitor.width
        minY = active_monitor.y
        maxY = active_monitor.y + active_monitor.height
        self.target_pos = Vector2(random.randrange(minX, maxY), random.randrange(minY, maxY))

    def action(self, pet):
        dir = self.target_pos - pet.get_position()
        if (dir.x < 0 and pet.get_anim_state() != PetAnimState.WALK_LEFT):
            pet.set_anim_state(PetAnimState.WALK_LEFT)

        if (dir.x >= 0 and pet.get_anim_state() != PetAnimState.WALK_RIGHT):
            pet.set_anim_state(PetAnimState.WALK_RIGHT)

        if (dir.length_squared() > 5):
            pet.translate_vec2(dir.normalised() * Stroll.STROLL_SPEED)
        else:
            pet.change_state(PetState.IDLE)