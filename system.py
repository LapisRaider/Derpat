import time
from petStates import PetState

class System():
    def __init__(self, delay=0, state = PetState.IDLE):
        self.last_update = time.time()
        self.delay = delay
        self.state = state

    def update(self, pet):
        if (time.time() > self.last_update + self.delay) and (pet.state == self.state):
            self.action(pet)

    def action(self, pet):
        pass