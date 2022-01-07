from pynput.mouse import Listener
from mouseController import *
from monitor import *

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    mousepos = getMousePos()

    print("pos")
    print(mousepos.x)
    print(mousepos.y)
    if not pressed:
        # Stop listener
        return False

# Collect events until released
with Listener(on_move=None, on_click=on_click, on_scroll=None) as listener:
    listener.join()