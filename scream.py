from time import time
import time
import random

from system import System
from pet import PetState
from pet import PetAnimState

from playsound import playsound

class Scream(System):
    MAX_SCREAM_TIME = 5
    MIN_SCREAM_TIME = 2

    def on_enter(self, pet):
        pet.screamStartTime = time.time()
        pet.screamTime = random.randrange(Scream.MIN_SCREAM_TIME, Scream.MAX_SCREAM_TIME)
        pet.set_anim_state(PetAnimState.HEADPAT)

    def action(self, pet):
        #check when to stop screaming
        if time.time() > pet.screamStartTime + pet.screamTime:
            pet.change_state(PetState.IDLE)
            return

        #scream
        #playsound("sfx/cat_meow.mp3", block=False)
    