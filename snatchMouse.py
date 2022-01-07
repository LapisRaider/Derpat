from mouseController import *
import math

from vector2 import Vector2 

FOLLOW_SPEED = 10

#pet follows the mouse ard
def followMouse(pet):
    mousePos = getMousePos()

    dir = Vector2()
    dir = mousePos.__sub__(pet.pos)
    dir = dir.normalised()
    
    pet.translate(round(dir.x) * FOLLOW_SPEED, round(dir.y) * FOLLOW_SPEED)

#behavior for taking the mouse
def takeMouse(pet):
    #after a certain amt of time drop the mouse
    setMousePos(pet.pos.x, pet.pos.y) #mouse attached to pet

    #run ard

# update snatching the mouse
def snatchMouseUpdate(pet):
    followMouse(pet)

    #takeMouse()
