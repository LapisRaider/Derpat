from system import System
from vector2 import Vector2
from mouseController import *

class SnatchMouse(System):
    FOLLOW_SPEED = 10
    MOUSE_CATCH_OFFSET = 10 
    SNATCH_TIME_AMT = 5 # in seconds

    #pet follows the mouse ard
    def follow_mouse(self, pet):
        mousePos = getMousePos()
        # Get direction vector and normalise.
        dir_normalised = Vector2(mousePos[0] - pet.x, mousePos[1] - pet.y).normalised()
        pet.translate(round(dir_normalised.x) * SnatchMouse.FOLLOW_SPEED, round(dir_normalised.y) * SnatchMouse.FOLLOW_SPEED)

    #check if pet close enough to grab the mouse
    def checkGetMouse(pet):
        dir = getMousePos().__sub__(pet.pos)
        return dir.length() < MOUSE_CATCH_OFFSET

    #behavior for taking the mouse
    def take_mouse(self, pet):
        #after a certain amt of time drop the mouse
        setMousePos(pet.x, pet.y) #mouse attached to pet

    def action(self, pet):
        self.follow_mouse(pet)
