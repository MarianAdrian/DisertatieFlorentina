from kivy.app import App
#kivy.require("1.8.0")                 why????

from kivy.uix.label import Label

class SimpleKivy(App):
    def build(self):
        return Label(text="Hello World!")
		
if __name__ == "__main__":
    SimpleKivy().run()