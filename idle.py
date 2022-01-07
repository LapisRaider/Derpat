import time
import random

from system import System
from pet import PetState
from pet import PetAnimState

class Idle(System):
    def on_enter(self, pet):
        pet.set_anim_state(PetAnimState.IDLE)
        self.duration = random.randrange(5, 10)
        self.start = time.time()

    def on_exit(self, pet):
        pass

    def action(self, pet):
        if (time.time() < self.start + self.duration):
            return

        # 30% chance of strolling.
        if (random.randrange(0, 10) < 9):
            pet.change_state(PetState.STROLL)

        # 20% chance of catching mouse.
        elif (random.randrange(0, 10) < 9):
            pet.change_state(PetState.CATCH_MOUSE)

        # 20% chance of creating window.
        elif (random.randrange(0, 10) < 9):
            pet.change_state(PetState.CREATE_WINDOW)