import pyautogui
from time import sleep
sleep(3)
if pyautogui.locateOnScreen('G:\z\inv.png'):
    sleep(2)
    pyautogui.hotkey('altleft', 'f4')
    print("CLOSING INVALID ID WINDOW")
else:
    print("....")
print("....")
sleep(2)
