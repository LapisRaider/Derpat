import time

from pet import PetState

class System():
    def __init__(self, delay=0, action_state = PetState.DEFAULT):
        self.last_update = time.time()
        self.delay = delay
        self.action_state = action_state

    def update(self, pet, delta_time):
        # If there was a state change, check if we entered or exited this system.
        if (pet.get_curr_state() != pet.get_prev_state()):
            if (self.action_state == pet.get_curr_state()):
                self.on_enter(pet)
            elif (self.action_state == pet.get_prev_state()):
                self.on_exit(pet)

        # self.always_action(self, pet, delta_time)

        # Check if we should run this system.
        if (pet.get_curr_state() == self.action_state) and (time.time() > self.last_update + self.delay):
            self.action(pet, delta_time)
            self.last_update = time.time()

    def on_enter(self, pet):
        pass

    def on_exit(self, pet):
        pass

    def action(self, pet, delta_time):
        pass

    def always_action(self, pet, delta_time):
        pass