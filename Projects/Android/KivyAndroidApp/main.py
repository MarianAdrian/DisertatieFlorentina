from kivy.app import App
from kivy.uix.widget import Widget

import cv2

#Projects\Android\KivyAndroidApp\haarcascade_frontalface_default.xml
class _MainWindow(Widget):
self.add_widget
    pass


class _Main(App):
    def build(self):
        return _MainWindow()

def _OpencvTest():
    faceCascade = cv2.CascadeClassifier('Projects\Android\KivyAndroidApp\haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
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
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

def _StartApp():
    if __name__ == '__main__':
        _Main().run()
        _OpencvTest()

_StartApp()      #start application