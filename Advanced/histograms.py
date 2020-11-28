#Histograms -->allow to visualize distribution of pixel intensity of an image (grayscale or RGB)
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# img = cv.imread("Photos/cats 2.jpg")
# # cv.imshow("Original Image",img)

img = cv.imread('Photos/cats.jpg')
# cv.imshow("Original Image",img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)  #Gray scaled image

blank = np.zeros(img.shape[:2],dtype=np.uint8) #blank screen of size of the image

# circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1) #circle of radius 100 in the center of the blank screen

# mask = cv.bitwise_and(gray,gray,mask=circle) #intersect(mask) the gray image with the circle
# cv.imshow("Masked image",mask)


#grayscale histogram
# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256]) #calculate the histogram for the masked image

# plt.figure()
# plt.title("Grayscale histogram")
# plt.xlabel("Bins")
# plt.ylabel("No. of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#Coloured Histogram
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked image",masked)

plt.figure()
plt.title("Color histogram")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()