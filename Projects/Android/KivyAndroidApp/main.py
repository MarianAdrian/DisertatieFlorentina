from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.uix.image import Image
#from kivy.uix.scatter import Scatter
from threading import Thread
#from kivy.lang import Builder
#import kivy

from opencv import*

from kivy.logger import Logger
import logging
Logger.setLevel(logging.TRACE)

class _CV_Feed(Image):
    source = ''

class _MainWindow(FloatLayout):
    pass

class _Main(App):
    #def __init__(self):
    #    self.camera_stream = Image()
    #    pass
    def build(self):
        self.load_kv('kv_template\_main.kv')
        #root = self.root
        #return Builder.load_string(kv)
        #return Builder.load_string(kv)
        return _MainWindow()
    def Run(self):
        return super(_Main, self).run()
    def VideoCapture(self):
        def _captureLoop():
            #img = Image()
            OpencvStream = OpencvVideoCapture()
            while(OpencvStream.StopVideoCapture() == False):
                scamera_stream = OpencvStream.GetFrame()
                #Image.source = OpencvStream.GetFrame()
                #root.add_widget(picture)
                #scatter = Scatter()
                #image = Image(source='sun.jpg')
                #scatter.add_widget(OpencvStream.GetFrame())
        t = Thread(target=_captureLoop)
        t.start()

if __name__ == "__main__":
    _main_app = _Main()
    #_Main().run()
    _main_app.VideoCapture()   #start video capture
    _main_app.Run()            #start application     