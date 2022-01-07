from screeninfo import get_monitors

#print(str(monitors)), debugging purpose


leftPosX = 0
rightPosX = 0

def initMonitors():
    for monitor in get_monitors():
        if monitor.x < leftPosX:
            leftPosX = monitor.x

        if monitor.width + monitor.x > rightPosX:
            rightPosX = monitor.width + monitor.x



#get which monitor you're in depending on pos X, y is unimpt here
def getMonitorOnScrPos(pos):
    for monitor in get_monitors():
        if pos.x >= monitor.x and pos.x <= monitor.x + monitor.width:
            return monitor

    return None

#check if out of monitor hori axis
def outOfRangeHori(pos):
    return pos.x < leftPosX or pos.x > rightPosX

#change if out of monitors vert axis
def outOfRangeVert(pos):
    currMonitor = getMonitorOnScrPos(pos)
    return pos.y > currMonitor.y + currMonitor.height or pos.y < 0
 