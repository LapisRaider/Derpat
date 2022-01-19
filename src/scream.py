import time
import random

from system import System
from pet import PetState
from pet import PetAnimState
from playsound import playsound

class Scream(System):
    MIN_DURATION = 2
    MAX_DURATION = 5
    SCREAM_INTERVAL = 1.5
    AUDIO_FILE = "src/assets/sfx/cat_scream.wav"

    def on_enter(self, pet):
        print("On Enter Scream")
        self.start_time = time.time()
        self.duration = random.randrange(Scream.MIN_DURATION, Scream.MAX_DURATION)
        self.interval_start = time.time()
        pet.set_anim_state(random.randint(PetAnimState.ATTACK_LEFT, PetAnimState.ATTACK_RIGHT))
        playsound(Scream.AUDIO_FILE, block=False)

    def action(self, pet, delta_time):
        # Check when to stop screaming.
        if time.time() > self.start_time + self.duration:
            pet.change_state(PetState.IDLE)
            return
        
        # Scream after a certain time interval.
        if time.time() > self.interval_start + Scream.SCREAM_INTERVAL:
            playsound(Scream.AUDIO_FILE, block=False)
            self.interval_start = time.time()
        
    