import time
import random
import enum

from vector2 import Vector2
from system import System
from pet import PetState
from pet import PetAnimState
from pynput import mouse
from pynput.mouse import Button
from read_parameters import param_dict

class ChanceState(enum.IntEnum):
    CHANCE_CHASE_MOUSE = 0
    CHANCE_OPEN_WINDOW = 1
    CHANCE_MOVE_WINDOW = 2
    CHANCE_SCREAM = 3
    CHANCE_STROLL = 4

# Work around due to Python's shitty lambda functions.
class _OnClick():
    def __init__(self, idle_system):
        self.idle_system = idle_system

    def __call__(self, x, y, button, pressed):
        if (button == Button.left and pressed):
            self.idle_system.click_pos = Vector2(x, y)
        return True

class Idle(System):
    MIN_DURATION_IDLE = float(param_dict["MIN_DURATION_IDLE"])
    MAX_DURATION_IDLE = float(param_dict["MAX_DURATION_IDLE"])

    CHANCES = [float(param_dict["CHANCE_CHASE_MOUSE"]), \
        float(param_dict["CHANCE_OPEN_WINDOW"]), \
        float(param_dict["CHANCE_MOVE_WINDOW"]),  \
        float(param_dict["CHANCE_SCREAM"]), \
        float(param_dict["CHANCE_STROLL"])
        ]
    TOTAL_CHANCE = 0

    def on_enter(self, pet):
        print("On Enter Idle")
        pet.set_anim_state(PetAnimState.IDLE)
        self.duration = random.randrange(Idle.MIN_DURATION_IDLE, Idle.MAX_DURATION_IDLE)
        self.start = time.time()

        # Non-blocking mouse listener.
        self.click_pos = None
        self.listener = mouse.Listener(on_move=None, on_click=_OnClick(self), on_scroll=None)
        self.listener.start()

        for chance in Idle.CHANCES:
            Idle.TOTAL_CHANCE += chance

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

        currChance = 0
        randomChance = random.randrange(0, Idle.TOTAL_CHANCE)
        for i in range(len(Idle.CHANCES)):
            currChance += Idle.CHANCES[i]
            if randomChance >= currChance:
                continue

            if i == ChanceState.CHANCE_CHASE_MOUSE:
                pet.change_state(PetState.CHASE_MOUSE)
            elif i == ChanceState.CHANCE_OPEN_WINDOW:
                pet.change_state(PetState.OPEN_WINDOW)
            elif i == ChanceState.CHANCE_MOVE_WINDOW:
                pet.change_state(PetState.MOVE_WINDOW)
            elif i == ChanceState.CHANCE_SCREAM:
                pet.change_state(PetState.SCREAM)
            else:
                pet.change_state(PetState.STROLL)

            break