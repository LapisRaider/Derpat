import tkinter as tk
import random
import monitor
import os
import enum

from tkinter.constants import CURRENT
from system import System
from pet import PetAnimState, PetState
from vector2 import Vector2
from custom_windows import NoteWindow, ImageWindow
from enum import auto, IntEnum
from read_parameters import param_dict

class _PullDirection(IntEnum):
    LEFT_TO_RIGHT = auto()
    RIGHT_TO_LEFT = auto()

class _State(IntEnum):
    MOVE_TO_CORNER = auto()
    SPAWN_WINDOW = auto()
    MOVE_TO_CENTRE = auto()

class _SpawnType(IntEnum):
    NOTE = auto()
    IMAGE = auto()

class OpenWindow(System):
    MOVEMENT_SPEED = int(param_dict["OPEN_RUN_SPEED"])

    def __init__(self, delay=0, action_state=PetState.DEFAULT):
        super().__init__(delay=delay, action_state=action_state)
        self.windows = []

    def on_enter(self, pet):
        print("On Enter Open Window")

        # Get active monitor.
        self.active_monitor = monitor.get_active_monitor(Vector2(0,0))
        
        # Initialise state and direction.
        self.state = _State.MOVE_TO_CORNER
        self.pull_dir = random.choice([_PullDirection.LEFT_TO_RIGHT, _PullDirection.RIGHT_TO_LEFT])
        
        # Corner is where the dog runs to and where the window spawns.
        self.corner = Vector2(-100, random.randint(250, self.active_monitor.height - 250))
        if self.pull_dir == _PullDirection.LEFT_TO_RIGHT:
            pet.set_anim_state(PetAnimState.WALK_LEFT)
        else:
            pet.set_anim_state(PetAnimState.WALK_RIGHT)
            pet.window.update()
            self.corner.x = self.active_monitor.width + 100 - pet.window.winfo_width()

    def action(self,pet,delta_time):
        # Going towards the corner.
        if self.state == _State.MOVE_TO_CORNER:
            # Translate pet.
            direction = (self.corner - pet.pos)
            pet.translate_vec2(direction.normalised() * OpenWindow.MOVEMENT_SPEED * delta_time)

            # Has reached destination.
            if direction.length_squared() < 4:
                pet.pos = self.corner
                self.state = _State.SPAWN_WINDOW

        # Spawn the window.
        elif self.state == _State.SPAWN_WINDOW:
            self.spawn_type = random.choice([_SpawnType.IMAGE, _SpawnType.NOTE])

            # Spawn note.
            if self.spawn_type == _SpawnType.NOTE:
                self.target_window = NoteWindow(width=400, height=300)

            # Spawn image.
            else:
                file_paths = os.listdir('src/assets/images')
                randomPath = file_paths[random.randint(0, len(file_paths) - 1)]
                self.target_window = ImageWindow('src/assets/images/' + randomPath)

            # Lift the pet window to ensure that it is not covered by our newly spawned window.
            pet.lift_window()
            
            if self.pull_dir == _PullDirection.LEFT_TO_RIGHT:
                self.target_window.set_position_vec2(self.corner - Vector2(self.target_window.get_width(), 0))
                pet.set_anim_state(PetAnimState.WALK_RIGHT)
            else:
                self.target_window.set_position_vec2(self.corner + Vector2(pet.get_width(), 0))
                pet.set_anim_state(PetAnimState.WALK_LEFT)

            self.state = _State.MOVE_TO_CENTRE

        # Pushing/Pulling the window.
        elif self.state == _State.MOVE_TO_CENTRE:
            # Translate pet and window.
            direction = Vector2(1, 0) if self.pull_dir == _PullDirection.LEFT_TO_RIGHT else Vector2(-1, 0)
            direction = direction * OpenWindow.MOVEMENT_SPEED * delta_time
            pet.translate_vec2(direction)
            self.target_window.translate_vec2(direction)
            self.target_window.update()

            # Stop moving once the pet reaches the centre of the screen.
            if (self.pull_dir == _PullDirection.LEFT_TO_RIGHT and pet.pos.x > self.active_monitor.width * 0.5):
                pet.change_state(PetState.IDLE)
                self.windows.append(self.target_window)
            elif (self.pull_dir == _PullDirection.RIGHT_TO_LEFT and pet.pos.x < self.active_monitor.width * 0.5):
                pet.change_state(PetState.IDLE)
                self.windows.append(self.target_window)

    def always_action(self, pet, delta_time):
        # Destroy closed windows.
        for x in self.windows:
            if x.is_closed():
                x.window.destroy()
                self.windows.remove(x)