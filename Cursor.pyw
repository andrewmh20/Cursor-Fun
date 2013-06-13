import pythoncom, pyHook, win32api, sys
import math
import threading, time
from time import sleep

# Radius is 250px
radius = 50

# Intervals in the circle
n_intervals = 50

# List of intervals
l_intervals = []
for i in range(0, n_intervals):
        l_intervals.append((i+1) * math.pi * 2 / n_intervals)
# Move the cursor in a circle
def move_circle():
        (x, y) = win32api.GetCursorPos()
        old_pos = (x, y)
        center = (x-radius, y)
        for i in l_intervals:
            p = (radius * math.cos(i), radius * math.sin(i))
            new_pos = (int(center[0]+p[0]), int(center[1]-p[1]))
            win32api.SetCursorPos(new_pos)
            sleep(0.01)

#attempt to stop pyHook hang...				
lock = threading.Lock()
def KeyEventThread1(i):
    lock.acquire()
    sys.exit()
    lock.release()
def KeyEventThread2(i):
    lock.acquire()
    move_circle()
    lock.release()


			
def OnKeyboardEvent(event):
	if event.Key == "Escape":
		t = threading.Thread(target=KeyEventThread1, args=(1,))
		t.start()
		sys.exit()
	else:
		t = threading.Thread(target=KeyEventThread2, args=(1,))
		t.start()
    # return True to pass the event to other handlers
	return True
    
def MouseEventThread(i):
	lock.acquire()
	sleep(.2) #So that mouse is not depressed when moved
	move_circle() # move the cursor
	hm.UnhookMouse() # unhook the mouse
	lock.release()  
	
def OnMouseEvent(event):
    # called when mouse events are received
	if event.MessageName == "mouse left down":
		t = threading.Thread(target=MouseEventThread, args=(1,))
		t.start()
	hm.HookKeyboard()
	return True


hm = pyHook.HookManager()
hm.MouseAll = OnMouseEvent
hm.KeyDown  = OnKeyboardEvent
# Hook the mouse
hm.HookMouse()
 # hook the keyboard

# Wait for any events
pythoncom.PumpMessages()