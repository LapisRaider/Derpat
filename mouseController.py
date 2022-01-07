from pynput.mouse import Button, Controller

mouse = Controller()

#set mouse position
def setMousePos(x, y):
    mouse.position = (x, y)

#relative to current pos
def setMousePosRelative(xOffset, yOffset):
    mouse.move(xOffset, yOffset)

#get pos
def getMousePos():
    return mouse.position

#press mouse
def mousePress(left):
    if left:
        mouse.press(Button.left)
    else:
        mouse.press(Button.right)

#release mouse
def mouseRelease(left):
    if left:
        mouse.release(Button.left)
    else:
        mouse.release(Button.right)

#clicking mouse
def mouseClick(left, noTimes):
    if left:
        mouse.click(Button.left, noTimes)
    else:
        mouse.click(Button.right, noTimes)