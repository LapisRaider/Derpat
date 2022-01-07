from mouseController import *
import math 

FOLLOW_SPEED = 10

#pet follows the mouse ard
def followMouse(pet):
    mousePos = getMousePos()
    
    # get directiopn vector and normalize
    dir = (mousePos[0] - pet.x, mousePos[1] - pet.y)
    length = math.sqrt(dir[0] * dir[0] + dir[1] * dir[1])

    try:
        dirNormalize = (dir[0] / length, dir[1] / length)
    except ZeroDivisionError:
        dirNormalize = (0,0)
    
    pet.translate(round(dirNormalize[0]) * FOLLOW_SPEED, round(dirNormalize[1]) * FOLLOW_SPEED)

#behavior for taking the mouse
def takeMouse(pet):
    #after a certain amt of time drop the mouse
    setMousePos(pet.x, pet.y) #mouse attached to pet

    #run ard

# update snatching the mouse
def snatchMouseUpdate(pet):
    followMouse(pet)

    #takeMouse()
