import time
import random
import monitor

from system import System
from vector2 import Vector2
from mouseController import *
from pet import PetState
from pet import PetAnimState

class SnatchMouse(System):
    MAX_SNATCH_TIME_AMT = 5 # in seconds
    MIN_SNATCH_TIME_AMT = 3

    RUN_SPEED = 300

    MOUSE_OFFSET_RUN_LEFT = Vector2(10, 70)
    MOUSE_OFFSET_RUN_RIGHT = Vector2(110, 70)

    #to be init at the start
    def on_enter(self, pet):
        pet.snatchStartTime = time.time()
        pet.snatchTimeAmt = random.randrange(SnatchMouse.MIN_SNATCH_TIME_AMT, SnatchMouse.MAX_SNATCH_TIME_AMT)   
        self.mouseOffset = SnatchMouse.MOUSE_OFFSET_RUN_LEFT if pet.anim_state == PetAnimState.WALK_LEFT else SnatchMouse.MOUSE_OFFSET_RUN_RIGHT

        self.randomizeDir(pet)

    # update snatching the mouse
    def action(self, pet, delta_time):
        #let go of mouse after a while
        if (time.time() > pet.snatchStartTime + SnatchMouse.MAX_SNATCH_TIME_AMT):
            pet.next_state = PetState.IDLE
            return

        #check if out of screen and change direction
        if monitor.outOfRangeHori(pet.pos) or monitor.outOfRangeVert(pet.pos):
            self.randomizeDir(pet)

        pet.translate(round(self.runDir.x) * SnatchMouse.RUN_SPEED * delta_time, round(self.runDir.y) * SnatchMouse.RUN_SPEED * delta_time)

        #update animation
        if (self.runDir.x < 0 and pet.get_anim_state() != PetAnimState.WALK_LEFT):
            pet.set_anim_state(PetAnimState.WALK_LEFT)
            self.mouseOffset = SnatchMouse.MOUSE_OFFSET_RUN_LEFT
        elif (self.runDir.x >= 0 and pet.get_anim_state() != PetAnimState.WALK_RIGHT):
            pet.set_anim_state(PetAnimState.WALK_RIGHT)
            self.mouseOffset = SnatchMouse.MOUSE_OFFSET_RUN_RIGHT

        #update mouse pos
        newMousePos = self.mouseOffset.__add__(pet.pos)
        setMousePos(newMousePos.x, newMousePos.y) #mouse attached to pet

    def randomizeDir(self, pet):
        active_monitor = monitor.getMonitorOnScrPos(pet.get_position())
        self.minSize = Vector2(active_monitor.x, active_monitor.y)
        self.maxSize = Vector2(active_monitor.x + active_monitor.width, active_monitor.y + active_monitor.height)
        
        nextRandomPos = Vector2(random.randrange(self.minSize.x, self.maxSize.x), random.randrange(self.minSize.y, self.maxSize.y))
        self.runDir =(nextRandomPos.__sub__(pet.pos)).normalised()

