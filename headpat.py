import time

from system import System
from pet import PetState
from pet import PetAnimState

class Headpat(System):
    def on_enter(self, pet):
        pet.set_anim_state(PetAnimState.HEADPAT)

    def on_exit(self, pet):
        pass

    def action(self, pet):
        pet.change_state(PetState.IDLE)

        