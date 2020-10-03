import numpy as np
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from tensorflow import keras as tf
from gpiozero import Servo
from gpiozero import LED
from gpiozero import Button

from time import sleep

labels_path = "/home/pi/Desktop/labels.txt"
labelsfile = open(labels_path, 'r')

classes = []
line = labelsfile.readline()

while line:
    classes.append(line.split(' ', 1)[1].rstrip())
    line = labelsfile.readline()

labelsfile.close()

model_path = '/home/pi/Desktop/keras_model.h5'
model = tf.models.load_model(model_path, compile=False)

pan = Servo(12)
tilt = Servo(13)
pan.mid()
tilt.mid()
sleep(0.5)
pan.close()
tilt.close()

ir = Button(18)
relay = LED(22)

relay.off()

dly = 1

cap = cv2.VideoCapture(0)

frameWidth = 640
frameHeight = 480

cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)

cap.set(cv2.CAP_PROP_GAIN, 0)

np.set_printoptions(suppress=True)

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def left():
    print("Dropped left.")
    
    pan = Servo(12)
    tilt = Servo(13)
    
    tilt.min()
    sleep(dly)
    pan.min()
    sleep(dly)
    pan.mid()
    sleep(dly)
    tilt.mid()
    sleep(dly)
    
    pan.close()
    tilt.close()
    
def middle():
    print("Dropped middle.")
    
    pan = Servo(12)
    tilt = Servo(13)
    
    pan.min()
    sleep(dly)
    pan.mid()
    sleep(dly)
    
    pan.close()
    tilt.close()

def right():
    
    print("Dropped right.")
    
    pan = Servo(12)
    tilt = Servo(13)
    
    tilt.max()
    sleep(dly)
    pan.min()
    sleep(dly)
    pan.mid()
    sleep(dly)
    tilt.mid()
    sleep(dly)
    
    pan.close()
    tilt.close()

def classify():
    for i in range(1,6):
        
        relay.on()
        
        sleep(0.2)
        
        check, frame = cap.read()
        
        if frame is None:
            print("couldn't capture")

        margin = int(((frameWidth-frameHeight)/2))
        square_frame = frame[0:frameHeight, margin:margin + frameHeight]

        resized_img = cv2.resize(square_frame, (224, 224))

        ret,th1 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)

        image_array = np.asarray(th1)
        image_array = np.expand_dims(image_array, axis=2)

        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        
        #normalized_image_array = normalized_image_array[:, :, 1]
        normalized_image_array = normalized_image_array[224, 224, 0, :]
        
        data[0] = normalized_image_array

        predictions = model.predict(data)

        predictions = predictions[0]

        largest_index = np.argmax(predictions)
        
        if i%5==0:
            if predictions[largest_index] > 0.99:
                print("Object Detected: ")

                if largest_index==0:
                    print(classes[largest_index])
                    left()

                elif largest_index==1:
                    print(classes[largest_index])
                    middle()

                elif largest_index==2:
                    print(classes[largest_index])
                    right()

            else:
                print("undefined")
        
        relay.off()

while True:

    if ir.is_pressed:
        classify()
        #print("Classified")
        sleep(2)

    else:
        sleep(1)
        print("No object is detected")

