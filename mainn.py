from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.button import Button

#pos[3][3]=
class Game:
    myTurn = False

    def turnn(self, x, y):
        pass


class MyButton(Button):
    #id = "btn"
    text = "free"
    #background_disabled_normal = (1, 0, 0)
    #background_disabled_down = (1, 0, 0)
    disabled = False
    background_color = (255, 1, 1)
    def choose(self,  x, y):
        print("chosen: " + str(x) + " " + str(y));


class BoxLayout(GridLayout):
    pass


class MainLayout(GridLayout):
    pass


class MyLayout(GridLayout):
    #box = BoxiLayout()
    #main = MainLayout()
    game = Game()

    def printMe(self, x, y):
        print(self.ids.mylabel.text)
        print(x + y)
        print(self.children)

class TutorialApp(App):
    def build(self):
        self.load_kv('mainn.kv')
        Config.set('graphics', 'resizable', '0')
        Config.set('graphics', 'width', '480')
        Config.set('graphics', 'height', '320')
        return MyLayout()


TutorialApp().run()