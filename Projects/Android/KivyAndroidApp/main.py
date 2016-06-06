from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from threading import Thread
#import time

from opencv import*

class _MainWindow(Widget):
    pass

class _Main(App):
    def build(self):
        return _MainWindow()
    def Run(self):
        return super(_Main, self).run()
    def VideoCapture(self):
        def _captureLoop():
            OpencvStream = OpencvVideoCapture()
            while(OpencvStream.StopVideoCapture() == False):
                camera_stream = OpencvStream.GetFrame()
        t = Thread(target=_captureLoop)
        t.start()

if __name__ == "__main__":
    _main_app = _Main()
    _main_app.VideoCapture()   #start video capture
    _main_app.Run()            #start application     