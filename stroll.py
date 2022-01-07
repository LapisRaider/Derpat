import time
import random

from system import System
from vector2 import Vector2
from pet import PetState

class Stroll(System):
    STROLL_SPEED = 1

    def on_enter(self, pet):
        monitor = getMonitorOnScrPos(pet.get_position())
        minX = monitor.x; maxX = monitor.x + monitor.width
        minY = monitor.y; maxY = monitor.y + monitor.height
        self.target_pos = Vector2(randrange(minX, maxX), randrange(minY, maxY))

    def action(self, pet):
        dir = target_pos - pet.get_position()
        if (dir.x < 0 and pet.get_anim_state() != PetAnimState.WALK_LEFT):
            pet.set_anim_state(PetAnimState.WALK_LEFT)

        if (dir.x >= 0 and pet.get_anim_state() != PetAnimState.WALK_RIGHT):
            pet.set_anim_state(PetAnimState.WALK_RIGHT)

        if (dir.length_square() > 5):
            pet.translate(dir.normalised() * Stroll.STROLL_SPEED)
        else:
            pet.change_state(PetState.IDLE)