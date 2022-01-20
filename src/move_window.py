import random
import win32gui, win32com.client
import ctypes
import ctypes.wintypes
import monitor
import custom_windows

from ctypes.wintypes import HWND, DWORD
from pet import PetAnimState, PetState
from system import System
from vector2 import Vector2
from ctypes import c_int
from read_parameters import state_param_dict

## For moving non-tkInter windows

# Gets the current active window
# Rect[0] = x, Rect[1] = y, Rect[2] = width, Rect[3] = height
def get_active_window():
    return win32gui.GetForegroundWindow()

def set_window_pos(window, x, y):
    rect = win32gui.GetWindowRect(window)
    win32gui.MoveWindow(window,round(x),round(y),rect[2]-rect[0],rect[3]-rect[1],True)

# Callback function for EnumWindows
def window_enum_handler(hwnd, list):
    dwmapi = ctypes.WinDLL("dwmapi")
    dwmwa_cloaked = 14 
    is_cloaked = c_int(0)
    active_monitor = monitor.get_active_monitor(Vector2(0,0)) # Used to get screen width/height

    # Just tons of hard-coded checks to make sure I don't get any invalid windows.
    invalid_windows = ['', 'tk', 'Task Manager', custom_windows.NoteWindow.TITLE, custom_windows.ImageWindow.TITLE]
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) not in invalid_windows:
        dwmapi.DwmGetWindowAttribute(HWND(hwnd), DWORD(dwmwa_cloaked), ctypes.byref(is_cloaked), ctypes.sizeof(is_cloaked))
        if(is_cloaked.value == 0): # Checking if window is suspended.
            rect = win32gui.GetWindowRect(hwnd)
            if rect[0] > 0 and rect[0] < active_monitor.height and rect[1] > 0 and rect[1] < active_monitor.width: # If within window borders.
                if rect[2] - rect[0] > 0 and rect[3] - rect[1] > 0: # If size of window larger than 0.
                    list.append(hwnd)
                    print("Window Found:", win32gui.GetWindowText(hwnd))
    return True

def get_random_window():
    top_windows = []
    win32gui.EnumWindows(window_enum_handler,top_windows)
    if len(top_windows) > 0:
        random_num = random.randint(0,len(top_windows)-1)
        print("Random Window Selected: ",win32gui.GetWindowText(top_windows[random_num]))
        return top_windows[random_num]
    return None

class MoveWindow(System):
    DISTANCE_TO_TRAVEL = float(state_param_dict["MOVE_WIN_DIST_TO_TRAVEL"])
    MOVEMENT_SPEED = float(state_param_dict["MOVE_WIN_RUN_SPEED"])

    def __init__(self, delay=0, action_state=PetState.DEFAULT):
        # State 0 = moving to window, State 1 = moving window
        self.state = 0
        super().__init__(delay=delay, action_state=action_state)
        
    def on_enter(self, pet):
        print("On Enter Move Window")
        self.state = 0
        self.target_window = get_random_window()
        if self.target_window == None:
            pet.change_state(PetState.IDLE)
            return
        self.dist_travelled = 0
        rect = win32gui.GetWindowRect(self.target_window)
        direction = Vector2(rect[0]-pet.window.winfo_width(),rect[1]) - pet.pos
        self.target_window_pos = Vector2(rect[0],rect[1])
        if direction.x > 0:
            pet.set_anim_state(PetAnimState.WALK_RIGHT)
        else:
            pet.set_anim_state(PetAnimState.WALK_LEFT)

    def action(self,pet,delta_time):
        if self.target_window == None:
            pet.change_state(PetState.IDLE)
            return
        if self.state == 0:
            rect = win32gui.GetWindowRect(self.target_window)
            direction = Vector2(rect[0]-pet.window.winfo_width(),rect[1]) - pet.pos

            if direction.length() < 3:
                self.state = 1
                pet.set_anim_state(PetAnimState.WALK_RIGHT)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(self.target_window)
            else:
                normal = direction.normalised() * MoveWindow.MOVEMENT_SPEED * delta_time
                pet.translate(normal.x,normal.y)
        elif self.state == 1:
            movement = 1 * MoveWindow.MOVEMENT_SPEED * delta_time
            pet.translate(movement,0)
            self.dist_travelled = self.dist_travelled + movement
            self.target_window_pos.x = self.target_window_pos.x + movement
            set_window_pos(self.target_window,self.target_window_pos.x,self.target_window_pos.y)
            if self.dist_travelled >= MoveWindow.DISTANCE_TO_TRAVEL:
                pet.change_state(PetState.IDLE)