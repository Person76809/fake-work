import pyautogui
import time

# Move the mouse to the top-left corner of the screen
pyautogui.moveTo(0, 0, duration=1)

# Move the mouse in a square pattern
for i in range(4):
    # Move the mouse to the right
    pyautogui.moveRel(100, 0, duration=0.5)
    
    # Move the mouse down
    pyautogui.moveRel(0, 100, duration=0.5)
    
    # Move the mouse to the left
    pyautogui.moveRel(-100, 0, duration=0.5)
    
    # Move the mouse up
    pyautogui.moveRel(0, -100, duration=0.5)

# Wait for 3 seconds before exiting the script
time.sleep(3)
