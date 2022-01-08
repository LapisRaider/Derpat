from pynput.mouse import Button, Controller
from vector2 import Vector2 

mouse = Controller()

# Set mouse position
def set_mouse_pos(x, y):
    mouse.position = (x, y)

# Relative to current pos
def translate_mouse_pos(xOffset, yOffset):
    mouse.move(xOffset, yOffset)

# Get pos
def get_mouse_pos():
    return Vector2(mouse.position[0], mouse.position[1])

# Press mouse
def mouse_press(left):
    if left:
        mouse.press(Button.left)
    else:
        mouse.press(Button.right)

# Release mouse
def mouse_release(left):
    if left:
        mouse.release(Button.left)
    else:
        mouse.release(Button.right)

# Clicking mouse
def mouse_click(left, num_clicks):
    if left:
        mouse.click(Button.left, num_clicks)
    else:
        mouse.click(Button.right, num_clicks)