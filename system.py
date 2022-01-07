import time
from pet import PetState

class System():
    def __init__(self, delay=0, action_state = PetState.DEFAULT):
        self.last_update = time.time()
        self.delay = delay
        self.action_state = action_state

    def update(self, pet):
        # If there was a state change, check if we entered or exited this system.
        if (pet.curr_state != pet.prev_state):
            if (self.action_state == pet.curr_state):
                self.on_enter(pet)
            elif (self.action_state == pet.prev_state):
                self.on_exit(pet)

        # Check if we should run this system.
        if (pet.curr_state == self.action_state) and (time.time() > self.last_update + self.delay):
            self.action(pet)
            self.last_update = time.time()

        # Update previous state.
        pet.prev_state = pet.curr_state

    def on_enter(self, pet):
        pass

    def on_exit(self, pet):
        pass

    def action(self, pet):
        pass

