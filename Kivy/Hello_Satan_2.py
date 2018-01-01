from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage

class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(font_size=150,
                      size_hint_y=None,
                      height=200,
                      text='AVE Satan !')

        f = FloatLayout()
        s = Scatter()
        l = Label(text='AVE Satan !',
                  font_size=150)

        t.bind(text=l.setter('text'))
        i = AsyncImage(
                source="Behemoth.jpg",
                size_hint= (6, 6),
                pos_hint={'center_x':.5, 'center_y':.01})

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(t)
        b.add_widget(i)
        b.add_widget(f)

        return b

if __name__ == "__main__":
    TutorialApp().run()