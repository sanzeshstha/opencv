import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Black Blank',blank)

#paint a certain color in the blank black screen
# blank[250:350, 200:300] = 0,0,255
# cv.imshow("Red square",blank)

#Draw a rectangle
# cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,0,255),thickness=cv.FILLED) 
# #to fill the figure with the mentioned color, thickness=-1 or cv.FILLED
# cv.imshow("Rectangle",blank)

# Draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(0,0,255),thickness=-1)
# cv.imshow("Circle",blank)

#Draw a line
# cv.line(blank,(0,0),(250,250),(0,0,255),thickness=3)
# cv.imshow("Line",blank)

#Write text on the image
cv.putText(blank,'Hello World',(200,250),cv.FONT_HERSHEY_DUPLEX,1.0,(0,255,0),thickness=2)
cv.imshow("Text",blank)

cv.waitKey(0)