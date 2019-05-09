from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config


class BoxiLayout(GridLayout):
    pass

class MainLayout(GridLayout):
    pass


class MyLayout(GridLayout):
    box = BoxiLayout()
    main = MainLayout()
    def printMe(self):
        print(self.ids.mylabel.text)


class TutorialApp(App):
    def build(self):
        self.load_kv('mainn.kv')
        Config.set('graphics', 'resizable', '0')
        Config.set('graphics', 'width', '480')
        Config.set('graphics', 'height', '320')
        return MyLayout()


TutorialApp().run()