import tkinter as tk
import time
import random
import win32gui, win32com.client

from pet import PetAnimState, PetState
from system import System
from vector2 import Vector2

import ctypes
from ctypes import c_int
import ctypes.wintypes
from ctypes.wintypes import HWND, DWORD
dwmapi = ctypes.WinDLL("dwmapi")
DWMWA_CLOAKED = 14 
isCloaked = c_int(0)

import monitor

## For moving non-tkInter windows

# Gets the current active window
# Rect[0] = x, Rect[1] = y, Rect[2] = width, Rect[3] = height
def getActiveWindow():
    return win32gui.GetForegroundWindow()

def translateWindow(window,x,y):
    # Only moves the window if it is in the foreground
    #if win32gui.GetForegroundWindow() == window:
        rect = win32gui.GetWindowRect(window)
        win32gui.MoveWindow(window,rect[0]+x,rect[1]+y,rect[2]-rect[0],rect[3]-rect[1],True)
        #win32gui.SetWindowPos(window,0,0,0,rect[2],rect[3],0x0004)
        rect = win32gui.GetWindowRect(window)
        # For debugging
        #print(win32gui.GetWindowText(window))
        #print(rect)
        return True
    #else:
    #    return False

def setWindowPosition(window,x,y):
    rect = win32gui.GetWindowRect(window)
    win32gui.MoveWindow(window,round(x),round(y),rect[2]-rect[0],rect[3]-rect[1],True)


# Callback function for EnumWindows
def windowEnumHandler(hwnd, list):
    tempMonitor = monitor.getMonitorOnScrPos(Vector2(0,0)) # Used to get screen width/height

    #Just tons of checks to make sure I don't get any invalid windows
    invalid_windows = ['', 'tk', 'Task Manager', 'Meme', 'You have a note!']
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) not in invalid_windows:
        dwmapi.DwmGetWindowAttribute(HWND(hwnd), DWORD(DWMWA_CLOAKED), ctypes.byref(isCloaked), ctypes.sizeof(isCloaked))
        if(isCloaked.value == 0): # Checking if window is suspended
            rect = win32gui.GetWindowRect(hwnd)
            if rect[0] > 0 and rect[0] < tempMonitor.height and rect[1] > 0 and rect[1] < tempMonitor.width: # If within window borders
                if rect[2] - rect[0] > 0 and rect[3] - rect[1] > 0: # If size of window larger than 0
                    list.append(hwnd)
                    print("Window Name:", win32gui.GetWindowText(hwnd))
    return True

def getRandomWindow():
    top_windows = []
    win32gui.EnumWindows(windowEnumHandler,top_windows)
    if len(top_windows) > 0:
        randomNum = random.randint(0,len(top_windows)-1)
        print("Window Found:",win32gui.GetWindowText(top_windows[randomNum]))
        return top_windows[randomNum]
    else:
        return None

class MoveWindow(System):
    DISTANCE_TO_TRAVEL = 500
    MOVEMENT_SPEED = 300

    def __init__(self, delay=0, action_state=PetState.DEFAULT):
        # State 0 = moving to window, State 1 = moving window
        self.state = 0
        super().__init__(delay=delay, action_state=action_state)
        
    def on_enter(self, pet):
        self.state = 0
        self.targetWindow = getRandomWindow()
        if self.targetWindow == None:
            pet.change_state(PetState.IDLE)
            return
        self.distanceTravelled = 0
        rect = win32gui.GetWindowRect(self.targetWindow)
        direction = Vector2(rect[0]-pet.window.winfo_width(),rect[1]).__sub__(pet.pos)
        self.targetWindowPos = Vector2(rect[0],rect[1])
        if direction.x > 0:
            pet.set_anim_state(PetAnimState.WALK_RIGHT)
        else:
            pet.set_anim_state(PetAnimState.WALK_LEFT)

    def action(self,pet,delta_time):
        if self.targetWindow == None:
            pet.change_state(PetState.IDLE)
            return
        if self.state == 0:
            rect = win32gui.GetWindowRect(self.targetWindow)
            direction = Vector2(rect[0]-pet.window.winfo_width(),rect[1]).__sub__(pet.pos)

            if direction.length() < 3:
                self.state = 1
                pet.set_anim_state(PetAnimState.WALK_RIGHT)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(self.targetWindow)
            else:
                normal = direction.normalised() * MoveWindow.MOVEMENT_SPEED * delta_time
                pet.translate(normal.x,normal.y)
            # If window loses focus, return to idle state
            #if getActiveWindow() != self.targetWindow:
            #    pet.change_state(PetState.IDLE)
        elif self.state == 1:
            movement = 1 * MoveWindow.MOVEMENT_SPEED * delta_time
            pet.translate(movement,0)
            self.distanceTravelled = self.distanceTravelled + movement
            self.targetWindowPos.x = self.targetWindowPos.x + movement
            setWindowPosition(self.targetWindow,self.targetWindowPos.x,self.targetWindowPos.y)
            if self.distanceTravelled >= MoveWindow.DISTANCE_TO_TRAVEL:
                pet.change_state(PetState.IDLE)
