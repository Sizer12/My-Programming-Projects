import numpy as np
from PIL import ImageGrab, Image
import cv2
from time import sleep
import keyboard
import pyautogui

sleep(2)

while True:
                                #sleep(2)
    img1 = ImageGrab.grab(bbox=(1002, 486, 1108, 574))
    img_np1 = np.array(img1)
    gray1 = cv2.cvtColor(img_np1, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage1) = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
    #print('ilk fotoyu çektim, değiştir')
                                #sleep(2)
    img2 = ImageGrab.grab(bbox=(1002, 486, 1108, 574))
    img_np2 = np.array(img2)
    gray2 = cv2.cvtColor(img_np2, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage2) = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
    #print('ikinciyi de çektim hesaplıyorum')
                                #sleep(2)
    difference = cv2.subtract(blackAndWhiteImage1, blackAndWhiteImage2)
    result = not np.any(difference)

    if result is True:
        print(" ")
    else:
        #print("Pictures are different")
        pyautogui.rightClick()
        sleep(0.5)
        pyautogui.rightClick()
        print('item picked')
        sleep(2)
        #break
    if keyboard.is_pressed('q'):
        break
