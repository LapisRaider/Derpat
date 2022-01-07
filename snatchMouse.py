from mouseController import *
import time

from vector2 import Vector2 
from petStates import PetState

FOLLOW_SPEED = 10
MOUSE_CATCH_OFFSET = 10 
SNATCH_TIME_AMT = 5 # in seconds

#pet follows the mouse ard
def followMouse(pet):
    mousePos = getMousePos()

    dir = mousePos.__sub__(pet.pos)
    dir = dir.normalised()
    
    pet.translate(round(dir.x) * FOLLOW_SPEED, round(dir.y) * FOLLOW_SPEED)

#check if pet close enough to grab the mouse
def checkGetMouse(pet):
    dir = getMousePos().__sub__(pet.pos)
    return dir.length() < MOUSE_CATCH_OFFSET

# update snatching the mouse
def snatchMouseUpdate(pet):
    followMouse(pet)

    #TODO:: might want to move this part somewhere else like the proper statemachine
    if checkGetMouse():
        pet.snatchStartTime = time.time()
        pet.state = PetState.CHASE_MOUSE

#behavior for taking the mouse and running away
def takeMouse(pet):
    #let go of mouse after a while
    if (time.time() > pet.snatchStartTime + SNATCH_TIME_AMT)
        return False

    #set random directions

    
    setMousePos(pet.pos.x, pet.pos.y) #mouse attached to pet

    pet.state = PetState.IDLE #TODO:: TEMP CODE REMOVE THIS

    return True

