import cv2
import numpy as np
a = cv2.imread("lena.jpg")
b = cv2.imread("baboon.jpg")
difference = cv2.subtract(a, b)    
result = not np.any(difference)
if result is True:
    print("Pictures are the same")
else:
    print("Pictures are different")