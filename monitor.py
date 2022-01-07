from screeninfo import get_monitors

minPosX = 0
maxPosX = 0

def initMonitors():
    global minPosX
    global maxPosX

    minPosX = 0
    maxPosX = 0

    for monitor in get_monitors():
        if monitor.x < minPosX:
            minPosX = monitor.x

        if monitor.width + monitor.x > maxPosX:
            maxPosX = monitor.width + monitor.x

#get which monitor you're in depending on pos X, y is unimpt here
def getMonitorOnScrPos(pos):
    for monitor in get_monitors():
        if pos.x >= monitor.x and pos.x <= monitor.x + monitor.width:
            return monitor

    return None

#check if out of monitor hori axis
def outOfRangeHori(pos):
    global minPosX
    global maxPosX

    return pos.x < minPosX or pos.x > maxPosX

#change if out of monitors vert axis
def outOfRangeVert(pos):
    currMonitor = getMonitorOnScrPos(pos)
    return pos.y > currMonitor.y + currMonitor.height or pos.y < currMonitor.y
 