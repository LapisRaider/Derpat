from pet import Pet
from snatch_mouse import SnatchMouse

import sys
print(sys.executable)

if __name__ == "__main__":
    # Pet
    pet = Pet()
    # Systems
    snatch_mouse = SnatchMouse()

    while True:
        # System Update
        snatch_mouse.action(pet)
        # Pet Update
        pet.update()