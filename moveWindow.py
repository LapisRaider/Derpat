import tkinter as tk
import time
import random
import win32gui

# Gets the current active window
# Rect[0] = x, Rect[1] = y, Rect[2] = width, Rect[3] = height
def getActiveWindow():
    return win32gui.GetForegroundWindow()

def translateWindow(window,x,y):
    if win32gui.GetForegroundWindow() == window:
        rect = win32gui.GetWindowRect(window)
        win32gui.MoveWindow(window,rect[0]+x,rect[1]+y,rect[2]-rect[0],rect[3]-rect[1],True)
        #win32gui.SetWindowPos(window,0,0,0,rect[2],rect[3],0x0004)
        rect = win32gui.GetWindowRect(window)
        print(win32gui.GetWindowText(window))
        print(rect)
        return True
    else:
        return False

# Callback function for EnumWindows
def windowEnumHandler(hwnd, list):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '' and win32gui.GetWindowText(hwnd) == "Command Prompt":
        list.append(hwnd)
        print("Window Name:", win32gui.GetWindowText(hwnd))
    return True

def getRandomWindow():
    top_windows = []
    win32gui.EnumWindows(windowEnumHandler,top_windows)
    if len(top_windows) > 0:
        randomNum = random.randint(0,len(top_windows))
        return top_windows[randomNum]
    else:
        return None
