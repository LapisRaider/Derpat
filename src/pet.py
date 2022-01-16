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
    MOVE_WINDOW = 5
    OPEN_WINDOW = 6
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
    FOOT_PRINT_SPAWN_INTERVAL = 0.4
    FOOT_X_LEFT_OFFSET = 64
    FOOT_X_RIGHT_OFFSET = -5
    FOOT_Y_OFFSET = 80

    TRACK_FOOTPRINT_MAX_DURATION = 8
    TRACK_FOOTPRINT_MIN_DURATION = 5
    FOOTPRINT_CHANCE = 40 # 40%

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

        # For tracking footprints.
        self.active_footprints = []
        self.track_foot_print = False

        # Set default state.
        self.next_state = PetState.IDLE
        self.curr_state = PetState.DEFAULT
        self.prev_state = PetState.DEFAULT

        # Create animations.
        self.anims = [ \
            SpriteAnim('assets/animations/derpat/idle.gif', 6),
            SpriteAnim('assets/animations/derpat/headpat.gif', 6), \
            SpriteAnim('assets/animations/derpat/walk_left.gif', 4), \
            SpriteAnim('assets/animations/derpat/walk_right.gif', 4), \
            SpriteAnim('assets/animations/derpat/attack_left.gif', 5), \
            SpriteAnim('assets/animations/derpat/attack_right.gif', 5)]
        self.anim_state = PetAnimState.IDLE
        self.label = tk.Label(self.window, image=self.anims[self.anim_state].get_frame(), bd=0, bg='black')
        self.label.pack()

    def set_anim_state(self, anim_state):
        self.anims[self.anim_state].reset() # Reset previous animation.
        self.anim_state = anim_state # Switch to new animation.

        # Spawn footprints.
        if self.anim_state == PetAnimState.WALK_LEFT or self.anim_state == PetAnimState.WALK_RIGHT:
            if random.randrange(0, 100) < Pet.FOOTPRINT_CHANCE and not self.track_foot_print:
                self.track_foot_print = True
                self.init_track_footprints()
        else:
            self.track_foot_print = False

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
        # Update animation.
        self.anims[self.anim_state].update()
        self.label.configure(image=self.anims[self.anim_state].get_frame()) # Update animation frame.

        # Update window.
        self.window.geometry('+%d+%d' % (round(self.pos.x), round(self.pos.y)))
        self.window.update()

        # Update state.
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
        return self.window.winfo_width()

    def get_height(self):
        return self.window.winfo_height()

    def lift_window(self):
        self.window.lift()

    def init_track_footprints(self):
        self.footprint_end_time = time.time() + random.randrange(Pet.TRACK_FOOTPRINT_MIN_DURATION, Pet.TRACK_FOOTPRINT_MAX_DURATION)
        self.footprint_prev_spawn_time = 0
        
    def track_footprints(self):
        # Update and check those who are inactive.
        inactive_footprints = []
        for footprint in self.active_footprints:
            if footprint.is_active():
                footprint.update()
            else:
                inactive_footprints.append(footprint)

        # Remove inactive footprints.
        for footprint in inactive_footprints:
            self.active_footprints.remove(footprint)
            del footprint
        inactive_footprints.clear()
        
        if not self.track_foot_print:
            return

        # Intervals between footprints.
        time_now = time.time()
        if time_now < self.footprint_prev_spawn_time + Pet.FOOT_PRINT_SPAWN_INTERVAL:
            return
        self.footprint_prev_spawn_time = time_now

        foot_print_offset = Vector2(Pet.FOOT_X_LEFT_OFFSET, Pet.FOOT_Y_OFFSET) if self.anim_state == PetAnimState.WALK_LEFT else Vector2(Pet.FOOT_X_RIGHT_OFFSET, Pet.FOOT_Y_OFFSET)
        self.active_footprints.append(Footprints(self.pos + foot_print_offset, self.anim_state == PetAnimState.WALK_LEFT))

        # How long the foot prints would keep spawning for.
        if time_now > self.footprint_end_time:
            self.track_foot_print = False