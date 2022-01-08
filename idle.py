import time
import random

from vector2 import Vector2
from system import System
from pet import PetState
from pet import PetAnimState
from pynput import mouse
from pynput.mouse import Button

# Work around due to Python's shitty lambda functions.
class _OnClick():
    def __init__(self, idle_system):
        self.idle_system = idle_system

    def __call__(self, x, y, button, pressed):
        if (button == Button.left and pressed):
            self.idle_system.click_pos = Vector2(x, y)
        return True

class Idle(System):
    def on_enter(self, pet):
        pet.set_anim_state(PetAnimState.IDLE)
        self.duration = random.randrange(5, 10)
        self.start = time.time()

        # Non-blocking mouse listener.
        self.click_pos = None
        self.listener = mouse.Listener(on_move=None, on_click=_OnClick(self), on_scroll=None)
        self.listener.start()

    def on_exit(self, pet):
        # Stop mouse listener.
        self.listener.stop()
        self.listener = None

    def action(self, pet, delta_time):
        # If clicked on, change to headpat state.
        if self.click_pos is not None:
            minX = pet.get_position().x
            maxX = pet.get_position().x + pet.get_width()
            minY = pet.get_position().y
            maxY = pet.get_position().y + pet.get_height()
            if (minX < self.click_pos.x and self.click_pos.x < maxX) and (minY < self.click_pos.y and self.click_pos.y < maxY):
                pet.change_state(PetState.HEADPAT)
                self.click_pos = None

        if (time.time() < self.start + self.duration):
            return

        # Else, 30% chance of catching mouse.
        if (random.randrange(0, 10) < 3):
            pet.change_state(PetState.CATCH_MOUSE)
        # Else, 10% chance of creating window.
        elif (random.randrange(0, 10) < 2):
            pet.change_state(PetState.CREATE_WINDOW)
        # Else, 10% chance of dragging a window.
        elif (random.randrange(0, 10) < 2):
            pet.change_state(PetState.DRAG_WINDOW)
        # Else, 10% chance of screaming.
        elif (random.randrange(0, 10) < 1):
            pet.change_state(PetState.SCREAM)
        # Else, stroll.
        else:
            pet.change_state(PetState.STROLL)