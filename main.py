# Pet
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
    # Pet
    pet = Pet()
    # Systems
    idle = Idle(0, PetState.IDLE)
    stroll = Stroll(0, PetState.STROLL)
    headpat = Headpat(6, PetState.HEADPAT)
    catch_mouse = CatchMouse(0, PetState.CATCH_MOUSE)
    open_window = OpenWindow(0, PetState.CREATE_WINDOW, windows)
    move_window = MoveWindow(0,PetState.DRAG_WINDOW)
    # notepad = Notepad(width=400, height=200)
    pet.change_state(PetState.DRAG_WINDOW)
    
    # Main Loop
    while True:
        # System Update
        idle.update(pet)
        stroll.update(pet)
        headpat.update(pet)
        catch_mouse.update(pet)
        open_window.update(pet)
        move_window.update(pet)

        # Pet Update
        pet.update()

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