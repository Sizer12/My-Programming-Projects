import numpy as np
from PIL import ImageGrab, Image
import cv2
from time import sleep
import keyboard
import os
import pyautogui

blackAndWhiteImage =[]
img_np1=[]
img_np2=[]

sleep(1)
directory = r'C:\Users\musta\Desktop\open-cv'
while True:
    os.chdir(directory)
    #bbox=(982, 506, 1108, 574)
    #cv2.imshow('window',blackAndWhiteImage)
    img1 = ImageGrab.grab()  # (bbox=x,y,width,height)
    img_np1 = np.array(img1)
    cv2.imwrite('img_np1.jpg', img_np1)
    print('first one is captured')
    sleep(2)
    
    img2 = ImageGrab.grab()
    img_np2 = np.array(img1)
    cv2.imwrite('img_np2.jpg', img_np2)
    print('second one is captured')
    sleep(2)
    #gray1 = cv2.cvtColor(img_np1, cv2.COLOR_BGR2GRAY)
    #gray2 = cv2.cvtColor(img_np2, cv2.COLOR_BGR2GRAY)
    #(thresh, blackAndWhiteImage1) = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
    #(thresh, blackAndWhiteImage2) = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
    
    difference = cv2.subtract(img_np1, img_np2) 
    result = not np.any(difference)
    img_np1=[]
    img_np2=[]
    
    print('differance is checked')
    sleep(2)
    if result is True:
        print("Pictures are the same")
        sleep(2)
        #blackAndWhiteImage1.cv2.imshow()
        #blackAndWhiteImage2.cv2.imshow()
    else:
        print("Pictures are different")
        sleep(1)
        break
    if keyboard.is_pressed('q'):
    #if cv2.waitKey(25) & 0xFF == ord('.'):
        #cv2.destroyAllWindows()
        break
#print(blackAndWhiteImage)

