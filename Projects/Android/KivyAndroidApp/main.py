from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image

from opencv import*

class _MainWindow(Widget):
    pass

class _Main(App):
    def build(self):
        #self.camera_stream = OpencvVideoCapture().GetFrame()
        return _MainWindow()
    def Run(self):
        return super(_Main, self).run()
        

def _StartApp():
    _Main().Run()
    OpencvStream = OpencvVideoCapture()
    while(True):
        _Main().camera_stream = OpencvStream.GetFrame()
        if OpencvStream.StopVideoCapture() == True:
            break

if __name__ == "__main__":
    _StartApp()      #start application