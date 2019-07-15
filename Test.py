# Python program to illustrate 
# template matching 
import cv2 
import numpy as np 

# Read the main image 
img_rgb = cv2.imread('object.JPG')

# Convert it to grayscale 
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 

# Read the template 
template = cv2.imread('original.jpg',0) 

# Store width and heigth of template in w and h 
w, h = template.shape[::-1] 

# Perform match operations. 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 

# Specify a threshold 
threshold = 0.8

cv2.imshow("Original Image", img_rgb)
cv2.imshow("Object", template)

cv2.moveWindow("Object", 10, 50);
cv2.moveWindow("Original Image", 200, 50);
 
 
# Store the coordinates of matched area in a numpy array 
loc = np.where( res >= threshold) 

# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 

# Show the final image with the matched area. 
cv2.imshow('Detected',img_rgb) 
