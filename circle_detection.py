import cv2
import numpy as np
from time import sleep

cap = cv2.VideoCapture(1);

height  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
width = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

centerX = 240
centerY = 320

# print(width,height)

a = 0
b = 0
relX = False
relY = False
isXCentered = False
isYCentered = False

while True:
    relX = False
    relY = False
    isXCentered = False
    isYCentered = False

    _, capt = cap.read()

    frame = cv2.rotate(capt, cv2.ROTATE_90_COUNTERCLOCKWISE)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    gray_blurred = cv2.blur(gray, (5, 5)) 
    
    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 60) 
    
    if detected_circles is not None: 

        detected_circles = np.uint16(np.around(detected_circles)) 
  
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2) 

            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3) 
            
            # print(pt)
            

    pay =30

    if a > width/2 + pay:
        # print("left")
        cv2.putText(frame, "left", (centerX, centerY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        relX = False
    elif a < width/2 - pay:
        # print("right")
        cv2.putText(frame, "right", (centerX, centerY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        relX = True
    elif (width/2 - pay) < a < (width/2 + pay):
        isXCentered = True

    if b > height/2 + pay:
        # print("up")
        cv2.putText(frame, "up", (centerX, centerY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        relX = False
    elif b < height/2 - pay:
        # print("down")
        cv2.putText(frame, "down", (centerX, centerY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        relX = True
    elif (height/2 - pay) < b < (height/2 + pay):
        isYCentered = True
    
    # print('x',relX,'y',relY,'\n')
    # print('is centered ',isXCentered,isYCentered,'\n')
    if isXCentered == isYCentered == True:
        # print("yük ile hizalandı, kıskaçlar açılıyor...")
        cv2.putText(frame, "alligned with the load, picking up", (centerX-50, centerY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    # sleep(0.2)
    cv2.imshow("frame", frame)


    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()