# AnnoyingPet
Basic Tutorial: https://seebass22.github.io/python-desktop-pet-tutorial/
Handling Mouse Input: https://pythonhosted.org/pynput/mouse.html

# Keyboard Shortcuts
Quitting the Application: CTRL + ALT + 2 + 9 + Y (Yes, it is possible.)

# Dependencies:
Screen Information: pip install screeninfo
Mouse: pip install pynput
Keyboard: pip install keyboard
Window Movement: pip install pywin32
Audio: pip install playsound==1.2.2

# Solving pynput dependency issue:
Print out Python's PATH using Python.
```
import sys
print(sys.executable)
```
Copy the path printed onto the terminal type `<path> -m pip install pynput`