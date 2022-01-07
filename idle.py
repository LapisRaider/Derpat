import time
import random

from system import System
from pet import PetState

class Idle(System):
    def on_enter(self, pet):
        pet.set_anim_state(PetAnimState.IDLE)
        self.duration = randrange(15, 30)
        self.start = time.time()

    def action(self, pet):
        if (time.time() < self.start + self.duration):
            return

        # 30% chance of strolling.
        if (randrange(0, 10) < 3):
            pet.change_state(PetState.STROLL)

        # 20% chance of catching mouse.
        if (randrange(0, 10) < 2):
            pet.change_state(PetState.CATCH_MOUSE)

        # 20% chance of catching mouse.
        if (randrange(0, 10) < 2):
            pet.change_state(PetState.CREATE_WINDOW)