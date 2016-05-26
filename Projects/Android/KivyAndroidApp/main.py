from kivy.app import App
from kivy.uix.widget import Widget

import cv2

class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()