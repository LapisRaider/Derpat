# Others
import time
import keyboard

# Pet
from monitor import init_monitors
from pet import Pet
from pet import PetState

# Systems
from idle import Idle
from stroll import Stroll
from headpat import Headpat
from got_mouse import GotMouse
from chase_mouse import ChaseMouse
from scream import Scream
from open_window import *
from move_window import *

def quit_combination():
    return keyboard.is_pressed("ctrl") and keyboard.is_pressed('alt') and keyboard.is_pressed('2') and keyboard.is_pressed('9') and keyboard.is_pressed('Y')

if __name__ == "__main__":
    monitor.init_monitors()

    # Pet
    pet = Pet()
    
    # Systems
    idle = Idle(0, PetState.IDLE)
    stroll = Stroll(0, PetState.STROLL)
    headpat = Headpat(6, PetState.HEADPAT)
    chase_mouse = ChaseMouse(0, PetState.CHASE_MOUSE)
    got_mouse = GotMouse(0, PetState.GOT_MOUSE)
    open_window = OpenWindow(0, PetState.OPEN_WINDOW)
    move_window = MoveWindow(0, PetState.MOVE_WINDOW)
    scream = Scream(0, PetState.SCREAM)
    
    # Main Loop
    prev_time = time.time()
    while True:
        # Calculate delta time.
        curr_time = time.time()
        delta_time = curr_time - prev_time
        prev_time = curr_time

        # System Update
        idle.update(pet, delta_time)
        stroll.update(pet, delta_time)
        headpat.update(pet, delta_time)
        chase_mouse.update(pet, delta_time)
        got_mouse.update(pet, delta_time)
        open_window.update(pet, delta_time)
        move_window.update(pet, delta_time)
        scream.update(pet, delta_time)

        # Pet Update
        pet.update(delta_time)
        pet.track_footprints()

        # Exit the application, can be changed.
        if quit_combination():
            break

        #if keyboard.is_pressed("1"):
        #    pet.change_state(PetState.IDLE)
        #elif keyboard.is_pressed("2"):
        #    pet.change_state(PetState.STROLL)
        #elif keyboard.is_pressed("3"):
        #    pet.change_state(PetState.CATCH_MOUSE)
        #elif keyboard.is_pressed("4"):
        #    pet.change_state(PetState.OPEN_WINDOW)
        #elif keyboard.is_pressed("5"):
        #    pet.change_state(PetState.MOVE_WINDOW)
        #elif keyboard.is_pressed("6"):
        #    pet.change_state(PetState.HEADPAT)
        #elif keyboard.is_pressed("7"):
        #    pet.change_state(PetState.SCREAM)