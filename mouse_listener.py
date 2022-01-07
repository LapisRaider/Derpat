from pynput.mouse import Button
from pynput.mouse import Listener

left_click_pos = None

def on_move(x, y, button, pressed):
    return True

def on_scroll(x, y, button, pressed):
    return True

def on_click(x, y, button, pressed):
    if (button == Button.left):
        global left_click_pos
        left_click_pos = Vector2(x, y) if pressed else None
    return True

# Collect events until released
with Listener(on_move=None, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()