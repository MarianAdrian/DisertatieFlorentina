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

smiles_detected = 0
frames_checked = 0
stare = 'None'

def _find_mouth(image, face_x, face_y, frame):
    global frames_checked
    global smiles_detected
    global stare
    frames_checked = frames_checked + 1
    # Detect mouths in the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    mouths = mouthCascade.detectMultiScale(
        image,
        scaleFactor=3.35, #increase if wrong objects are detected
        minNeighbors=5,
        minSize=(25, 15),
        #flags = cv2.CV_HAAR_SCALE_IMAGE                 #such a attribute does not exist
    )
    if len(mouths) == 0:
        if frames_checked >= 20:
            stare = 'sad'
            frames_checked = 0
    else:
        # Draw a rectangle around the mouths
        for (x, y, w, h) in mouths:
            smiles_detected = smiles_detected + 1
            #cv2.imshow('mouth',image[y:y+h, x:x+w])
            #cv2.rectangle(frame, (x, face_y+y), (x+w, y+h), (255, 0, 0), 2)
            if (smiles_detected/frames_checked >= 0.3) and (frames_checked >= 20):
                stare = 'happy'
                smiles_detected = 0
                frames_checked = 0
            if stare == 'happy':
                cv2.rectangle(frame, (face_x+x, face_y+y), (face_x+x+w, face_y+y+h), (255, 0, 0), 2)
                cv2.putText(frame,'Fericire',(10, 40), font, 1,(0,255,0),2,cv2.LINE_AA)
    
    if stare == 'sad':
        cv2.putText(frame,'Suparare',(10, 40), font, 1,(0,0,255),2,cv2.LINE_AA)

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
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        _find_mouth(frame[y:y+h, x:x+w], x, y, frame)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
