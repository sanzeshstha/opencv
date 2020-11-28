import cv2 as cv

img = cv.imread('Photos/park.jpg')
# cv.imshow("Original Image",img)

#Gray scaling (B/W)
#cv.imshow('Gray Scaled',cv.cvtColor(img,cv.COLOR_BGR2GRAY))

# BGR to HSV
#cv.imshow('HSV color space(FULL)',cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL))
# cv.imshow('HSV color space',cv.cvtColor(img,cv.COLOR_BGR2HSV))

#BGR to LAB
cv.imshow('LAB color space',cv.cvtColor(img,cv.COLOR_BGR2LAB))

# BGR to RGB
#cv.imshow("RBG color space",cv.cvtColor(img,cv.COLOR_BGR2RGB))

# HSV to BGR
#cv.imshow("HSV to BGR",cv.cvtColor(cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL),cv.COLOR_HSV2BGR_FULL))

#LAB to BGR
cv.imshow("LAB to BGR",cv.cvtColor(cv.cvtColor(img,cv.COLOR_BGR2LAB),cv.COLOR_LAB2BGR))

cv.waitKey(0)
cv.destroyAllWindows()