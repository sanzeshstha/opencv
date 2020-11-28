import cv2 as cv

#Resize function for existing videos/pictures
def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

#Resize function for live videos (webcam,live telecast, etc.)
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

# Resizing Videos
# capture = cv.VideoCapture('Videos/dog.mp4')  #VideoCapture has other values for live videos (i.e.0,1,etc.)
# while True:
#     isTrue, frame = capture.read()
#     frame_rescaled = rescaleframe(frame)
#     #cv.imshow('Video',frame)
#     cv.imshow('Video Resized',frame_rescaled)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

#Resizing Pictures
img = cv.imread('Photos/cat.jpg')
img_resized = rescaleframe(img)
cv.imshow('Cat',img)
cv.imshow('Cat Resized',img_resized)
cv.waitKey(0)