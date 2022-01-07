import time
import random

from system import System
from pet import PetState
from pet import PetAnimState

class Headpat(System):
    def on_enter(self, pet):
        pet.set_anim_state(PetAnimState.HEADPAT)
        self.duration = random.randrange(5, 10)
        self.start = time.time()
        self.listener = mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll)
            listener.start()

    def on_exit(self, pet):
        self.listener = None

    def action(self, pet):
        if (time.time() > self.start + self.duration):
            pet.change_state(PetState.IDLE)

        