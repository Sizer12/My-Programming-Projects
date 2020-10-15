import numpy as np
from PIL import ImageGrab, Image
import cv2
from time import sleep
import keyboard
import pyautogui

sleep(2)
def grabIMG():
    img = ImageGrab.grab(bbox=(1002, 486, 1108, 574))
    img_np = np.array(img)
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return blackAndWhiteImage
while True:
    blackAndWhiteImage1 = grabIMG()
    blackAndWhiteImage2 = grabIMG()
    difference = cv2.subtract(blackAndWhiteImage1, blackAndWhiteImage2)
    result = not np.any(difference)

    if result is True:
        print(" ")
    else:
        pyautogui.rightClick()
        sleep(0.5)
        pyautogui.rightClick()
        print('item picked')
        sleep(2)
    if keyboard.is_pressed('q'):
        break
