import os
import numpy as np
from numpy import asarray

labels_path = "C:/Users/musta/Desktop/labels.txt"
    # open input file label.txt
labelsfile = open(labels_path, 'r')

    # initialize classes and read in lines until there are no more
classes = []
line = labelsfile.readline()

# with open("C:/Users/musta/Desktop/labels.txt", encoding="utf-8") as f:
#     for line in f:
#         splitted = line.splitlines()
#         # splitted = splitted[0]
#         print(splitted)

# retrieve just class name and append to classes
while line:
    classes.append(line.split(' ', 1)[1].rstrip())
    
    line = labelsfile.readline()
print(classes[2])
labelsfile.close()
