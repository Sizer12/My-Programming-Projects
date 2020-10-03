import numpy as np
from numpy import asarray
import cv2
import os
import keyboard
from time import sleep

path ="C:/Users/musta/Desktop/datas/mask"
i =0

cap = cv2.VideoCapture(1)

frameWidth = 640
frameHeight = 480

cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)

cap.set(cv2.CAP_PROP_GAIN, 0)

while True:
    check, frame = cap.read()

    margin = int(((frameWidth-frameHeight)/2))
    square_frame = frame[0:frameHeight, margin:margin + frameHeight]

    th1 = cv2.resize(square_frame, (224, 224))

    # ret,th1 = cv2.threshold(resized_img,127,255,cv2.THRESH_BINARY)

    if keyboard.is_pressed('q'):
        _, frame = cap.read()
        # cv2.imwrite('deneme'+str(i)+'.jpg',frame)
        cv2.imwrite(os.path.join(path , 'img'+str(i)+'.jpg'), th1)
        sleep(0.3)
        i+=1

    cv2.imshow("capture", th1)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()