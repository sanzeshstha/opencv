import os
import cv2 as cv
import numpy as np

# people = ['Ben Affleck','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
people = []
for i in os.listdir('Faces/train'):         #append all the names in the folders into a list
    people.append(i)

DIR = r'/home/maitidevi/Documents/opencv-course/Resources/Faces/train'

haar_classifier = cv.CascadeClassifier('Face Detection/haar_cascade.xml')

features = []  #the image arrays of the faces
labels = [] #for every face in the features list, points to the corresponding people

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+h]   #regions of interest --> faces detection
                features.append(faces_roi)
                labels.append(label)

create_train()
print("~~~~~~~~~~~~~~Training done~~~~~~~~~~~~~")

features = np.array(features,dtype=np.object)
labels = np.array(labels)

face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.train(features,labels)

face_recogniser.save('Face Detection/face_trained.yml')   #train this same face recogniser model into another file/directory
# np.save('Face Detection/features.npy',features)     #save the features of the trained image
# np.save('Face Detection/labels.npy',labels)         #save the labels of the trained image