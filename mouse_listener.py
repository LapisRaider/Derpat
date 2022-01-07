from vector2 import Vector2
from pynput import mouse
from pynput.mouse import Button
from pynput.mouse import Listener

left_click_pos = None

def on_move(x, y):
    return True

def on_scroll(x, y, dx, dy):
    return True

def on_click(x, y, button, pressed):
    if (button == Button.left):
        global left_click_pos
        left_click_pos = Vector2(x, y) if pressed else None
    return True

# Non-blocking mouse listener.
listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listener.start()