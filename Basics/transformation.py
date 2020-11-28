import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow("Original Image",img)

# Translation
# def translate(img,x,y):
#     tran = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img,tran,dimensions)

# # -x --> left
# # -y --> Up
# # x --> Right
# # y --> Down

# cv.imshow('Translated image',translate(img,100,-100))

#Rotation
# def rotate(img,angle,rotpoint=None):
#     (height,width) = img.shape[:2]
#     if rotpoint is None:
#         rotpoint = (width//2,height//2)
    
#     rotmat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
#     dimensions = (width,height)
#     return cv.warpAffine(img,rotmat,dimensions)

# cv.imshow("Rotation",rotate(img,-90))  # -ve clockwise and vice versa

# Resize image
#cv.imshow("Resized image",cv.resize(img,(500,500),interpolation=cv.INTER_AREA))

# Flipping image
cv.imshow("Fliped image",cv.flip(img,-1))
#flipcode --> 0 -->flip vertically(over x-axis) or reverse the image
#flipcode --> 1 --> flip horizontally(over y-axis) or mirror image of the original one
#flipcode --> -1 --> flip both ways (ver & hori)
cv.waitKey(0)
cv.destroyAllWindows()