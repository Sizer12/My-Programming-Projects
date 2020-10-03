import pyautogui
from time import sleep
import keyboard
import timeit
import numpy as np
from PIL import ImageGrab, Image
import cv2
import os

test = False

pyautogui.FAILSAFE = False;

def get_ss():
    img1 = ImageGrab.grab(bbox =(763,457,833,499))
    img_np1 = np.array(img1)
    gray1 = cv2.cvtColor(img_np1, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage1) = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(os.path.expanduser('~'),'Desktop','saved.jpg'), blackAndWhiteImage1)
    print('ss saved')

def detect_test():
    img2 = ImageGrab.grab(bbox =(763,457,833,499))
    img_np2 = np.array(img2)
    gray2 = cv2.cvtColor(img_np2, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage2) = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(os.path.expanduser('~'),'Desktop','current.jpg'), blackAndWhiteImage2)

    saved_pic = cv2.imread(os.path.join(os.path.expanduser('~'),'Desktop','saved.jpg'), 0)
    current_pic = cv2.imread(os.path.join(os.path.expanduser('~'),'Desktop','current.jpg'), 0)
    
    saved_np = np.array(saved_pic)
    current_np = np.array(current_pic)

    difference = cv2.subtract(saved_np, current_np)
    result = not np.any(difference)

    if result is True:
        #print('test is detected')
        status = 'test is detected'
    elif result is False:
        #print('test is not detected')
        status = 'test is not detected'
    return status

if detect_test()=='test is detected':
        test = True
elif detect_test()=='test is not detected':
        test = False
while True:
    if(test==True):
        q_count = int(input('Kaç soru var bu testte ?'))
        print('Sallıyorum cevapları hemen')
        pyautogui.moveTo(797,477, duration=0.2)
        pyautogui.leftClick()
        sleep(5)
        pyautogui.moveTo(1117,172, duration=0.2)
        #pyautogui.leftClick()
        pyautogui.leftClick()

        for i in range(q_count-1):
            pyautogui.move(0,50)
            pyautogui.leftClick()
            pyautogui.leftClick()

        pyautogui.moveTo(1263,670);pyautogui.leftClick()
        pyautogui.moveTo(894,523);pyautogui.leftClick()
        sleep(0.2)
        pyautogui.moveTo(1263,670);pyautogui.leftClick()
        sleep(0.2)
        pyautogui.moveTo(274,146);pyautogui.leftClick()


    else:
        print('Görünüyor ki bu bir test değil, bir test açtığıdan emin olduğunda tekrar başlat')
        break

