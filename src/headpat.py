from system import System
from pet import PetState
from pet import PetAnimState
from playsound import playsound
from read_parameters import asset_param_dist

class Headpat(System):
    def on_enter(self, pet):
        print("On Enter Headpat")
        pet.set_anim_state(PetAnimState.HEADPAT)
        playsound(asset_param_dist["HEADPAT_SOUND"], block=False)

    def on_exit(self, pet):
        pass

    def action(self, pet, delta_time):
        pet.change_state(PetState.IDLE)