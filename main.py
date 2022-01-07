# Pet
from monitor import initMonitors
from pet import Pet
from pet import PetState

# Systems
from idle import Idle
from stroll import Stroll
from headpat import Headpat
from snatch_mouse import SnatchMouse
from catch_mouse import CatchMouse

# Others
from openWindow import *
from moveWindow import *
# from makeNotes import *
import keyboard

if __name__ == "__main__":
    #List of windows for testing
    windows = []

    monitor.initMonitors()

    # Pet
    pet = Pet()
    # Systems
    idle = Idle(0, PetState.IDLE)
    stroll = Stroll(0, PetState.STROLL)
    headpat = Headpat(6, PetState.HEADPAT)
    catch_mouse = CatchMouse(0, PetState.CATCH_MOUSE)
    snatch_mouse = SnatchMouse(0, PetState.GOT_MOUSE)
    open_window = OpenWindow(0, PetState.CREATE_WINDOW, windows)
    move_window = MoveWindow(0,PetState.DRAG_WINDOW)
    # notepad = Notepad(width=400, height=200)
    pet.change_state(PetState.CREATE_WINDOW)
    
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
        catch_mouse.update(pet, delta_time)
        snatch_mouse.update(pet, delta_time)
        open_window.update(pet, delta_time)
        move_window.update(pet, delta_time)

        # Pet Update
        pet.update(delta_time)
        pet.track_footprints()

        # Updating all windows
        for x in windows:
            if x.closing: # To prevent program from crashing when closed.
                x.window.destroy()
                windows.remove(x)
            else:
                x.update()

        # Exit the application, can be changed.
        if keyboard.is_pressed("shift") and keyboard.is_pressed('a'):
            break