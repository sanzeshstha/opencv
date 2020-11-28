#haar cascades are sensitive to noises in the image, so may or may not detect accurate faces.
#In order to reduce the noise, increase the minNeighbors parameter.

import cv2 as cv

img = cv.imread("Photos/group 1.jpg")
# cv.imshow("Original image",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #b/w image

haar_classifier = cv.CascadeClassifier('Face Detection/haar_cascade.xml') #Need to enter full absolute path to the xml file

faces_rect = haar_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'The number of faces found is : {len(faces_rect)}')
# print(faces_rect)

for x,y,i,j in faces_rect:
    cv.rectangle(img, (x,y), (x+i,y+j),(0,255,0),thickness=2)

cv.imshow("Detected Faces",img)

cv.waitKey(0)
cv.destroyAllWindows()