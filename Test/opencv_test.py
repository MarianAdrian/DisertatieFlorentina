import numpy as np
import cv2
import sys

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('Test\haarcascade_frontalface_default.xml')
#mouthCascade = cv2.CascadeClassifier('Test\haarcascade_smile.xml')
mouthCascade = cv2.CascadeClassifier('Test\haarcascade_smile2.xml')
#mouthCascade = cv2.CascadeClassifier('Test\haarcascade_mouth.xml')          #this one detects mouth + eyes at random
#mouthCascade = cv2.CascadeClassifier('haar_mouth_cascade.xml')        #my mouth haar seems to detect nose instead

cap = cv2.VideoCapture(0)

frames_checked = 0
stare = 'None'
max_object = 0

def _getMax_Object(objects):
    return_value = 0
    global max_object
    for object in objects:
                 #w       #h
        if (object[2]*object[3])>=max_object:
            max_object = object[2]*object[3]
            return_value = object
    max_object = 0
    return return_value

def _find_mouth(image, face_x, face_y, frame):
    global frames_checked
    global stare
    frames_checked = frames_checked + 1
    # Detect mouths in the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    mouths = mouthCascade.detectMultiScale(
        image,
        scaleFactor=1.6, #increase if wrong objects are detected
        minNeighbors=5,
        minSize=(25, 15),
        #flags = cv2.CV_HAAR_SCALE_IMAGE                 #such a attribute does not exist
    )
    if len(mouths) == 0:
        if frames_checked >= 10:
            stare = 'sad'
            frames_checked = 0
    else:
        smile = _getMax_Object(mouths)
        stare = 'happy'
        frames_checked = 0
        # Draw a rectangle around the mouth
                                          #x               #y                 #x       #w               #y       #h
        cv2.rectangle(frame, (face_x+smile[0], face_y+smile[1]), (face_x+smile[0]+smile[2], face_y+smile[1]+smile[3]), (255, 0, 0), 2)
    if stare == 'happy':     
        cv2.putText(frame,'Bucurie',(10, 40), font, 1,(0,255,0),2,cv2.LINE_AA)
    elif stare == 'sad':
        cv2.putText(frame,'Tristete',(10, 40), font, 1,(0,0,255),2,cv2.LINE_AA)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.2, #increase if wrong objects are detected
        minNeighbors=5,
        minSize=(30, 30),
        #flags = cv2.CV_HAAR_SCALE_IMAGE                 #such a attribute does not exist
    )

    if len(faces)>0:
        face = _getMax_Object(faces)
                            #y      #y      #h       #x      #x      #w        #x       #y
        _find_mouth(frame[face[1]:face[1]+face[3], face[0]:face[0]+face[2]], face[0], face[1], frame)
        # Draw a rectangle around the face
                                #x      #y          #x        #w        #y       #h
        cv2.rectangle(frame, (face[0], face[1]), (face[0] + face[2], face[1] + face[3]), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
