import cv2 as cv
import numpy as np
green = np.uint8([[[251,236,91 ]]])
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print( hsv_green )