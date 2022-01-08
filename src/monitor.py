from screeninfo import get_monitors

min_pos_x = 0
max_pos_x = 0

def init_monitors():
    global min_pos_x
    global max_pos_x
    min_pos_x = 0
    max_pos_x = 0
    for monitor in get_monitors():
        if monitor.x < min_pos_x:
            min_pos_x = monitor.x
        if monitor.width + monitor.x > max_pos_x:
            max_pos_x = monitor.width + monitor.x

# Get which monitor you're in depending on pos X, y is unimpt here.
def get_active_monitor(pos):
    for monitor in get_monitors():
        if pos.x >= monitor.x and pos.x <= monitor.x + monitor.width:
            return monitor

    return get_monitors()[0]

# Check if out of monitor hori axis.
def outside_bounds_x(pos):
    global min_pos_x
    global max_pos_x
    return pos.x < min_pos_x or pos.x > max_pos_x

# Change if out of monitors vert axis.
def outside_bounds_y(pos):
    currMonitor = get_active_monitor(pos)
    return pos.y > currMonitor.y + currMonitor.height or pos.y < currMonitor.y
 