from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.graphics import Color, Rectangle

class SatanScreen_1(FloatLayout):
    def __init__(self, **kwargs):
        self.size = (100, 100)
        super(SatanScreen_1, self).__init__(**kwargs)
        #self.cols = 1
        self.add_widget(
            Image(
                source="Baphomet-Pentagram.jpg",
                size_hint=(1.5, 1.5),
                pos_hint={'center_x': .5, 'center_y': .6}))

class SatanScreen_2(FloatLayout):
    def __init__(self, **kwargs):
        self.size = (100, 100)
        super(SatanScreen_2, self).__init__(**kwargs)
        self.add_widget(
            Image(
                source="Behemoth.jpg",
                size_hint=(1, 1),
                pos_hint={'center_x': .5, 'center_y': .5}))
        self.add_widget(Button(text="Użytkownik:"))

class MyButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = 'Baphomet-Pentagram.jpg'

    def on_press(self):
        print("Behemoth")
        self.source = 'Behemoth.jpg'


    def on_release(self):
        self.source = 'Baphomet-Pentagram.jpg'
        print("Baphomet")

class Satan(App):
    def build(self):
        return MyButton()
if __name__ == "__main__":
    Satan().run()
