import numpy as np
import cv2 as cv

haar_classifier = cv.CascadeClassifier('Face Detection/haar_cascade.xml')
# features = np.load('Face Detection/features.npy')
# labels = np.load('Face Detection/labels.npy')
people = ['Ben Affleck','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

face_recognise = cv.face.LBPHFaceRecognizer_create()
face_recognise.read('Face Detection/face_trained.yml')

img = cv.imread(r"/home/maitidevi/Documents/opencv-course/Resources/Faces/val/elton_john/1.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Persion",img)

#detect face in the image
faces_rect = haar_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]

    label,confidence = face_recognise.predict(faces_roi)
    print(f'{people[label]} detected with {confidence} confidence')

    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),thickness=1)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Face',img)

cv.waitKey(0)
cv.destroyAllWindows()