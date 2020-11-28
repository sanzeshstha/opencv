import cv2 as cv

# Reading images
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0)

# Reading videos
capture = cv.VideoCapture('Videos/dog.mp4')
# capture = cv.VideoCapture(cv.CAP_ANY)   #capture from any available media (0 is default webcam,1 is installed webcam)
# capture.set(3,640) #setting width
# capture.set(4,480)  #setting height
# capture.set(10,100) #setting brightness

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()