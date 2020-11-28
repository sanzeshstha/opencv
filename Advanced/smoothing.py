import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow("Original image",img)

# Averaging (type of blurring)
cv.imshow("Average blur",cv.blur(img,(3,3)))

# Gaussian BLur
cv.imshow("Gaussian Blur",cv.GaussianBlur(img,(3,3),0))

# Median blur
cv.imshow("Median Blur",cv.medianBlur(img,3))

# Bilateral Blurring
cv.imshow("Bilateral blur",cv.bilateralFilter(img,10,35,25))

cv.waitKey(0)
cv.destroyAllWindows()