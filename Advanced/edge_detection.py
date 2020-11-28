#gradients -->edge like regions present in a image(considering from programming perspective),different from an edge though(mathemtically)
import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("Original Image",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Laplacian method
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian Edge Detection",lap)

#Sobel Gradient Magnitude Representation
sobel_x = cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobel_x,sobel_y)
# cv.imshow("Sobel on X-axis",sobel_x)
# cv.imshow("Sobel on Y-axis",sobel_y)
cv.imshow("Combined Sobel",combined_sobel)

#Canny --> advanced algo, multi-stage process (one of the stages uses Sobel to compute gradients)
cv.imshow("Canny Method",cv.Canny(gray,150,175))

cv.waitKey(0)
cv.destroyAllWindows()