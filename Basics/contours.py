import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg',1)
cv.imshow('Original image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray scaled',gray) #B/W image

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT) #blur the image
canny = cv.Canny(blur,125,175)
cv.imshow('Edges',canny) #show edges of the image
#We can use blur to reduce the edges to pass to the Contours function
# ----------------------OR-----------------------------
# We can use threshold to perform the same
#thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
# ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('Threshold',thresh)

# To find contours
# - Retrieval - LIST
# - Approximation - SIMPLE [Contour approximation — Approximating the shape of a contour from an irregular shape.]
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#mode(retrieval methods) in findContours:
# CV_RETR_EXTERNAL gives “outer” contours, so if you have (say) one contour enclosing another (like concentric circles), only the outermost is given.
# CV_RETR_LIST gives all the contours and doesn’t even bother calculating the hierarchy — good if you only want the contours and don’t care whether one is nested inside another.
# CV_RETR_CCOMP gives contours and organizes them into outer and inner contours. Every contour is either the outline of an object or the outline of an object inside another object (i.e. hole). The hierarchy is adjusted accordingly. This can be useful if (say) you want to find all the holes.
# CV_RETR_TREE calculates the full hierarchy of the contours. So you can say that object1 is nested 4 levels deep within object2 and object3 is also nested 4 levels deep.
print(f'{len(contours)} contours found!!')

# Drawing the contours on a blank black screen
blank = np.zeros(img.shape,dtype=np.uint8)
cv.imshow('Drawing contours',cv.drawContours(blank,contours,-1,(0,0,255),thickness=1))

cv.waitKey(0)
cv.destroyAllWindows()