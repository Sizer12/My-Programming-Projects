import keyboard
from time import sleep

import pyautogui
#pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

dr = 0.2

while True:
    if keyboard.is_pressed('d'):
        print(pyautogui.position())
        #624,644
        
while True:
    if keyboard.is_pressed('q'):
        break
    pyautogui.moveTo(421, 206, duration=dr)
    pyautogui.leftClick()
    #entered textbox
    pyautogui.typewrite('botum.',0.08)
    #message typed
    pyautogui.moveTo(384, 262, duration=dr)
    pyautogui.leftClick()
    #checkbox checked
    pyautogui.moveTo(975, 263, duration=dr)
    pyautogui.leftClick()
    #dropdowned list
    pyautogui.moveTo(844, 335, duration=dr)
    pyautogui.leftClick()
    #group selected
    pyautogui.moveTo(1024, 261, duration=dr)
    pyautogui.leftClick()
    #published
        