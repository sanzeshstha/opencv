import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype=np.uint8)

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370), 255, -1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

# cv.imshow("Rectangle",rectangle)
# cv.imshow("Circle",circle)

#bitwise AND
cv.imshow("Bitwise AND",cv.bitwise_and(circle,rectangle)) #returns common regions from the images(intersection)

#bitwise OR
cv.imshow("Bitwise OR",cv.bitwise_or(circle,rectangle)) #returns both intersecing and non-intersecting regions (union)

# bitwise xor
cv.imshow("Bitwise XOR",cv.bitwise_xor(circle,rectangle))  # returns non-intersecting regions

# bitwise not 
cv.imshow("Bitwise not",cv.bitwise_not(rectangle)) #inverts binary color of image 

cv.waitKey(0)
cv.destroyAllWindows()