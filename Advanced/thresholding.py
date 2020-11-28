#Thresholding is binarization of an image(pixels are either black(0) or white(255))
#certain threshold value, compare each pixel to this threshold value
# if value is less then threshold value, assign black, else white
import cv2 as cv

img = cv.imread("Photos/cats.jpg")
# cv.imshow("Original Image",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #b/w image

#Simple Thresholding
# val, thres = cv.threshold(gray,160,255,cv.THRESH_BINARY) #pixel intensity that are greater than 160 are assigned 255(white)
# cv.imshow("Simple Thresholded Image",thres)

# val, thres = cv.threshold(gray,160,255,cv.THRESH_BINARY_INV)  #pixel intensity that are less than 160 are assigned 255(white)
# cv.imshow("Inverse Thresholded Image",thres)

#Adaptive Thresholding
adap_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,7)
cv.imshow("Adaptive Thesholding",adap_thresh)

cv.waitKey(0)
cv.destroyAllWindows()