import pyautogui
from time import sleep
import keyboard
import timeit
import numpy as np
from PIL import ImageGrab, Image
import cv2

pyautogui.FAILSAFE = True;
dr = 0.2;

def ekle():
    sleep(0.5)
    pyautogui.scroll(500)
    pyautogui.moveTo(307, 216, duration=dr)
    pyautogui.leftClick()
    pyautogui.moveTo(356, 314, duration=dr)
    pyautogui.leftClick()
    pyautogui.typewrite('project_name',0.08)
    pyautogui.moveTo(888, 304, duration=dr)
    pyautogui.leftClick()
    pyautogui.moveTo(879, 351, duration=dr)
    pyautogui.leftClick()
    pyautogui.moveTo(1032, 310, duration=dr)
    pyautogui.leftClick()
    pyautogui.moveTo(477, 175, duration=dr)
    pyautogui.leftClick()
    pyautogui.moveTo(442, 152, duration=dr)
    pyautogui.leftClick()
    pyautogui.moveTo(1192, 701, duration=dr)
    pyautogui.leftClick()
    pyautogui.moveTo(933, 177, duration=dr)
    pyautogui.leftClick()

    img1 = ImageGrab.grab(bbox=(240, 96, 1057, 296))
    img_np1 = np.array(img1)
    gray1 = cv2.cvtColor(img_np1, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage1) = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
    
    sleep(1.5)
    
    img2 = ImageGrab.grab(bbox=(240, 96, 1057, 296))
    img_np2 = np.array(img2)
    gray2 = cv2.cvtColor(img_np2, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage2) = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
    
    difference = cv2.subtract(blackAndWhiteImage1, blackAndWhiteImage2)
    result = not np.any(difference)

    if result is True:
        pyautogui.typewrite('z')
        
    else:
        #print("Pictures are different")
        pyautogui.scroll(-500)
        pyautogui.moveTo(1301, 700, duration=dr)
        pyautogui.leftClick()
        sleep(0.5)
        pyautogui.moveTo(767, 273, duration=dr)
        pyautogui.leftClick()
        pyautogui.moveTo(724, 322, duration=dr)
        pyautogui.leftClick()
        pyautogui.moveTo(891, 281, duration=dr)
        pyautogui.leftClick()
        sleep(1)
    
while True:
    if keyboard.is_pressed('x'):
        break
    ekle()  
    #sc = timeit.timeit(ekle, number=1)
    #if sc>13 :
        #pyautogui.typewrite('z')
