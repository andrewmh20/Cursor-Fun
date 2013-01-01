This is a python script to move the cursor in a circle when the mouse is clicked once, and subsequently move whenever a key on the keyboard is pressed. When a specific key is pressed the process exits.

The string on line 29 determines the key that terminates the script. Currently it is the Play/Pause button found on some keyboards. This may or may not work on each keyboard that has one. The script may also be terminated by ending the pythonw.exe process from the Task Manager. 

The script stops collecting key presses after 6 presses. The cause of this bug is currently unknown. At that point the script can be ended by ending the pythonw.exe process from the Task Manager.


Place in the startup folder of a friends computer (of course don't do anything illegal or anything that may get them mad at you) and have some fun!

Thanks doomrobo.

Tested on Windows 7 x64 SP1 with Python 2.7.3 x86

**External libraries:**

pywin32 -- http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/pywin32-218.win32-py2.7.exe/download

pyHook -- http://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/pyHook-1.5.1.win32-py2.7.exe/download