import time
import random

from vector2 import Vector2
from system import System
from pet import PetState
from pet import PetAnimState
from pynput import mouse
from pynput.mouse import Button
from pynput.mouse import Listener

class Idle(System):
    CLICK_POS = None

    def on_click(x, y, button, pressed):
        if (button == Button.left and pressed):
            Idle.CLICK_POS = Vector2(x, y)
        return True

    def on_enter(self, pet):
        pet.set_anim_state(PetAnimState.IDLE)
        self.duration = random.randrange(10, 15)
        self.start = time.time()

        # Non-blocking mouse listener.
        self.listener = mouse.Listener(on_move=None, on_click=Idle.on_click, on_scroll=None)
        self.listener.start()

    def on_exit(self, pet):
        # Stop mouse listener.
        self.listener.stop()

    def action(self, pet, delta_time):
        # If clicked on, change to headpat state.
        if Idle.CLICK_POS is not None:
            minX = pet.get_position().x
            maxX = pet.get_position().x + pet.get_width()
            minY = pet.get_position().y
            maxY = pet.get_position().y + pet.get_height()
            if (minX < Idle.CLICK_POS.x and Idle.CLICK_POS.x < maxX) and (minY < Idle.CLICK_POS.y and Idle.CLICK_POS.y < maxY):
                pet.change_state(PetState.HEADPAT)
                Idle.CLICK_POS = None

        if (time.time() < self.start + self.duration):
            return

        # Else, 30% chance of catching mouse.
        if (random.randrange(0, 10) < 3):
            pet.change_state(PetState.CATCH_MOUSE)
        # Else, 10% chance of creating window.
        elif (random.randrange(0, 10) < 1):
            pet.change_state(PetState.CREATE_WINDOW)
        # Else, stroll.
        else:
            pet.change_state(PetState.STROLL)