from pet import Pet
from snatch_mouse import SnatchMouse
from catch_mouse import CatchMouse
from pet import PetState

import sys
print(sys.executable)

if __name__ == "__main__":
    # Pet
    pet = Pet()
    # Systems
    pet.curr_state = PetState.CATCH_MOUSE #temp for testing
    catch_mouse = CatchMouse(0, PetState.CATCH_MOUSE)

    while True:
        # System Update
        catch_mouse.update(pet)
        # Pet Update
        pet.update()