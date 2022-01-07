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

    SCREAM_INTERVALS = 1.5

    def on_enter(self, pet):
        pet.screamStartTime = time.time()
        pet.screamTime = random.randrange(Scream.MIN_SCREAM_TIME, Scream.MAX_SCREAM_TIME)
        
        pet.screamIntervalStart = time.time()
        
        pet.set_anim_state(random.randint(PetAnimState.ATTACK_LEFT, PetAnimState.ATTACK_RIGHT))
        playsound("sfx/cat_scream.wav", block=False)

    def action(self, pet, delta_time):
        #check when to stop screaming
        if time.time() > pet.screamStartTime + pet.screamTime:
            pet.change_state(PetState.IDLE)
            return
        
        #scream after a certain interval
        if time.time() > pet.screamIntervalStart + Scream.SCREAM_INTERVALS:
            playsound("sfx/cat_scream.wav", block=False)
            pet.screamIntervalStart = time.time()
        
    