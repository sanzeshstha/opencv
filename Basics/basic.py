import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Original Image',img)

# Display a grayscale image
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("B/W",gray)

# Blur an image
# blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# # #ksize should be positive and odd. Read documentation.
# # cv.imshow("Blur image",blur)

# # Edge cascade
# cascade = cv.Canny(blur,125,175)
# cv.imshow("Edge Cascade image",cascade)

# # Dilating the image
# dilated = cv.dilate(cascade,(3,3),iterations=3)
# cv.imshow("Dilation of canny image",dilated)

# # Eroding
# eroded = cv.erode(dilated,(3,3),iterations=3) #return the image same to cascading
# cv.imshow("Eroded Image",eroded)

# Resize image
# resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# #cv.INTER_AREA --> for shrinking the image to smaller dimensions than that of the original dimensions
# #cv.INTER_LINEAR or cv.INTER_CUBIC --> enlarge/scale image to larger dimensions
# # cv.INTER_CUBIC --> slower but image quality is better
# cv.imshow("Resized Image",resized)

# Cropping
# cropped = img[50:200,200:400]
# cv.imshow('Cropped',cropped)

cv.waitKey(0)
cv.destroyAllWindows()