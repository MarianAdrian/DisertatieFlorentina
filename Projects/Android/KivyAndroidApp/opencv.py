import cv2

class OpencvVideoCapture():
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('Projects\Android\KivyAndroidApp\haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
    def GetFrame(self):
        # Capture frame
        ret, frame = self.cap.read()
        
        # Detect faces in the image
        faces = self.faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.2, #increase if wrong objects are detected
            minNeighbors=5,
            minSize=(30, 30),
            #flags = cv2.CV_HAAR_SCALE_IMAGE                 #such a attribute does not exist
        )
        
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        return frame

    def StopVideoCapture(self):
        return_value = False
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()
            return_value = True
        return return_value
