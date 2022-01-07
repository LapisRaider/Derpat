from pet import Pet
from snatch_mouse import SnatchMouse
from catch_mouse import CatchMouse
from pet import PetState
from openWindow import *

import keyboard

if __name__ == "__main__":
    #List of windows for testing
    windows = []
    # Pet
    pet = Pet()
    # Systems
    pet.curr_state = PetState.CREATE_WINDOW #temp for testing
    catch_mouse = CatchMouse(0, PetState.CATCH_MOUSE)
    open_window = OpenWindow(0, PetState.CREATE_WINDOW,windows)
    pet.set_anim_state(PetAnimState.WALK_LEFT)
    while True:
        # System Update
        catch_mouse.update(pet)
        open_window.update(pet)
        # Pet Update
        pet.update()
        # Updating all windows
        for x in windows:
            if x.closing: # To prevent program from crashing when closed
                x.window.destroy()
                windows.remove(x)
            else:
                x.update()

        #exit the application, can be changed
        if keyboard.is_pressed("shift") and keyboard.is_pressed('a'):
            break

