import cv2
from random import randrange

#load some pre trained data on face frontals from opencv
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#give that video or webcam starts with giveing arguement : 0 ,or give direct location of video like video1.mp4
webcam=cv2.VideoCapture(0)

#iterate forever over frames
while True:
    #read the current frame
    is_successful_frame_read,frame=webcam.read()

    #must convert into grayscale
    grayscale_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates=trained_face_data.detectMultiScale(grayscale_img)

    #draw rectangles
    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),10)

    #display
    cv2.imshow('ak face detector',frame)
    key=cv2.waitKey(1)

    #for quitting we dont want force quit just by q or Q
    #we use ascii value of both q and Q
    if key==81 or key==113:
        break
#release the Videocapture object
webcam.release() 