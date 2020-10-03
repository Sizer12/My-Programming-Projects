import cv2
import numpy as np
import imutils
from time import sleep

cap = cv2.VideoCapture(1);
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width,height)

relX = False
relY = False
isXCentered = False
isYCentered = False

cX=0
cY=0

while True:
    relX = False
    relY = False
    isXCentered = False
    isYCentered = False

    _, frame = cap.read()
    
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grayFrame, (5, 5), 0)
    ret, thresh = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	    cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draw the contour and center of the shape on the image
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(frame, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # pay =40
    print('x: ', cX, 'y: ', cY)
    # if cX > width/2 + pay:
    #     print("yukarı")
    #     # cv2.putText(frame, "yukarı", 320, 220, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    #     relX = False
    # elif cX < width/2 - pay:
    #     print("aşağı")
    #     # cv2.putText(frame, "aşağı", 320, 220, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    #     relX = True
    # elif (width/2 - pay) < cX < (width/2 + pay):
    #     isXCentered = True

    # if cY > height/2 + pay:
    #     print("sağa")
    #     # cv2.putText(frame, "sağa", 320, 220, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    #     relX = False
    # elif cY < height/2 - pay:
    #     print("sola")
    #     # cv2.putText(frame, "sola", 320, 220, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    #     relX = True
    # elif (height/2 - pay) < cY < (height/2 + pay):
    #     isYCentered = True
    
    # print('x',relX,'y',relY,'\n')
    # print('is centered ',isXCentered,isYCentered,'\n')
    # if isXCentered == isYCentered == True:
    #     print("yük ile hizalandı, kıskaçlar açılıyor...")
    #     # cv2.putText(frame, "yük ile hizalandı, kıskaçlar açılıyor...", 320, 220, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    cv2.imshow("capture", frame)
    # sleep(0.2)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()