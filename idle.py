import time
import random

from system import System
from vector2 import Vector2
from pet import PetState

class Idle(System):
    IDLE_DURATION = 5

    def on_enter(self, pet):
        self.idle_start = time.time()

    def action(self, pet):
        pass