from system import System
from pet import PetState
from pet import PetAnimState
from playsound import playsound

class Headpat(System):
    def on_enter(self, pet):
        print("On Enter Headpat")
        pet.set_anim_state(PetAnimState.HEADPAT)
        playsound("assets/sfx/cat_meow.mp3", block=False)

    def on_exit(self, pet):
        pass

    def action(self, pet, delta_time):
        pet.change_state(PetState.IDLE)