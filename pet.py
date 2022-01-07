import tkinter as tk
import time
import random
import enum

from vector2 import *
from sprite_anim import SpriteAnim
from footprints import Footprints

class PetState(enum.IntEnum):
    DEFAULT = 0
    IDLE = 1
    STROLL = 2
    CATCH_MOUSE = 3
    GOT_MOUSE = 4
    DRAG_WINDOW = 5
    CREATE_WINDOW = 6
    MAKE_NOTE = 7
    HEADPAT = 8
    SCREAM = 9

class PetAnimState(enum.IntEnum):
    IDLE = 0
    HEADPAT = 1
    WALK_LEFT = 2
    WALK_RIGHT = 3
    ATTACK_LEFT = 4
    ATTACK_RIGHT = 5

class Pet():
    FOOT_PRINT_SPAWN = 0.4
    FOOT_X_LEFT_OFFSET = 64
    FOOT_X_RIGHT_OFFSET = -5
    FOOT_Y_OFFSET = 80

    def __init__(self):
        # Create a window
        self.window = tk.Tk()
        # Make window draw over all others
        self.window.attributes('-topmost', True)
        # Make window borderless.
        self.window.overrideredirect(True)

        # WINDOWS ONLY
        # Set focushighlight to black when the window does not have focus.
        self.window.config(highlightbackground='black')
        # Turn black into transparency.
        self.window.wm_attributes('-transparentcolor', 'black')

        # X & Y Coordinates of our window.
        self.pos = Vector2(500, 0)

        #for tracking footprints
        self.footPrintsStorer = []
        self.footPrintTime = time.time()

        #set default state
        self.next_state = PetState.IDLE
        self.curr_state = PetState.DEFAULT
        self.prev_state = PetState.DEFAULT

        # Create animations.
        self.anims = [ \
            SpriteAnim('animations/derpat/idle.gif', 6),
            SpriteAnim('animations/derpat/headpat.gif', 6), \
            SpriteAnim('animations/derpat/walk_left.gif', 4), \
            SpriteAnim('animations/derpat/walk_right.gif', 4), \
            SpriteAnim('animations/derpat/attack_left.gif', 5), \
            SpriteAnim('animations/derpat/attack_right.gif', 5)]
        self.anim_state = PetAnimState.IDLE
        self.label = tk.Label(self.window, image=self.anims[self.anim_state].get_frame(), bd=0, bg='black')
        self.label.pack()

    def set_anim_state(self, anim_state):
        self.anims[self.anim_state].reset() # Reset previous animation.
        self.anim_state = anim_state # Switch to new animation.

    def get_anim_state(self):
        return self.anim_state

    def set_position(self, x_pos, y_pos):
        self.pos.x = x_pos
        self.pos.y = y_pos

    def set_position_vec2(self, pos):
        self.pos = pos

    def translate(self, x_offset, y_offset):
        self.pos.x += x_offset
        self.pos.y += y_offset

    def translate_vec2(self, offset):
        self.pos = self.pos + offset

    def get_position(self):
        return self.pos

    def update(self, delta_time):
        self.anims[self.anim_state].update()
        self.label.configure(image=self.anims[self.anim_state].get_frame()) # Update animation frame.

        # Update Window
        self.window.geometry('+{x}+{y}'.format(x=str(round(self.pos.x)), y=str(round(self.pos.y))))
        #self.window.lift()
        self.window.update()

        # Update Previous
        self.prev_state = self.curr_state
        self.curr_state = self.next_state

    def change_state(self, state):
        self.next_state = state

    def get_prev_state(self):
        return self.prev_state

    def get_curr_state(self):
        return self.curr_state

    def get_next_state(self):
        return self.next_state

    def get_width(self):
        return self.label.winfo_width()

    def get_height(self):
        return self.label.winfo_height()

    def track_footprints(self):
        deleteQueue = []

        #update and check those who are inactive
        for footprint in self.footPrintsStorer:
            if not footprint.active:
                deleteQueue.append(footprint)
                continue

            footprint.update()

        #remove inactive
        for footprint in deleteQueue:
            self.footPrintsStorer.remove(footprint)
            del footprint

        deleteQueue.clear()

        if self.anim_state == PetAnimState.IDLE:
            return

        #check to see if should spawn footprints
        if time.time() < self.footPrintTime + Pet.FOOT_PRINT_SPAWN:
            return
        self.footPrintTime = time.time()

        walkingLeft = self.anim_state == PetAnimState.WALK_LEFT
        footPrintOffset = Vector2(Pet.FOOT_X_LEFT_OFFSET, Pet.FOOT_Y_OFFSET) if self.anim_state == PetAnimState.WALK_LEFT else Vector2(Pet.FOOT_X_RIGHT_OFFSET, Pet.FOOT_Y_OFFSET)

        self.footPrintsStorer.append(Footprints(self.pos.__add__(footPrintOffset), walkingLeft))