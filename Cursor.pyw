import pythoncom, pyHook, win32api, win32con
import math
from time import sleep

# Radius is 250px
radius = 50

# Intervals in the circle
n_intervals = 50

# List of intervals
l_intervals = []
for i in range(0, n_intervals):
        l_intervals.append((i+1) * math.pi * 2 / n_intervals)

def move_circle():
        (x, y) = win32api.GetCursorPos()
        old_pos = (x, y)
        center = (x-radius, y)
        for i in l_intervals:
                p = (radius * math.cos(i), radius * math.sin(i))
                new_pos = (int(center[0]+p[0]), int(center[1]-p[1]))
                win32api.SetCursorPos(new_pos)
                sleep(0.01)


def OnKeyboardEvent(event):
    if event.Key == "Media_Play_Pause":
        exit()
    else:
        move_circle()

    # return True to pass the event to other handlers
    return True
    
    
def OnMouseEvent(event):
    # called when mouse events are received
        if event.MessageName == "mouse left down":
                move_circle()
        return True


mhm = pyHook.HookManager()
mhm.MouseAll = OnMouseEvent
mhm.KeyDown  = OnKeyboardEvent

mhm.HookMouse()
mhm.HookKeyboard()

pythoncom.PumpMessages()
