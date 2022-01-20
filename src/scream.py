import time
import random

from system import System
from pet import PetState
from pet import PetAnimState
from playsound import playsound
from read_parameters import state_param_dict
from read_parameters import asset_param_dict

class Scream(System):
    SCREAM_MIN_TIME = float(state_param_dict["SCREAM_MIN_TIME"])
    SCREAM_MAX_TIME = float(state_param_dict["SCREAM_MAX_TIME"])
    SCREAM_INTERVAL = float(state_param_dict["SCREAM_INTERVAL"])
    AUDIO_FILE = asset_param_dict["SCREAM_SOUND"]

    def on_enter(self, pet):
        print("On Enter Scream")
        self.start_time = time.time()
        self.duration = random.randrange(Scream.SCREAM_MIN_TIME, Scream.SCREAM_MAX_TIME)
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
        
    