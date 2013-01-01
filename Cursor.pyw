import pythoncom, pyHook, win32api, win32con, ctypes, sys
from time import sleep

def moveRight():	
	for x in range(0, 20):
		
		win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 10,0)
		sleep(.08)
				
def moveLeft():	
	for x in range(0, 20):
		
		win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -10,0)
		sleep(.08)			
def moveDown():	
	for x in range(0, 20):
		
		win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0,10)
		sleep(.08)
def moveUp():	
	for x in range(0, 20):
		
		win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0,-10)
		sleep(.08)
		
def move1():
	moveRight()
	moveDown()
	moveLeft()
	moveUp()
	move2()

def move2():		
	def OnKeyboardEvent(event):
		if event.Key == "Media_Play_Pause":
			sys.exit()
		else:
			moveRight()
			moveDown()
			moveLeft()
			moveUp()

		#turn True to pass the event to other handlers
		return True

	#print ctrl	
	khm = pyHook.HookManager()
	# watch for all mouse events
	khm.KeyDown = OnKeyboardEvent
	# set the hook
	khm.HookKeyboard()
	pythoncom.PumpMessages()
	
	
def OnMouseEvent(event):
    # called when mouse events are received
	if event.MessageName == "mouse left down":
		sleep(1)
		ctypes.windll.user32.PostQuitMessage(0)
		move1()
		# create a hook manager
# return True to pass the event to other handlers
	return True


# create a hook manager
mhm = pyHook.HookManager()
# watch for all mouse events
mhm.MouseAll = OnMouseEvent
# set the hook
mhm.HookMouse()
# wait forever
pythoncom.PumpMessages()


# def click(x,y):
	# win32api.SetCursorPos((x,y))
	# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
# click(600,300)
