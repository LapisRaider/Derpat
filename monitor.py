from screeninfo import get_monitors

#print(str(monitors)), debugging purpose

#get which monitor you're in depending on pos X, y is unimpt here
def getMonitorOnScrPos(pos):
    for monitor in get_monitors():
        if pos.x >= monitor.x and pos.x <= monitor.x + monitor.width:
            return monitor

    return None

